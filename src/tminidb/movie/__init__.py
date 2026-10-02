# TODO: Validate
"""Contains the MovieEndpoints class."""

from __future__ import annotations

from typing import TYPE_CHECKING

from tminidb.movie.changes import MovieChanges
from tminidb.movie.details import MovieDetails
from tminidb.movie.external_ids import MovieExternalIds
from tminidb.movie.keywords import MovieKeywords
from tminidb.movie.recommendations import MovieRecommendations
from tminidb.movie.similar import MovieSimilar
from tminidb.movie.translations import MovieTranslations
from tminidb.movie.watch_providers import MovieWatchProviders

if TYPE_CHECKING:
    from tminidb import TMiniDB


# TODO: Validate
class MovieEndpoints:
    """The endpoints TMDB lists under Movies.

    Source: https://developer.themoviedb.org/reference/movie-details
    """

    # TODO: Validate
    def __init__(self, client: TMiniDB) -> None:
        """Build each endpoint under Movies."""
        self.details = MovieDetails(client)
        self.changes = MovieChanges(client)
        self.watch_providers = MovieWatchProviders(client)
        self.translations = MovieTranslations(client)
        self.similar = MovieSimilar(client)
        self.recommendations = MovieRecommendations(client)
        self.keywords = MovieKeywords(client)
        self.external_ids = MovieExternalIds(client)
