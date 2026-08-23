# TODO: Validate
"""Contains the TMiniDB class."""

from __future__ import annotations

import json
import time
from http import HTTPStatus
from logging import NullHandler, getLogger
from typing import Any

from get_around import GetAround

from tminidb.changes.movie import MovieChanges
from tminidb.changes.tv_episode import TvEpisodeChanges
from tminidb.changes.tv_season import TvSeasonChanges
from tminidb.changes.tv_series import TvSeriesChanges
from tminidb.details.movie import Movie
from tminidb.details.tv_episode import TvEpisode
from tminidb.details.tv_season import TvSeason
from tminidb.details.tv_series import TvSeries
from tminidb.exceptions import HTTPError, ResourceNotFoundError
from tminidb.search.movie import SearchMovie
from tminidb.search.multi import SearchMulti
from tminidb.search.tv import SearchTv
from tminidb.tv_episode_group import TvEpisodeGroup
from tminidb.tv_episode_translations import TvEpisodeTranslations
from tminidb.tv_series_episode_groups import TvSeriesEpisodeGroups
from tminidb.watch_providers.movie import MovieWatchProviders
from tminidb.watch_providers.tv_series import TvSeriesWatchProviders

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

        The client holds one attribute per endpoint, so `client.movie(603)` looks
        a movie up and `client.movie.download(603)` and `client.movie.load(data)`
        are the halves of it.

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

        self.movie = Movie(self)
        self.tv_series = TvSeries(self)
        self.tv_season = TvSeason(self)
        self.tv_episode = TvEpisode(self)
        self.tv_episode_group = TvEpisodeGroup(self)
        self.tv_episode_translations = TvEpisodeTranslations(self)
        self.tv_series_episode_groups = TvSeriesEpisodeGroups(self)
        self.movie_changes = MovieChanges(self)
        self.tv_series_changes = TvSeriesChanges(self)
        self.tv_season_changes = TvSeasonChanges(self)
        self.tv_episode_changes = TvEpisodeChanges(self)
        self.movie_watch_providers = MovieWatchProviders(self)
        self.tv_series_watch_providers = TvSeriesWatchProviders(self)
        self.search_movie = SearchMovie(self)
        self.search_multi = SearchMulti(self)
        self.search_tv = SearchTv(self)

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
