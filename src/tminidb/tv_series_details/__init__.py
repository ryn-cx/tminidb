# TODO: Validate
"""Contains the TvSeriesDetails class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any

from tminidb.base_api_endpoint import BaseEndpoint
from tminidb.tv_series_details.models import TvSeriesDetailsModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class TvSeriesDetails(BaseEndpoint[TvSeriesDetailsModel]):
    """Manage the TV series details file.

    Wraps `GET /tv/{series_id}`:
    https://developer.themoviedb.org/reference/tv-series-details
    """

    _response_model = TvSeriesDetailsModel

    def get_log_id(
        self,
        series_id: int,
        *,
        append_to_response: str | None = None,
        language: str | None = None,
    ) -> str:
        """Build the log id for a download."""
        return self.append_non_default_args(
            f"{self.__class__.__name__} {series_id=}",
            append_to_response=(append_to_response, None),
            language=(language, None),
        )

    def download(
        self,
        series_id: int,
        *,
        append_to_response: str | None = None,
        language: str | None = None,
    ) -> dict[str, Any]:
        """Downloads the TV series details file."""
        return self._client.download(
            f"tv/{series_id}",
            {
                "append_to_response": append_to_response,
                "language": language or self._client.language,
            },
            log_id=self.get_log_id(
                series_id,
                append_to_response=append_to_response,
                language=language,
            ),
        )

    def download_and_parse(
        self,
        series_id: int,
        *,
        append_to_response: str | None = None,
        language: str | None = None,
    ) -> TvSeriesDetailsModel:
        """Downloads and parses the TV series details file."""
        return self.parse(
            self.download(
                series_id,
                append_to_response=append_to_response,
                language=language,
            ),
        )
