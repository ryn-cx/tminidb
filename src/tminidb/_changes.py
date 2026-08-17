# TODO: Validate
"""Helpers shared by the changes endpoints.

Every changes endpoint answers with the same shape, a list of groups keyed by
the field that was edited, and every one of them refuses a window wider than 14
days. Walking a longer window therefore means asking for it a chunk at a time
and stitching the answers back together, which is what these do.
"""

from __future__ import annotations

from datetime import UTC, datetime, timedelta
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Callable, Iterator
    from datetime import date

MAX_WINDOW_DAYS = 14


# TODO: Validate
def today() -> date:
    """Return the current date."""
    return datetime.now(UTC).date()


# TODO: Validate
def date_chunks(
    start_date: date,
    end_date: date,
    days: int = MAX_WINDOW_DAYS,
) -> Iterator[tuple[date, date]]:
    """Split `start_date` to `end_date` into windows of at most `days` days.

    The windows share their boundary days because the API counts both ends of a
    window, so the last day of one window is the first day of the next. That
    hands back the same edits twice, which is why merging deduplicates.

    A start on or after the end is still one window, since asking for a single
    day is a sensible thing to want and an empty iterator would silently answer
    it with nothing.
    """
    if start_date >= end_date:
        yield (start_date, start_date)
        return

    window = timedelta(days=days)
    chunk_start = start_date
    while chunk_start < end_date:
        chunk_end = min(chunk_start + window, end_date)
        yield (chunk_start, chunk_end)
        chunk_start = chunk_end


# TODO: Validate
def download_chunks(
    start_date: date,
    end_date: date | None,
    download: Callable[[str, str], dict[str, Any]],
) -> dict[str, Any]:
    """Download every 14 day window between the dates and merge the answers.

    Args:
        start_date: Oldest change to return.
        end_date: Newest change to return. Defaults to today.
        download: Downloads one window, given its start and end as `YYYY-MM-DD`.

    Returns:
        One response holding the changes of every window, in the same shape a
        single window comes back in. Groups that show up in more than one window
        are merged into one group, and edits that show up twice, either because
        two windows share a boundary day or because the API repeated them, are
        kept once.
    """
    merged: dict[str, list[dict[str, Any]]] = {}
    seen: set[tuple[str, str]] = set()
    for chunk_start, chunk_end in date_chunks(start_date, end_date or today()):
        data = download(chunk_start.isoformat(), chunk_end.isoformat())
        for group in data["changes"]:
            items = merged.setdefault(group["key"], [])
            for item in group["items"]:
                item_id = (group["key"], item["id"])
                if item_id in seen:
                    continue
                seen.add(item_id)
                items.append(item)
    return {"changes": [{"key": key, "items": items} for key, items in merged.items()]}
