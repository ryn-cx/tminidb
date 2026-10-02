# TODO: Validate
"""Get the videos that belong to a movie.

Source: https://developer.themoviedb.org/reference/movie-videos
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
from tminidb.movie.videos.models import MovieVideosModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class MovieVideos(BaseEndpoint):
    """Get the videos that belong to a movie.

    Querying videos with a `language` parameter will filter the results. If you
    want to include a fallback language you can use the `include_video_language`
    parameter. This should be a comma separated value like so:
    `include_video_language=en,null`.

    Source: https://developer.themoviedb.org/reference/movie-videos
    """

    # TODO: Validate
    def __call__(
        self,
        movie_id: int,
        *,
        include_video_language: str | None = None,
        language: str | None = None,
    ) -> MovieVideosModel:
        """Get the videos that belong to a movie.

        Source: https://developer.themoviedb.org/reference/movie-videos
        """
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(
                movie_id,
                include_video_language=include_video_language,
                language=language,
            ),
            log_id,
        )

    # TODO: Validate
    def download(
        self,
        movie_id: int,
        *,
        include_video_language: str | None = None,
        language: str | None = None,
    ) -> str:
        """Download the movie videos file.

        Raises:
            MovieNotFoundError: If no movie is under that id.
        """
        log_id = self.get_log_id(self.download, locals())
        try:
            response = self._client.download(
                f"movie/{movie_id}/videos",
                params={
                    "include_video_language": include_video_language,
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
    def load(self, data: str, log_id: str = "") -> MovieVideosModel:
        """Load a movie videos file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)
