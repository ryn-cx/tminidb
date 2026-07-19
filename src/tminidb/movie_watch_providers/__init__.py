# TODO: Validate
"""Contains the MovieWatchProviders class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any

from tminidb.base_api_endpoint import BaseEndpoint
from tminidb.movie_watch_providers.models import MovieWatchProvidersModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class MovieWatchProviders(BaseEndpoint[MovieWatchProvidersModel]):
    """Manage the movie watch providers file.

    Wraps ``GET /movie/{movie_id}/watch/providers``:
    https://developer.themoviedb.org/reference/movie-watch-providers
    """

    _response_model = MovieWatchProvidersModel

    def get_log_id(self, movie_id: int) -> str:
        """Build the log id for a download."""
        return f"{self.__class__.__name__} {movie_id=}"

    def download(self, movie_id: int) -> dict[str, Any]:
        """Downloads the movie watch providers file."""
        return self._client.download(
            f"movie/{movie_id}/watch/providers",
            {},
            log_id=self.get_log_id(movie_id),
        )

    def download_and_parse(self, movie_id: int) -> MovieWatchProvidersModel:
        """Downloads and parses the movie watch providers file."""
        return self.parse(self.download(movie_id))
