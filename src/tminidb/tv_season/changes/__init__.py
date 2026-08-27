# TODO: Validate
"""Get the recent changes for a TV season.

Source: https://developer.themoviedb.org/reference/tv-season-changes-by-id
"""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import TYPE_CHECKING

from tminidb.base_changes import BaseChanges
from tminidb.exceptions import ResourceNotFoundError, SeasonChangesNotFoundError
from tminidb.tv_season.changes.models import TvSeasonChangesModel, model_validate_json

if TYPE_CHECKING:
    from datetime import date

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class TvSeasonChanges(BaseChanges[TvSeasonChangesModel]):
    """Get the recent changes for a TV season.

    By default only the last 24 hours are returned.

    You can query up to 14 days in a single query by using the `start_date` and
    `end_date` query parameters.

    TV season changes are a little different than movie changes in that there are some
    edits on episodes that will create a top level change entry at the season level.
    These can be found under the episode keys. These keys will contain a `episode_id`.
    You can use the episode changes methods to look these up individually.

    A longer range is downloaded a window at a time by `download_merged`.

    Source: https://developer.themoviedb.org/reference/tv-season-changes-by-id
    """

    MODEL = TvSeasonChangesModel
    LOAD = staticmethod(model_validate_json)

    # TODO: Validate
    def __call__(
        self,
        season_id: int,
        *,
        start_date: date | None = None,
        end_date: date | None = None,
        page: int = 1,
    ) -> TvSeasonChangesModel:
        """Get the recent changes for a TV season.

        Source: https://developer.themoviedb.org/reference/tv-season-changes-by-id
        """
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(
                season_id,
                start_date=start_date,
                end_date=end_date,
                page=page,
            ),
            log_id,
        )

    # TODO: Validate
    def download(
        self,
        season_id: int,
        *,
        start_date: date | None = None,
        end_date: date | None = None,
        page: int = 1,
    ) -> str:
        """Download one window of the TV season change log.

        Raises:
            SeasonChangesNotFoundError: If nothing is under that id.
        """
        log_id = self.get_log_id(self.download, locals())
        try:
            return self._download(
                f"tv/season/{season_id}/changes",
                start_date=start_date,
                end_date=end_date,
                page=page,
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise SeasonChangesNotFoundError(
                season_id,
                err.status_code,
                err.response,
            ) from err

    # TODO: Validate
    def download_merged(
        self,
        season_id: int,
        start_date: date,
        end_date: date,
        *,
        page: int = 1,
    ) -> str:
        """Download the whole range as one file, a 14 day window at a time.

        Raises:
            SeasonChangesNotFoundError: If nothing is under that id.
        """
        log_id = self.get_log_id(self.download_merged, locals())
        try:
            return self._download_merged(
                f"tv/season/{season_id}/changes",
                start_date=start_date,
                end_date=end_date,
                page=page,
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise SeasonChangesNotFoundError(
                season_id,
                err.status_code,
                err.response,
            ) from err
