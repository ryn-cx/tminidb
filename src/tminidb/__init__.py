# TODO: Validate
"""Contains the Tminidb class."""

from __future__ import annotations

import time
from http import HTTPStatus
from logging import NullHandler, getLogger
from typing import Any

from get_around import GetAround, get_credential

from tminidb.exceptions import HTTPError
from tminidb.movie_details import MovieDetails
from tminidb.search_movie import SearchMovie
from tminidb.search_tv import SearchTv
from tminidb.tv_episode_details import TvEpisodeDetails
from tminidb.tv_season_details import TvSeasonDetails
from tminidb.tv_series_details import TvSeriesDetails

logger = getLogger(__name__)
logger.addHandler(NullHandler())

API_DOMAIN = "api.themoviedb.org"
BASE_API_URL = f"https://{API_DOMAIN}/3"
ACCESS_TOKEN_CREDENTIAL = "TMDB_ACCESS_TOKEN"  # noqa: S105


class Tminidb:
    """The Movie Database (TMDB) API wrapper."""

    def __init__(
        self,
        access_token: str | None = None,
        get_around_client: GetAround | None = None,
        language: str = "en-US",
        timeout: int = 30,
    ) -> None:
        """Initialize the Tminidb client.

        Args:
            access_token: TMDB API Read Access Token used as a bearer token. When
                omitted, it is loaded lazily from the ``TMDB_ACCESS_TOKEN``
                credential the first time a request is made.
            get_around_client: HTTP client to use. Defaults to a direct client.
            language: Default ``ISO 639-1`` language sent with every request.
            timeout: Request timeout in seconds.
        """
        self._access_token_value = access_token
        self.get_around_client = get_around_client or GetAround()
        self.language = language
        self.timeout = timeout

        self.search_movie = SearchMovie(self)
        self.search_tv = SearchTv(self)
        self.movie_details = MovieDetails(self)
        self.tv_series_details = TvSeriesDetails(self)
        self.tv_season_details = TvSeasonDetails(self)
        self.tv_episode_details = TvEpisodeDetails(self)

    @property
    def access_token(self) -> str:
        """The bearer token, loaded from the credential store on first use."""
        if not self._access_token_value:
            self._access_token_value = get_credential(ACCESS_TOKEN_CREDENTIAL)
        return self._access_token_value

    def download(
        self,
        endpoint: str,
        params: dict[str, Any],
        *,
        log_id: str,
    ) -> dict[str, Any]:
        """Downloads data from the API for a given endpoint.

        Parameters whose value is ``None`` are dropped so optional filters are
        only sent when explicitly provided.
        """
        url = f"{BASE_API_URL}/{endpoint}"
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.access_token}",
        }

        logger.debug("Downloading: %s", log_id)
        start = time.monotonic()
        response = self.get_around_client.get(
            url,
            params={key: value for key, value in params.items() if value is not None},
            headers=headers,
            timeout=self.timeout,
        )

        if response.status_code != HTTPStatus.OK:
            msg = f"Unexpected response status code: {response.status_code}"
            raise HTTPError(msg)

        logger.debug("Downloaded %s (%.4f s)", log_id, time.monotonic() - start)
        return response.json()
