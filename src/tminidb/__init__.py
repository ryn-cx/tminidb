# TODO: Validate
"""Contains the TMiniDB class."""

from __future__ import annotations

import json
import time
from http import HTTPStatus
from logging import NullHandler, getLogger
from typing import Any

from get_around import GetAround

from tminidb.exceptions import HTTPError, ResourceNotFoundError
from tminidb.movie import MovieEndpoints
from tminidb.search import SearchEndpoints
from tminidb.tv_episode import TvEpisodeEndpoints
from tminidb.tv_episode_group import TvEpisodeGroupEndpoints
from tminidb.tv_season import TvSeasonEndpoints
from tminidb.tv_series import TvSeriesEndpoints

logger = getLogger(__name__)
logger.addHandler(NullHandler())

API_DOMAIN = "api.themoviedb.org"

RESOURCE_NOT_FOUND_CODE = 34
"""The status code TMDB puts in the body when nothing is under the id it was given."""


# TODO: Validate
class TMiniDB:
    """Mini The Movie Database (TMDB) API wrapper."""

    # TODO: Validate
    def __init__(
        self,
        access_token: str,
        get_around_client: GetAround | None = None,
        language: str = "en-US",
    ) -> None:
        """Initialize the TMiniDB client.

        The client holds one attribute per category TMDB lists its endpoints
        under, and each of those holds one attribute per endpoint, so
        `client.movie.details(603)` looks a movie up, and
        `client.movie.details.download(603)` and
        `client.movie.details.load(data)` are the halves of it.

        Args:
            access_token: TMDB API Read Access Token. Available at
                https://www.themoviedb.org/settings/api
            get_around_client: Get Around client to route requests through.
            language: Default `ISO 639-1` language sent with every request. More
                information at https://developer.themoviedb.org/docs/languages

        Raises:
            ValueError: If no access token is given.
        """
        if not access_token.strip():
            msg = "An access token is required."
            raise ValueError(msg)

        self.access_token = access_token
        self.language = language
        self.get_around_client = get_around_client or GetAround()

        self.movie = MovieEndpoints(self)
        self.tv_series = TvSeriesEndpoints(self)
        self.tv_season = TvSeasonEndpoints(self)
        self.tv_episode = TvEpisodeEndpoints(self)
        self.tv_episode_group = TvEpisodeGroupEndpoints(self)
        self.search = SearchEndpoints(self)

    # TODO: Validate
    def download(
        self,
        endpoint: str,
        params: dict[str, Any],
        log_id: str,
        headers: dict[str, str] | None = None,
    ) -> str:
        """Download from the API and return the body as text.

        Args:
            endpoint: The path under the API root to download.
            params: The query parameters to send. A parameter set to None is
                left out.
            log_id: What the request is called in the log.
            headers: Extra headers to send alongside the authorization.

        Raises:
            ResourceNotFoundError: If TMDB says nothing is under what was asked
                for.
            HTTPError: If the request is answered with anything but a 200.
        """
        request_headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.access_token}",
            **(headers or {}),
        }

        logger.debug("Downloading: %s", log_id)
        url = f"https://{API_DOMAIN}/3/{endpoint}"
        start = time.monotonic()
        response = self.get_around_client.get(
            url,
            params={key: value for key, value in params.items() if value is not None},
            headers=request_headers,
        )

        if response.status_code != HTTPStatus.OK:
            try:
                code = json.loads(response.text).get("status_code")
            except ValueError, AttributeError:
                code = None
            if code == RESOURCE_NOT_FOUND_CODE:
                raise ResourceNotFoundError(response.status_code, response.text)
            raise HTTPError(response.status_code, response.text)

        logger.debug("Downloaded %s (%.4f s)", log_id, time.monotonic() - start)
        return response.text
