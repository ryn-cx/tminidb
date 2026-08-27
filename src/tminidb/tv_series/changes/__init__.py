# TODO: Validate
"""Get the recent changes for a TV show.

Source: https://developer.themoviedb.org/reference/tv-series-changes
"""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import TYPE_CHECKING

from tminidb.base_changes import BaseChanges
from tminidb.exceptions import ResourceNotFoundError, SeriesNotFoundError
from tminidb.tv_series.changes.models import TvSeriesChangesModel, model_validate_json

if TYPE_CHECKING:
    from datetime import date

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class TvSeriesChanges(BaseChanges[TvSeriesChangesModel]):
    """Get the recent changes for a TV show.

    By default only the last 24 hours are returned.

    You can query up to 14 days in a single query by using the `start_date` and
    `end_date` query parameters.

    TV show changes are a little different than movie changes in that there are some
    edits on seasons and episodes that will create a top level change entry at the show
    level. These can be found under the season and episode keys. These keys will contain
    a `series_id` and `episode_id`. You can use the season changes and episode changes
    methods to look these up individually.

    A longer range is downloaded a window at a time by `download_merged`.

    Source: https://developer.themoviedb.org/reference/tv-series-changes
    """

    MODEL = TvSeriesChangesModel
    LOAD = staticmethod(model_validate_json)

    # TODO: Validate
    def __call__(
        self,
        series_id: int,
        *,
        start_date: date | None = None,
        end_date: date | None = None,
        page: int = 1,
    ) -> TvSeriesChangesModel:
        """Get the recent changes for a TV show.

        Source: https://developer.themoviedb.org/reference/tv-series-changes
        """
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(
                series_id,
                start_date=start_date,
                end_date=end_date,
                page=page,
            ),
            log_id,
        )

    # TODO: Validate
    def download(
        self,
        series_id: int,
        *,
        start_date: date | None = None,
        end_date: date | None = None,
        page: int = 1,
    ) -> str:
        """Download one window of the TV series change log.

        Raises:
            SeriesNotFoundError: If nothing is under that id.
        """
        log_id = self.get_log_id(self.download, locals())
        try:
            return self._download(
                f"tv/{series_id}/changes",
                start_date=start_date,
                end_date=end_date,
                page=page,
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise SeriesNotFoundError(series_id, err.status_code, err.response) from err

    # TODO: Validate
    def download_merged(
        self,
        series_id: int,
        start_date: date,
        end_date: date,
        *,
        page: int = 1,
    ) -> str:
        """Download the whole range as one file, a 14 day window at a time.

        Raises:
            SeriesNotFoundError: If nothing is under that id.
        """
        log_id = self.get_log_id(self.download_merged, locals())
        try:
            return self._download_merged(
                f"tv/{series_id}/changes",
                start_date=start_date,
                end_date=end_date,
                page=page,
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise SeriesNotFoundError(series_id, err.status_code, err.response) from err
