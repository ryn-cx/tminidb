"""Get the translations that have been added to a TV episode.

Take a read through our
[language](https://developer.themoviedb.org/docs/languages) documentation for
more information about languages on TMDB.

[Official Documentation](https://developer.themoviedb.org/reference/tv-episode-translations)
"""

from __future__ import annotations

from logging import NullHandler, getLogger

from tminidb.base_endpoint import BaseEndpoint, records_call
from tminidb.tv_episodes.translations.models import Translations

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class TvEpisodeTranslations(BaseEndpoint):
    """Get the translations that have been added to a TV episode.

    Take a read through our
    [language](https://developer.themoviedb.org/docs/languages) documentation for
    more information about languages on TMDB.

    [Official Documentation](https://developer.themoviedb.org/reference/tv-episode-translations)
    """

    @records_call
    def __call__(
        self,
        series_id: int,
        season_number: int,
        episode_number: int,
    ) -> Translations:
        """Get the translations that have been added to a TV episode.

        Take a read through our
        [language](https://developer.themoviedb.org/docs/languages) documentation
        for more information about languages on TMDB.

        [Official Documentation](https://developer.themoviedb.org/reference/tv-episode-translations)

        The response carries the episode's own id but neither the season nor
        the episode number, so there is nothing in it that can be checked
        against what was asked for.
        """
        log_id = self.log_id()
        data = self._client.download(
            f"tv/{series_id}/season/{season_number}/episode/{episode_number}"
            "/translations",
            {},
            log_id=log_id,
        )
        return Translations.from_response(data)
