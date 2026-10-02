# TODO: Validate
"""Get the external ids that have been added to a movie.

Source: https://developer.themoviedb.org/reference/movie-external-ids
"""

from __future__ import annotations

import json
from logging import NullHandler, getLogger

from tminidb.base_api_endpoint import BaseEndpoint
from tminidb.exceptions import (
    InvalidFileError,
    MovieNotFoundError,
    ResourceNotFoundError,
)
from tminidb.movie.external_ids.models import MovieExternalIdsModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class MovieExternalIds(BaseEndpoint):
    """Get the external ids that have been added to a movie.

    Source: https://developer.themoviedb.org/reference/movie-external-ids
    """

    # TODO: Validate
    def __call__(self, movie_id: int) -> MovieExternalIdsModel:
        """Get the external ids that have been added to a movie.

        Source: https://developer.themoviedb.org/reference/movie-external-ids
        """
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(movie_id), log_id)

    # TODO: Validate
    def download(self, movie_id: int) -> str:
        """Download the movie external ids file.

        Raises:
            MovieNotFoundError: If no movie is under that id.
        """
        log_id = self.get_log_id(self.download, locals())
        try:
            response = self._client.download(
                f"movie/{movie_id}/external_ids",
                params={},
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

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> MovieExternalIdsModel:
        """Load a movie external ids file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)
