# TODO: Validate
"""Get the translations that have been added to a movie.

Source: https://developer.themoviedb.org/reference/movie-translations
"""

from __future__ import annotations

from logging import NullHandler, getLogger

from tminidb.base_api_endpoint import BaseEndpoint
from tminidb.exceptions import MovieNotFoundError, ResourceNotFoundError
from tminidb.movie.translations.models import (
    MovieTranslationsModel,
    model_validate_json,
)

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class MovieTranslations(BaseEndpoint):
    """Get the translations that have been added to a movie.

    Take a read through TMDB's language documentation for more information about
    languages on TMDB: https://developer.themoviedb.org/docs/languages

    Source: https://developer.themoviedb.org/reference/movie-translations
    """

    # TODO: Validate
    def __call__(self, movie_id: int) -> MovieTranslationsModel:
        """Get the translations that have been added to a movie.

        Source: https://developer.themoviedb.org/reference/movie-translations
        """
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(movie_id), log_id)

    # TODO: Validate
    def download(self, movie_id: int) -> str:
        """Download the movie translations file.

        Raises:
            MovieNotFoundError: If no movie is under that id.
        """
        log_id = self.get_log_id(self.download, locals())
        try:
            return self._client.download(
                f"movie/{movie_id}/translations",
                params={},
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise MovieNotFoundError(
                movie_id,
                err.status_code,
                err.response,
            ) from err

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> MovieTranslationsModel:
        """Read a downloaded movie translations file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)
