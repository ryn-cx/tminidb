# TODO: Validate
"""Contains the WatchProvidersEndpoints class."""

from __future__ import annotations

from typing import TYPE_CHECKING

from tminidb.watch_providers.movie_list import WatchProvidersMovieList
from tminidb.watch_providers.tv_list import WatchProvidersTvList

if TYPE_CHECKING:
    from tminidb import TMiniDB


# TODO: Validate
class WatchProvidersEndpoints:
    """The endpoints TMDB lists under Watch Providers.

    Source: https://developer.themoviedb.org/reference/watch-providers-movie-list
    """

    # TODO: Validate
    def __init__(self, client: TMiniDB) -> None:
        """Build each endpoint under Watch Providers."""
        self.movie_list = WatchProvidersMovieList(client)
        self.tv_list = WatchProvidersTvList(client)
