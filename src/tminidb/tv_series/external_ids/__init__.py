# TODO: Validate
"""Get the external ids that have been added to a TV series.

Source: https://developer.themoviedb.org/reference/tv-series-external-ids
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
from tminidb.tv_series.external_ids.models import (
    TvSeriesExternalIdsModel,
    model_validate_json,
)

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class TvSeriesExternalIds(BaseEndpoint):
    """Get the external ids that have been added to a TV series.

    Source: https://developer.themoviedb.org/reference/tv-series-external-ids
    """

    # TODO: Validate
    def __call__(self, series_id: int) -> TvSeriesExternalIdsModel:
        """Get the external ids that have been added to a TV series.

        Source: https://developer.themoviedb.org/reference/tv-series-external-ids
        """
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(series_id), log_id)

    # TODO: Validate
    def download(self, series_id: int) -> str:
        """Download the TV series external ids file.

        Raises:
            SeriesNotFoundError: If no series is under that id.
        """
        log_id = self.get_log_id(self.download, locals())
        try:
            response = self._client.download(
                f"tv/{series_id}/external_ids",
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
    def load(self, data: str, log_id: str = "") -> TvSeriesExternalIdsModel:
        """Load a TV series external ids file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)
