# TODO: Validate
"""Contains the TvSeriesChanges class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import TYPE_CHECKING

from tminidb.changes.base import BaseChanges
from tminidb.changes.tv_series.models import TvSeriesChangesModel, model_validate_json
from tminidb.exceptions import ResourceNotFoundError, SeriesNotFoundError

if TYPE_CHECKING:
    from datetime import date

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class TvSeriesChanges(BaseChanges[TvSeriesChangesModel]):
    """Manage the TV series change log file.

    By default the API answers with the last 24 hours. A range longer than 14
    days is downloaded a window at a time by `download_merged`.

    Source: https://developer.themoviedb.org/reference/tv-series-changes

    Example request:
        - GET /3/tv/{series_id}/changes?
            - start_date=2026-08-18&
            - page=1
            - HTTP/2
        - Host: api.themoviedb.org
        - Accept: application/json
        - Authorization: Bearer __REDACTED__
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
        """Look the change log up and return the model it is read into."""
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
