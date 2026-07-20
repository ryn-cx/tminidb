# TODO: Validate
"""Contains the MovieDetails class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any

from tminidb.base_api_endpoint import BaseEndpoint
from tminidb.movie_details.models import MovieDetailsModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class MovieDetails(BaseEndpoint[MovieDetailsModel]):
    """Manage the movie details file.

    Wraps `GET /movie/{movie_id}`:
    https://developer.themoviedb.org/reference/movie-details
    """

    _response_model = MovieDetailsModel

    def get_log_id(
        self,
        movie_id: int,
        *,
        append_to_response: str | None = None,
        language: str | None = None,
    ) -> str:
        """Build the log id for a download."""
        return self.append_non_default_args(
            f"{self.__class__.__name__} {movie_id=}",
            append_to_response=(append_to_response, None),
            language=(language, None),
        )

    def download(
        self,
        movie_id: int,
        *,
        append_to_response: str | None = None,
        language: str | None = None,
    ) -> dict[str, Any]:
        """Downloads the movie details file."""
        return self._client.download(
            f"movie/{movie_id}",
            {
                "append_to_response": append_to_response,
                "language": language or self._client.language,
            },
            log_id=self.get_log_id(
                movie_id,
                append_to_response=append_to_response,
                language=language,
            ),
        )

    def download_and_parse(
        self,
        movie_id: int,
        *,
        append_to_response: str | None = None,
        language: str | None = None,
    ) -> MovieDetailsModel:
        """Downloads and parses the movie details file."""
        return self.parse(
            self.download(
                movie_id,
                append_to_response=append_to_response,
                language=language,
            ),
        )
