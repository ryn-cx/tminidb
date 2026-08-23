# TODO: Validate
"""Contains the TvSeriesWatchProviders class."""

from __future__ import annotations

from logging import NullHandler, getLogger

from tminidb.exceptions import ResourceNotFoundError, SeriesNotFoundError
from tminidb.watch_providers.base import BaseWatchProviders
from tminidb.watch_providers.tv_series.models import (
    TvSeriesWatchProvidersModel,
    model_validate_json,
)

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class TvSeriesWatchProviders(BaseWatchProviders[TvSeriesWatchProvidersModel]):
    """Manage the TV series watch providers file.

    Source: https://www.themoviedb.org/tv/{series_id}/watch

    Example request:
        - GET /3/tv/{series_id}/watch/providers HTTP/2
        - Host: api.themoviedb.org
        - Accept: application/json
        - Authorization: Bearer __REDACTED__
    """

    MODEL = TvSeriesWatchProvidersModel
    LOAD = staticmethod(model_validate_json)

    # TODO: Validate
    def __call__(self, series_id: int) -> TvSeriesWatchProvidersModel:
        """Look the series' watch providers up and return the model."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(series_id), log_id)

    # TODO: Validate
    def download(self, series_id: int) -> str:
        """Download the TV series watch providers file.

        Raises:
            SeriesNotFoundError: If no series is under that id.
        """
        log_id = self.get_log_id(self.download, locals())
        try:
            response = self._download(
                f"tv/{series_id}/watch/providers",
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise SeriesNotFoundError(series_id, err.status_code, err.response) from err
        return self._validate_download(response, "series id", series_id)
