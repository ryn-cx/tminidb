# TODO: Validate
"""Get a list of recommended movies for a movie.

Source: https://developer.themoviedb.org/reference/movie-recommendations
"""

from __future__ import annotations

from logging import NullHandler, getLogger

from tminidb.base_recommendations import BaseRecommendations
from tminidb.exceptions import MovieNotFoundError, ResourceNotFoundError
from tminidb.movie.recommendations.models import (
    MovieRecommendationsModel,
    model_validate_json,
)

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class MovieRecommendations(BaseRecommendations[MovieRecommendationsModel]):
    """Get a list of recommended movies for a movie.

    Source: https://developer.themoviedb.org/reference/movie-recommendations
    """

    MODEL = MovieRecommendationsModel
    LOAD = staticmethod(model_validate_json)

    # TODO: Validate
    def __call__(
        self,
        movie_id: int,
        *,
        language: str | None = None,
        page: int = 1,
    ) -> MovieRecommendationsModel:
        """Get a list of recommended movies for a movie.

        Source: https://developer.themoviedb.org/reference/movie-recommendations
        """
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(movie_id, language=language, page=page),
            log_id,
        )

    # TODO: Validate
    def download(
        self,
        movie_id: int,
        *,
        language: str | None = None,
        page: int = 1,
    ) -> str:
        """Download one page of movies recommended for a movie.

        Raises:
            MovieNotFoundError: If no movie is under that id.
        """
        log_id = self.get_log_id(self.download, locals())
        try:
            return self._download(
                f"movie/{movie_id}/recommendations",
                language=language,
                page=page,
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise MovieNotFoundError(movie_id, err.status_code, err.response) from err
