# TODO: Validate
"""Contains the TvEpisodeChanges class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any

from tminidb._changes import download_chunks
from tminidb.base_api_endpoint import BaseEndpoint
from tminidb.exceptions import InvalidFileError
from tminidb.tv_episode_changes.models import TvEpisodeChangesModel

if TYPE_CHECKING:
    from datetime import date

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class TvEpisodeChanges(BaseEndpoint[TvEpisodeChangesModel]):
    """Manage the TV episode changes file.

    Wraps `GET /tv/episode/{episode_id}/changes`:
    https://developer.themoviedb.org/reference/tv-episode-changes

    Every change is grouped under the field it happened to, and each group
    holds one item per edit. An item carries `value`, and `original_value` when
    the edit replaced something, but what those hold depends on the field the
    group is for, so a change is only meaningful alongside its `key`.

    The window defaults to the last 24 hours and cannot be wider than 14 days.
    Nothing in the response says which TV episode it is for, and an id that
    belongs to no TV episode is answered with an empty list rather than with an
    error, so an empty result does not mean the id was good.
    """

    _response_model = TvEpisodeChangesModel

    # TODO: Validate
    def download(
        self,
        episode_id: int,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
        page: int = 1,
    ) -> dict[str, Any]:
        """Downloads the TV episode changes file.

        Args:
            episode_id: The TV episode to read the changes of.
            start_date: Oldest change to return, as `YYYY-MM-DD`.
            end_date: Newest change to return, as `YYYY-MM-DD`.
            page: Page of changes to return.
        """
        log_id = self.get_log_id(self.download, locals())
        data = self._client.download(
            f"tv/episode/{episode_id}/changes",
            {
                "start_date": start_date,
                "end_date": end_date,
                "page": page,
            },
            log_id=log_id,
        )
        # Nothing in the response identifies the TV episode it is for, so the
        # only thing worth checking is that there is a list of changes at all.
        if data.get("changes") is None:
            raise InvalidFileError(field="changes", response=data)
        return data

    # TODO: Validate
    def download_and_parse(
        self,
        episode_id: int,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
        page: int = 1,
    ) -> TvEpisodeChangesModel:
        """Downloads and parses the TV episode changes file."""
        return self.parse(
            self.download(
                episode_id,
                start_date=start_date,
                end_date=end_date,
                page=page,
            ),
        )

    # TODO: Validate
    def download_since(
        self,
        episode_id: int,
        start_date: date,
        *,
        end_date: date | None = None,
        page: int = 1,
    ) -> dict[str, Any]:
        """Downloads every TV episode change since a date, 14 days at a time.

        A window cannot be wider than 14 days, so a longer one is asked for a
        chunk at a time and the chunks are merged into a single response of the
        same shape a single window comes back in.

        Args:
            episode_id: The TV episode to read the changes of.
            start_date: Oldest change to return.
            end_date: Newest change to return. Defaults to today.
            page: Page of changes to return from each window.
        """
        return download_chunks(
            start_date,
            end_date,
            lambda chunk_start, chunk_end: self.download(
                episode_id,
                start_date=chunk_start,
                end_date=chunk_end,
                page=page,
            ),
        )

    # TODO: Validate
    def download_and_parse_since(
        self,
        episode_id: int,
        start_date: date,
        *,
        end_date: date | None = None,
        page: int = 1,
    ) -> TvEpisodeChangesModel:
        """Downloads and parses every TV episode change since a date."""
        return self.parse(
            self.download_since(
                episode_id,
                start_date,
                end_date=end_date,
                page=page,
            ),
        )
