# TODO: Validate
"""Get the details of a TV show.

Source: https://developer.themoviedb.org/reference/tv-series-details
"""

from __future__ import annotations

import json
from logging import NullHandler, getLogger

from tminidb.base_details import BaseDetails
from tminidb.exceptions import (
    InvalidFileError,
    ResourceNotFoundError,
    SeriesNotFoundError,
)
from tminidb.tv_series.details.models import TvSeriesDetailsModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class TvSeriesDetails(BaseDetails[TvSeriesDetailsModel]):
    """Get the details of a TV show.

    This method supports using `append_to_response`. Read more about this at
    https://developer.themoviedb.org/docs/append-to-response

    Source: https://developer.themoviedb.org/reference/tv-series-details
    """

    MODEL = TvSeriesDetailsModel
    LOAD = staticmethod(model_validate_json)

    # TODO: Validate
    def __call__(
        self,
        series_id: int,
        *,
        append_to_response: str | None = None,
        language: str | None = None,
    ) -> TvSeriesDetailsModel:
        """Get the details of a TV show.

        Source: https://developer.themoviedb.org/reference/tv-series-details
        """
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
