# TODO: Validate
"""Get the translations that have been added to a TV episode.

Source: https://developer.themoviedb.org/reference/tv-episode-translations
"""

from __future__ import annotations

from logging import NullHandler, getLogger

from tminidb.base_api_endpoint import BaseEndpoint
from tminidb.exceptions import EpisodeNotFoundError, ResourceNotFoundError
from tminidb.tv_episode.translations.models import (
    TvEpisodeTranslationsModel,
    model_validate_json,
)

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class TvEpisodeTranslations(BaseEndpoint):
    """Get the translations that have been added to a TV episode.

    Take a read through TMDB's language documentation for more information about
    languages on TMDB: https://developer.themoviedb.org/docs/languages

    Source: https://developer.themoviedb.org/reference/tv-episode-translations
    """

    # TODO: Validate
    def __call__(
        self,
        series_id: int,
        season_number: int,
        episode_number: int,
    ) -> TvEpisodeTranslationsModel:
        """Get the translations that have been added to a TV episode.

        Source: https://developer.themoviedb.org/reference/tv-episode-translations
        """
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(series_id, season_number, episode_number),
            log_id,
        )

    # TODO: Validate
    def download(
        self,
        series_id: int,
        season_number: int,
        episode_number: int,
    ) -> str:
        """Download the TV episode translations file.

        Raises:
            EpisodeNotFoundError: If the series has no such episode.
        """
        log_id = self.get_log_id(self.download, locals())
        try:
            return self._client.download(
                f"tv/{series_id}/season/{season_number}/episode/{episode_number}"
                "/translations",
                params={},
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise EpisodeNotFoundError(
                series_id,
                season_number,
                episode_number,
                err.status_code,
                err.response,
            ) from err

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> TvEpisodeTranslationsModel:
        """Read a downloaded TV episode translations file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)
