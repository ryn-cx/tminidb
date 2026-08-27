# TODO: Validate
"""Contains the SearchEndpoints class."""

from __future__ import annotations

from typing import TYPE_CHECKING

from tminidb.search.movie import SearchMovie
from tminidb.search.multi import SearchMulti
from tminidb.search.tv import SearchTv

if TYPE_CHECKING:
    from tminidb import TMiniDB


# TODO: Validate
class SearchEndpoints:
    """The endpoints TMDB lists under Search.

    Source: https://developer.themoviedb.org/reference/search-movie
    """

    # TODO: Validate
    def __init__(self, client: TMiniDB) -> None:
        """Build each endpoint under Search."""
        self.movie = SearchMovie(client)
        self.multi = SearchMulti(client)
        self.tv = SearchTv(client)
