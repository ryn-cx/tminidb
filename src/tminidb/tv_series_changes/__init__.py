# TODO: Validate
"""Contains the TvSeriesChanges class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any

from tminidb.base_api_endpoint import BaseEndpoint
from tminidb.exceptions import InvalidFileError
from tminidb.tv_series_changes.models import TvSeriesChangesModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class TvSeriesChanges(BaseEndpoint[TvSeriesChangesModel]):
    """Manage the TV series changes file.

    Wraps `GET /tv/{series_id}/changes`:
    https://developer.themoviedb.org/reference/tv-series-changes

    Every change is grouped under the field it happened to, and each group
    holds one item per edit. An item carries `value`, and `original_value` when
    the edit replaced something, but what those hold depends on the field the
    group is for, so a change is only meaningful alongside its `key`.

    The window defaults to the last 24 hours and cannot be wider than 14 days.
    Nothing in the response says which TV series it is for, and an id that
    belongs to no TV series is answered with an empty list rather than with an
    error, so an empty result does not mean the id was good.
    """

    _response_model = TvSeriesChangesModel

    # TODO: Validate
    def download(
        self,
        series_id: int,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
        page: int = 1,
    ) -> dict[str, Any]:
        """Downloads the TV series changes file.

        Args:
            series_id: The TV series to read the changes of.
            start_date: Oldest change to return, as `YYYY-MM-DD`.
            end_date: Newest change to return, as `YYYY-MM-DD`.
            page: Page of changes to return.
        """
        log_id = self.get_log_id(self.download, locals())
        data = self._client.download(
            f"tv/{series_id}/changes",
            {
                "start_date": start_date,
                "end_date": end_date,
                "page": page,
            },
            log_id=log_id,
        )
        # Nothing in the response identifies the TV series it is for, so the
        # only thing worth checking is that there is a list of changes at all.
        if data.get("changes") is None:
            raise InvalidFileError(field="changes", response=data)
        return data

    # TODO: Validate
    def download_and_parse(
        self,
        series_id: int,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
        page: int = 1,
    ) -> TvSeriesChangesModel:
        """Downloads and parses the TV series changes file."""
        return self.parse(
            self.download(
                series_id,
                start_date=start_date,
                end_date=end_date,
                page=page,
            ),
        )
