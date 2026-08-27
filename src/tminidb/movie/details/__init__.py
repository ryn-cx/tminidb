# TODO: Validate
"""Get the top level details of a movie by ID.

Source: https://developer.themoviedb.org/reference/movie-details
"""

from __future__ import annotations

import json
from logging import NullHandler, getLogger

from tminidb.base_details import BaseDetails
from tminidb.exceptions import (
    InvalidFileError,
    MovieNotFoundError,
    ResourceNotFoundError,
)
from tminidb.movie.details.models import MovieDetailsModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class MovieDetails(BaseDetails[MovieDetailsModel]):
    """Get the top level details of a movie by ID.

    This method supports using `append_to_response`. Read more about this at
    https://developer.themoviedb.org/docs/append-to-response

    Source: https://developer.themoviedb.org/reference/movie-details
    """

    MODEL = MovieDetailsModel
    LOAD = staticmethod(model_validate_json)

    # TODO: Validate
    def __call__(
        self,
        movie_id: int,
        *,
        append_to_response: str | None = None,
        language: str | None = None,
    ) -> MovieDetailsModel:
        """Get the top level details of a movie by ID.

        Source: https://developer.themoviedb.org/reference/movie-details
        """
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(
                movie_id,
                append_to_response=append_to_response,
                language=language,
            ),
            log_id,
        )

    # TODO: Validate
    def download(
        self,
        movie_id: int,
        *,
        append_to_response: str | None = None,
        language: str | None = None,
    ) -> str:
        """Download the movie details file.

        Raises:
            MovieNotFoundError: If no movie is under that id.
        """
        log_id = self.get_log_id(self.download, locals())
        try:
            response = self._download(
                f"movie/{movie_id}",
                append_to_response=append_to_response,
                language=language,
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise MovieNotFoundError(movie_id, err.status_code, err.response) from err
        return self._validate_download(response, movie_id)

    # TODO: Validate
    @staticmethod
    def _validate_download(response: str, movie_id: int) -> str:
        if json.loads(response).get("id") != movie_id:
            raise InvalidFileError(
                field="movie id",
                expected=movie_id,
                response=response,
            )
        return response
