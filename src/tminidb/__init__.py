from __future__ import annotations

import time
from http import HTTPStatus
from logging import NullHandler, getLogger
from typing import Any

from get_around import GetAround

from tminidb.exceptions import HTTPError
from tminidb.movies import MovieEndpoints
from tminidb.search import SearchEndpoints
from tminidb.tv_episode_groups import TvEpisodeGroupEndpoints
from tminidb.tv_episodes import TvEpisodeEndpoints
from tminidb.tv_seasons import TvSeasonEndpoints
from tminidb.tv_series import TvSeriesEndpoints

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class TMiniDB:
    """Mini The Movie Database (TMDB) API wrapper."""

    # TODO: Validate
    def __init__(
        self,
        access_token: str,
        language: str = "en-US",
        get_around_client: GetAround | None = None,
    ) -> None:
        """Initialize the TMiniDB client.

        Args:
            access_token: TMDB API Read Access Token. Available at
                https://www.themoviedb.org/settings/api
            language: Default `ISO 639-1` language sent with every request. More
                information at https://developer.themoviedb.org/docs/languages
            get_around_client: Get Around client to route requests through.

        Raises:
            ValueError: If no access token is given. It is refused here rather
                than sent, because an empty one makes the header it goes out in
                `Bearer ` and a header ending in a space is not one that can be
                sent at all: the request would fail somewhere below this with
                nothing to say the token was what was missing.
        """
        if not access_token.strip():
            msg = "An access token is required."
            raise ValueError(msg)

        self.access_token = access_token
        self.language = language
        self.get_around_client = get_around_client or GetAround()

        self.search = SearchEndpoints(self)
        self.movies = MovieEndpoints(self)
        self.tv_series = TvSeriesEndpoints(self)
        self.tv_seasons = TvSeasonEndpoints(self)
        self.tv_episodes = TvEpisodeEndpoints(self)
        self.tv_episode_groups = TvEpisodeGroupEndpoints(self)

    # TODO: Validate
    def download(
        self,
        endpoint: str,
        params: dict[str, Any],
        log_id: str,
    ) -> dict[str, Any]:
        """Download the response from TMDB.

        Args:
            endpoint: The API endpoint to download data from.
            params: The query parameters to send with the request.
            log_id: A unique identifier for the request.

        Raises:
            HTTPError: If the request is answered with anything but a 200.
        """
        start = time.monotonic()
        response = self.get_around_client.get(
            f"https://api.themoviedb.org/3/{endpoint}",
            params={key: value for key, value in params.items() if value is not None},
            headers={
                "accept": "application/json",
                "Authorization": f"Bearer {self.access_token}",
            },
        )

        if response.status_code != HTTPStatus.OK:
            raise HTTPError(response)

        duration = time.monotonic() - start
        logger.debug("Downloaded: %s - Completed in %.4f seconds", log_id, duration)

        return response.json()
