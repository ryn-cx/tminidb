# TODO: Validate
"""Contains the MovieWatchProviders class."""

from __future__ import annotations

from logging import NullHandler, getLogger

from tminidb.exceptions import MovieNotFoundError, ResourceNotFoundError
from tminidb.watch_providers.base import BaseWatchProviders
from tminidb.watch_providers.movie.models import (
    MovieWatchProvidersModel,
    model_validate_json,
)

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class MovieWatchProviders(BaseWatchProviders[MovieWatchProvidersModel]):
    """Manage the movie watch providers file.

    Source: https://www.themoviedb.org/movie/{movie_id}/watch

    Example request:
        - GET /3/movie/{movie_id}/watch/providers HTTP/2
        - Host: api.themoviedb.org
        - Accept: application/json
        - Authorization: Bearer __REDACTED__
    """

    MODEL = MovieWatchProvidersModel
    LOAD = staticmethod(model_validate_json)

    # TODO: Validate
    def __call__(self, movie_id: int) -> MovieWatchProvidersModel:
        """Look the movie's watch providers up and return the model."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(movie_id), log_id)

    # TODO: Validate
    def download(self, movie_id: int) -> str:
        """Download the movie watch providers file.

        Raises:
            MovieNotFoundError: If no movie is under that id.
        """
        log_id = self.get_log_id(self.download, locals())
        try:
            response = self._download(
                f"movie/{movie_id}/watch/providers",
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise MovieNotFoundError(movie_id, err.status_code, err.response) from err
        return self._validate_download(response, "movie id", movie_id)
