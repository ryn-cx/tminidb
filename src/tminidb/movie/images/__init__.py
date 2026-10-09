# TODO: Validate
"""Get the images that belong to a movie.

Source: https://developer.themoviedb.org/reference/movie-images
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
from tminidb.movie.images.models import MovieImagesModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class MovieImages(BaseEndpoint):
    """Get the images that belong to a movie.

    Querying images with a `language` parameter will filter the results. If you
    want to include a fallback language (especially useful for backdrops) you
    can use the `include_image_language` parameter. This should be a comma
    separated value like so: `include_image_language=en,null`.

    Source: https://developer.themoviedb.org/reference/movie-images
    """

    # TODO: Validate
    def __call__(
        self,
        movie_id: int,
        *,
        include_image_language: str | None = None,
        language: str | None = None,
    ) -> MovieImagesModel:
        """Get the images that belong to a movie.

        Source: https://developer.themoviedb.org/reference/movie-images
        """
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(
                movie_id,
                include_image_language=include_image_language,
                language=language,
            ),
            log_id,
        )

    # TODO: Validate
    def download(
        self,
        movie_id: int,
        *,
        include_image_language: str | None = None,
        language: str | None = None,
    ) -> str:
        """Download the movie images file.

        Raises:
            MovieNotFoundError: If no movie is under that id.
        """
        log_id = self.get_log_id(self.download, locals())
        try:
            response = self._client.download(
                f"movie/{movie_id}/images",
                params={
                    "include_image_language": include_image_language,
                    "language": language or self._client.language,
                },
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
    def load(self, data: str, log_id: str = "") -> MovieImagesModel:
        """Load a movie images file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)
