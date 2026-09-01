# TODO: Validate
"""Contains the TvSeriesEndpoints class."""

from __future__ import annotations

from typing import TYPE_CHECKING

from tminidb.tv_series.changes import TvSeriesChanges
from tminidb.tv_series.details import TvSeriesDetails
from tminidb.tv_series.episode_groups import TvSeriesEpisodeGroups
from tminidb.tv_series.images import TvSeriesImages
from tminidb.tv_series.translations import TvSeriesTranslations
from tminidb.tv_series.watch_providers import TvSeriesWatchProviders

if TYPE_CHECKING:
    from tminidb import TMiniDB


# TODO: Validate
class TvSeriesEndpoints:
    """The endpoints TMDB lists under TV Series.

    Source: https://developer.themoviedb.org/reference/tv-series-details
    """

    # TODO: Validate
    def __init__(self, client: TMiniDB) -> None:
        """Build each endpoint under TV Series."""
        self.details = TvSeriesDetails(client)
        self.changes = TvSeriesChanges(client)
        self.episode_groups = TvSeriesEpisodeGroups(client)
        self.images = TvSeriesImages(client)
        self.translations = TvSeriesTranslations(client)
        self.watch_providers = TvSeriesWatchProviders(client)
