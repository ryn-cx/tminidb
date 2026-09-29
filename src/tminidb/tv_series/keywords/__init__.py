# TODO: Validate
"""Get the keywords that have been added to a TV series.

Source: https://developer.themoviedb.org/reference/tv-series-keywords
"""

from __future__ import annotations

import json
from logging import NullHandler, getLogger

from tminidb.base_api_endpoint import BaseEndpoint
from tminidb.exceptions import (
    InvalidFileError,
    ResourceNotFoundError,
    SeriesNotFoundError,
)
from tminidb.tv_series.keywords.models import (
    TvSeriesKeywordsModel,
    model_validate_json,
)

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class TvSeriesKeywords(BaseEndpoint):
    """Get the keywords that have been added to a TV series.

    Source: https://developer.themoviedb.org/reference/tv-series-keywords
    """

    # TODO: Validate
    def __call__(self, series_id: int) -> TvSeriesKeywordsModel:
        """Get the keywords that have been added to a TV series.

        Source: https://developer.themoviedb.org/reference/tv-series-keywords
        """
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(series_id), log_id)

    # TODO: Validate
    def download(self, series_id: int) -> str:
        """Download the TV series keywords file.

        Raises:
            SeriesNotFoundError: If no series is under that id.
        """
        log_id = self.get_log_id(self.download, locals())
        try:
            response = self._client.download(
                f"tv/{series_id}/keywords",
                params={},
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

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> TvSeriesKeywordsModel:
        """Load a TV series keywords file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)
