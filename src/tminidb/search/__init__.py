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
    """The endpoints the API's docs file under Search.

    [Official Documentation](https://developer.themoviedb.org/reference/search-movie)
    """

    # TODO: Validate
    def __init__(self, client: TMiniDB) -> None:
        """Build every endpoint in the group against the same client."""
        self.movie = SearchMovie(client)
        self.multi = SearchMulti(client)
        self.tv = SearchTv(client)
