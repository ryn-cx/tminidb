# TODO: Validate
"""Contains the MovieEndpoints class."""

from __future__ import annotations

from typing import TYPE_CHECKING

from tminidb.movies.changes import MovieChanges
from tminidb.movies.details import MovieDetails
from tminidb.movies.watch_providers import MovieWatchProviders

if TYPE_CHECKING:
    from tminidb import TMiniDB


# TODO: Validate
class MovieEndpoints:
    """The endpoints the API's docs file under Movies.

    [Official Documentation](https://developer.themoviedb.org/reference/movie-details)
    """

    # TODO: Validate
    def __init__(self, client: TMiniDB) -> None:
        """Build every endpoint in the group against the same client."""
        self.changes = MovieChanges(client)
        self.details = MovieDetails(client)
        self.watch_providers = MovieWatchProviders(client)
