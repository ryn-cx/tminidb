# TODO: Validate
"""Contains the TvEpisodeDetails class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any

from tminidb.base_api_endpoint import BaseEndpoint
from tminidb.tv_episode_details.models import TvEpisodeDetailsModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class TvEpisodeDetails(BaseEndpoint[TvEpisodeDetailsModel]):
    """Manage the TV episode details file.

    Wraps `GET /tv/{series_id}/season/{season_number}/episode/{episode_number}`:
    https://developer.themoviedb.org/reference/tv-episode-details
    """

    _response_model = TvEpisodeDetailsModel

    def get_log_id(
        self,
        series_id: int,
        season_number: int,
        episode_number: int,
        *,
        append_to_response: str | None = None,
        language: str | None = None,
    ) -> str:
        """Build the log id for a download."""
        return self.append_non_default_args(
            f"{self.__class__.__name__} {series_id=} {season_number=} "
            f"{episode_number=}",
            append_to_response=(append_to_response, None),
            language=(language, None),
        )

    def download(
        self,
        series_id: int,
        season_number: int,
        episode_number: int,
        *,
        append_to_response: str | None = None,
        language: str | None = None,
    ) -> dict[str, Any]:
        """Downloads the TV episode details file."""
        return self._client.download(
            f"tv/{series_id}/season/{season_number}/episode/{episode_number}",
            {
                "append_to_response": append_to_response,
                "language": language or self._client.language,
            },
            log_id=self.get_log_id(
                series_id,
                season_number,
                episode_number,
                append_to_response=append_to_response,
                language=language,
            ),
        )

    def download_and_parse(
        self,
        series_id: int,
        season_number: int,
        episode_number: int,
        *,
        append_to_response: str | None = None,
        language: str | None = None,
    ) -> TvEpisodeDetailsModel:
        """Downloads and parses the TV episode details file."""
        return self.parse(
            self.download(
                series_id,
                season_number,
                episode_number,
                append_to_response=append_to_response,
                language=language,
            ),
        )
