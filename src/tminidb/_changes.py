"""Utilities for downloading changes from TMDB."""

from __future__ import annotations

from datetime import timedelta
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Callable, Iterator
    from datetime import date


def date_chunks(start_date: date, end_date: date) -> Iterator[tuple[date, date]]:
    """Chunk a date range into 14 day chunks."""
    if start_date >= end_date:
        yield (start_date, start_date)
        return

    window = timedelta(days=14)
    day = timedelta(days=1)
    chunk_start = start_date
    while chunk_start <= end_date:
        chunk_end = min(chunk_start + window, end_date)
        yield (chunk_start, chunk_end)
        chunk_start = chunk_end + day


# TODO: Validate
def download_changes(
    start_date: date | None,
    end_date: date | None,
    download: Callable[[str | None, str | None], dict[str, Any]],
) -> dict[str, Any]:
    """Download changes with automatic date chunking."""
    if start_date is None or end_date is None:
        return download(
            start_date.isoformat() if start_date else None,
            end_date.isoformat() if end_date else None,
        )

    merged: dict[str, list[dict[str, Any]]] = {}
    for chunk_start, chunk_end in date_chunks(start_date, end_date):
        download_response = download(chunk_start.isoformat(), chunk_end.isoformat())
        for change in download_response["changes"]:
            merged.setdefault(change["key"], []).extend(change["items"])
    return {"changes": [{"key": key, "items": items} for key, items in merged.items()]}
