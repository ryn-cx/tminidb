# TODO: Validate
"""Contains the TMiniDB class."""

from __future__ import annotations

import time
from http import HTTPStatus
from logging import NullHandler, getLogger
from typing import Any

from get_around import GetAround

from tminidb.exceptions import HTTPError
from tminidb.movie_details import MovieDetails
from tminidb.movie_watch_providers import MovieWatchProviders
from tminidb.search_movie import SearchMovie
from tminidb.search_multi import SearchMulti
from tminidb.search_tv import SearchTv
from tminidb.tv_episode_details import TvEpisodeDetails
from tminidb.tv_episode_group_details import TvEpisodeGroupDetails
from tminidb.tv_episode_translations import TvEpisodeTranslations
from tminidb.tv_season_details import TvSeasonDetails
from tminidb.tv_series_details import TvSeriesDetails
from tminidb.tv_series_episode_groups import TvSeriesEpisodeGroups
from tminidb.tv_watch_providers import TvWatchProviders

logger = getLogger(__name__)
logger.addHandler(NullHandler())

API_DOMAIN = "api.themoviedb.org"
BASE_API_URL = f"https://{API_DOMAIN}/3"


class TMiniDB:
    """The Movie Database (TMDB) API wrapper."""

    def __init__(
        self,
        access_token: str,
        get_around_client: GetAround | None = None,
        language: str = "en-US",
    ) -> None:
        """Initialize the TMiniDB client.

        Args:
            access_token: TMDB API Read Access Token used as a bearer token.
                Reading it from a credential store is the caller's job.
            get_around_client: HTTP client to use. Defaults to a direct client.
            language: Default `ISO 639-1` language sent with every request.
            timeout: Request timeout in seconds.
        """
        self.access_token = access_token
        self.get_around_client = get_around_client or GetAround()
        self.language = language

        self.search_movie = SearchMovie(self)
        self.search_multi = SearchMulti(self)
        self.search_tv = SearchTv(self)
        self.movie_details = MovieDetails(self)
        self.movie_watch_providers = MovieWatchProviders(self)
        self.tv_series_details = TvSeriesDetails(self)
        self.tv_series_episode_groups = TvSeriesEpisodeGroups(self)
        self.tv_season_details = TvSeasonDetails(self)
        self.tv_episode_details = TvEpisodeDetails(self)
        self.tv_episode_group_details = TvEpisodeGroupDetails(self)
        self.tv_episode_translations = TvEpisodeTranslations(self)
        self.tv_watch_providers = TvWatchProviders(self)

    def download(
        self,
        endpoint: str,
        params: dict[str, Any],
        *,
        log_id: str,
    ) -> dict[str, Any]:
        """Downloads data from the API for a given endpoint.

        Parameters whose value is `None` are dropped so optional filters are
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
        )

        if response.status_code != HTTPStatus.OK:
            raise HTTPError(response.status_code, response.text)

        logger.debug("Downloaded %s (%.4f s)", log_id, time.monotonic() - start)
        return response.json()
