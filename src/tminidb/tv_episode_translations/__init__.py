# TODO: Validate
"""Contains the TvEpisodeTranslations class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any

from tminidb.base_api_endpoint import BaseEndpoint
from tminidb.exceptions import InvalidFileError
from tminidb.tv_episode_translations.models import TvEpisodeTranslationsModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class TvEpisodeTranslations(BaseEndpoint[TvEpisodeTranslationsModel]):
    """Manage the TV episode translations file.

    Wraps `GET /tv/{series_id}/season/{season_number}/episode/{episode_number}/translations`:
    https://developer.themoviedb.org/reference/tv-episode-translations
    """  # noqa: E501

    _response_model = TvEpisodeTranslationsModel

    def download(
        self,
        series_id: int,
        season_number: int,
        episode_number: int,
    ) -> dict[str, Any]:
        """Downloads the TV episode translations file."""
        log_id = self.get_log_id(self.download, locals())
        data = self._client.download(
            f"tv/{series_id}/season/{season_number}/episode/{episode_number}"
            "/translations",
            {},
            log_id=log_id,
        )
        # The response carries the episode's own id but neither the season nor
        # the episode number, so there is nothing here that can be checked
        # against what was asked for, only that the id is present at all.
        if "id" not in data:
            raise InvalidFileError(field="id", response=data)
        return data

    def download_and_parse(
        self,
        series_id: int,
        season_number: int,
        episode_number: int,
    ) -> TvEpisodeTranslationsModel:
        """Downloads and parses the TV episode translations file."""
        return self.parse(
            self.download(series_id, season_number, episode_number),
        )
