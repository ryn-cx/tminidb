# TODO: Validate
"""Contains the TvSeasonChanges class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any

from tminidb.base_api_endpoint import BaseEndpoint
from tminidb.exceptions import InvalidFileError
from tminidb.tv_season_changes.models import TvSeasonChangesModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class TvSeasonChanges(BaseEndpoint[TvSeasonChangesModel]):
    """Manage the TV season changes file.

    Wraps `GET /tv/season/{season_id}/changes`:
    https://developer.themoviedb.org/reference/tv-season-changes

    Every change is grouped under the field it happened to, and each group
    holds one item per edit. An item carries `value`, and `original_value` when
    the edit replaced something, but what those hold depends on the field the
    group is for, so a change is only meaningful alongside its `key`.

    The window defaults to the last 24 hours and cannot be wider than 14 days.
    Nothing in the response says which TV season it is for, and an id that
    belongs to no TV season is answered with an empty list rather than with an
    error, so an empty result does not mean the id was good.
    """

    _response_model = TvSeasonChangesModel

    # TODO: Validate
    def download(
        self,
        season_id: int,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
        page: int = 1,
    ) -> dict[str, Any]:
        """Downloads the TV season changes file.

        Args:
            season_id: The TV season to read the changes of.
            start_date: Oldest change to return, as `YYYY-MM-DD`.
            end_date: Newest change to return, as `YYYY-MM-DD`.
            page: Page of changes to return.
        """
        log_id = self.get_log_id(self.download, locals())
        data = self._client.download(
            f"tv/season/{season_id}/changes",
            {
                "start_date": start_date,
                "end_date": end_date,
                "page": page,
            },
            log_id=log_id,
        )
        # Nothing in the response identifies the TV season it is for, so the
        # only thing worth checking is that there is a list of changes at all.
        if data.get("changes") is None:
            raise InvalidFileError(field="changes", response=data)
        return data

    # TODO: Validate
    def download_and_parse(
        self,
        season_id: int,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
        page: int = 1,
    ) -> TvSeasonChangesModel:
        """Downloads and parses the TV season changes file."""
        return self.parse(
            self.download(
                season_id,
                start_date=start_date,
                end_date=end_date,
                page=page,
            ),
        )
