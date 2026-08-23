# TODO: Validate
"""Contains the TvEpisodeChanges class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import TYPE_CHECKING

from tminidb.changes.base import BaseChanges
from tminidb.changes.tv_episode.models import TvEpisodeChangesModel, model_validate_json
from tminidb.exceptions import EpisodeChangesNotFoundError, ResourceNotFoundError

if TYPE_CHECKING:
    from datetime import date

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class TvEpisodeChanges(BaseChanges[TvEpisodeChangesModel]):
    """Manage the TV episode change log file.

    By default the API answers with the last 24 hours. A range longer than 14
    days is downloaded a window at a time by `download_merged`.

    Source: https://developer.themoviedb.org/reference/tv-episode-changes-by-id

    Example request:
        - GET /3/tv/episode/{episode_id}/changes?
            - start_date=2026-08-18&
            - page=1
            - HTTP/2
        - Host: api.themoviedb.org
        - Accept: application/json
        - Authorization: Bearer __REDACTED__
    """

    MODEL = TvEpisodeChangesModel
    LOAD = staticmethod(model_validate_json)

    # TODO: Validate
    def __call__(
        self,
        episode_id: int,
        *,
        start_date: date | None = None,
        end_date: date | None = None,
        page: int = 1,
    ) -> TvEpisodeChangesModel:
        """Look the change log up and return the model it is read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(
                episode_id,
                start_date=start_date,
                end_date=end_date,
                page=page,
            ),
            log_id,
        )

    # TODO: Validate
    def download(
        self,
        episode_id: int,
        *,
        start_date: date | None = None,
        end_date: date | None = None,
        page: int = 1,
    ) -> str:
        """Download one window of the TV episode change log.

        Raises:
            EpisodeChangesNotFoundError: If nothing is under that id.
        """
        log_id = self.get_log_id(self.download, locals())
        try:
            return self._download(
                f"tv/episode/{episode_id}/changes",
                start_date=start_date,
                end_date=end_date,
                page=page,
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise EpisodeChangesNotFoundError(
                episode_id,
                err.status_code,
                err.response,
            ) from err

    # TODO: Validate
    def download_merged(
        self,
        episode_id: int,
        start_date: date,
        end_date: date,
        *,
        page: int = 1,
    ) -> str:
        """Download the whole range as one file, a 14 day window at a time.

        Raises:
            EpisodeChangesNotFoundError: If nothing is under that id.
        """
        log_id = self.get_log_id(self.download_merged, locals())
        try:
            return self._download_merged(
                f"tv/episode/{episode_id}/changes",
                start_date=start_date,
                end_date=end_date,
                page=page,
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise EpisodeChangesNotFoundError(
                episode_id,
                err.status_code,
                err.response,
            ) from err
