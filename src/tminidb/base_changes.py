# TODO: Validate
"""Contains the BaseChanges class."""

from __future__ import annotations

import json
from datetime import timedelta
from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any

from pydantic import BaseModel

from tminidb.base_api_endpoint import BaseEndpoint

if TYPE_CHECKING:
    from collections.abc import Callable, Iterator
    from datetime import date

logger = getLogger(__name__)
logger.addHandler(NullHandler())

WINDOW = timedelta(days=14)
"""The longest range TMDB answers a single changes request for."""


# TODO: Validate
def date_chunks(start_date: date, end_date: date) -> Iterator[tuple[date, date]]:
    """Split a date range into the 14 day windows the API answers for."""
    if start_date >= end_date:
        yield (start_date, start_date)
        return

    day = timedelta(days=1)
    chunk_start = start_date
    while chunk_start <= end_date:
        chunk_end = min(chunk_start + WINDOW, end_date)
        yield (chunk_start, chunk_end)
        chunk_start = chunk_end + day


# TODO: Validate
class BaseChanges[T: BaseModel](BaseEndpoint):
    """Base class for an endpoint that answers with a change log.

    Every changes endpoint takes the same parameters and differs only in the
    path it is under and the model it is read with.

    Source: https://developer.themoviedb.org/reference/movie-changes
    """

    MODEL: type[T]
    """The model this endpoint reads its responses with."""

    LOAD: Callable[[str | bytes | object, str], T]
    """The `model_validate_json` its model's module generates."""

    # TODO: Validate
    def _download(
        self,
        endpoint: str,
        *,
        start_date: date | None,
        end_date: date | None,
        page: int,
        log_id: str,
    ) -> str:
        return self._client.download(
            endpoint,
            params={
                "start_date": start_date.isoformat() if start_date else None,
                "end_date": end_date.isoformat() if end_date else None,
                "page": page,
            },
            log_id=log_id,
        )

    # TODO: Validate
    def _download_merged(
        self,
        endpoint: str,
        *,
        start_date: date,
        end_date: date,
        page: int,
        log_id: str,
    ) -> str:
        """Download every 14 day window of the range and merge them into one file."""
        merged: dict[str, list[dict[str, Any]]] = {}
        for chunk_start, chunk_end in date_chunks(start_date, end_date):
            window = self._download(
                endpoint,
                start_date=chunk_start,
                end_date=chunk_end,
                page=page,
                log_id=log_id,
            )
            for change in json.loads(window)["changes"]:
                merged.setdefault(change["key"], []).extend(change["items"])
        changes = [{"key": key, "items": items} for key, items in merged.items()]
        return json.dumps({"changes": changes})

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> T:
        """Read a downloaded change log file into its model."""
        return type(self).LOAD(data, log_id or type(self).__name__)
