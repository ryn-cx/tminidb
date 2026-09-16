# TODO: Validate
"""Get the similar movies based on genres and keywords.

Source: https://developer.themoviedb.org/reference/movie-similar
"""

from __future__ import annotations

from logging import NullHandler, getLogger

from tminidb.base_similar import BaseSimilar
from tminidb.exceptions import MovieNotFoundError, ResourceNotFoundError
from tminidb.movie.similar.models import MovieSimilarModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class MovieSimilar(BaseSimilar[MovieSimilarModel]):
    """Get the similar movies based on genres and keywords.

    This method only looks for other items based on genres and plot keywords. As
    such, the results found here are not always going to be 100%. Use it with
    that in mind.

    Source: https://developer.themoviedb.org/reference/movie-similar
    """

    MODEL = MovieSimilarModel
    LOAD = staticmethod(model_validate_json)

    # TODO: Validate
    def __call__(
        self,
        movie_id: int,
        *,
        language: str | None = None,
        page: int = 1,
    ) -> MovieSimilarModel:
        """Get the similar movies based on genres and keywords.

        Source: https://developer.themoviedb.org/reference/movie-similar
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
        """Download one page of movies similar to a movie.

        Raises:
            MovieNotFoundError: If no movie is under that id.
        """
        log_id = self.get_log_id(self.download, locals())
        try:
            return self._download(
                f"movie/{movie_id}/similar",
                language=language,
                page=page,
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise MovieNotFoundError(movie_id, err.status_code, err.response) from err
