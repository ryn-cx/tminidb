# TODO: Validate
"""Contains the TvSeries class."""

from __future__ import annotations

import json
from logging import NullHandler, getLogger

from tminidb.details.base import BaseDetails
from tminidb.details.tv_series.models import TvSeriesModel, model_validate_json
from tminidb.exceptions import (
    InvalidFileError,
    ResourceNotFoundError,
    SeriesNotFoundError,
)

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class TvSeries(BaseDetails[TvSeriesModel]):
    """Manage the TV series details file.

    Source: https://www.themoviedb.org/tv/{series_id}

    Example request:
        - GET /3/tv/{series_id}?
            - language=en-US
            - HTTP/2
        - Host: api.themoviedb.org
        - Accept: application/json
        - Authorization: Bearer __REDACTED__
    """

    MODEL = TvSeriesModel
    LOAD = staticmethod(model_validate_json)

    # TODO: Validate
    def __call__(
        self,
        series_id: int,
        *,
        append_to_response: str | None = None,
        language: str | None = None,
    ) -> TvSeriesModel:
        """Look the TV series up and return the model it is read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(
                series_id,
                append_to_response=append_to_response,
                language=language,
            ),
            log_id,
        )

    # TODO: Validate
    def download(
        self,
        series_id: int,
        *,
        append_to_response: str | None = None,
        language: str | None = None,
    ) -> str:
        """Download the TV series details file.

        Raises:
            SeriesNotFoundError: If no series is under that id.
        """
        log_id = self.get_log_id(self.download, locals())
        try:
            response = self._download(
                f"tv/{series_id}",
                append_to_response=append_to_response,
                language=language,
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise SeriesNotFoundError(series_id, err.status_code, err.response) from err
        return self._validate_download(response, series_id)

    # TODO: Validate
    @staticmethod
    def _validate_download(response: str, series_id: int) -> str:
        if json.loads(response).get("id") != series_id:
            raise InvalidFileError(
                field="series id",
                expected=series_id,
                response=response,
            )
        return response
