# TODO: Validate
"""Get the videos that belong to a TV series.

Source: https://developer.themoviedb.org/reference/tv-series-videos
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
from tminidb.tv_series.videos.models import TvSeriesVideosModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class TvSeriesVideos(BaseEndpoint):
    """Get the videos that belong to a TV series.

    Querying videos with a `language` parameter will filter the results. If you
    want to include a fallback language you can use the `include_video_language`
    parameter. This should be a comma separated value like so:
    `include_video_language=en,null`.

    Source: https://developer.themoviedb.org/reference/tv-series-videos
    """

    # TODO: Validate
    def __call__(
        self,
        series_id: int,
        *,
        include_video_language: str | None = None,
        language: str | None = None,
    ) -> TvSeriesVideosModel:
        """Get the videos that belong to a TV series.

        Source: https://developer.themoviedb.org/reference/tv-series-videos
        """
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(
                series_id,
                include_video_language=include_video_language,
                language=language,
            ),
            log_id,
        )

    # TODO: Validate
    def download(
        self,
        series_id: int,
        *,
        include_video_language: str | None = None,
        language: str | None = None,
    ) -> str:
        """Download the TV series videos file.

        Raises:
            SeriesNotFoundError: If no series is under that id.
        """
        log_id = self.get_log_id(self.download, locals())
        try:
            response = self._client.download(
                f"tv/{series_id}/videos",
                params={
                    "include_video_language": include_video_language,
                    "language": language or self._client.language,
                },
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
    def load(self, data: str, log_id: str = "") -> TvSeriesVideosModel:
        """Load a TV series videos file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)
