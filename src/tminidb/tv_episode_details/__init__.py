# TODO: Validate
"""Contains the TvEpisodeDetails class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any

from tminidb.base_api_endpoint import BaseEndpoint
from tminidb.exceptions import InvalidFileError
from tminidb.tv_episode_details.models import TvEpisodeDetailsModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class TvEpisodeDetails(BaseEndpoint[TvEpisodeDetailsModel]):
    """Manage the TV episode details file.

    Wraps `GET /tv/{series_id}/season/{season_number}/episode/{episode_number}`:
    https://developer.themoviedb.org/reference/tv-episode-details
    """

    _response_model = TvEpisodeDetailsModel

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
        log_id = self.get_log_id(self.download, locals())
        data = self._client.download(
            f"tv/{series_id}/season/{season_number}/episode/{episode_number}",
            {
                "append_to_response": append_to_response,
                "language": language or self._client.language,
            },
            log_id=log_id,
        )
        # `id` is the episode's own id, so the season and episode numbers are
        # what identify the file as the one that was asked for.
        if data.get("season_number") != season_number:
            raise InvalidFileError(field="season number", expected=season_number)
        if data.get("episode_number") != episode_number:
            raise InvalidFileError(field="episode number", expected=episode_number)
        return data

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
