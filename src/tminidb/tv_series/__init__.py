# TODO: Validate
"""Contains the TvSeriesEndpoints class."""

from __future__ import annotations

from typing import TYPE_CHECKING

from tminidb.tv_series.changes import TvSeriesChanges
from tminidb.tv_series.details import TvSeriesDetails
from tminidb.tv_series.episode_groups import TvSeriesEpisodeGroups
from tminidb.tv_series.watch_providers import TvWatchProviders

if TYPE_CHECKING:
    from tminidb import TMiniDB


# TODO: Validate
class TvSeriesEndpoints:
    """The endpoints the API's docs file under TV Series.

    [Official Documentation](https://developer.themoviedb.org/reference/tv-series-details)
    """

    # TODO: Validate
    def __init__(self, client: TMiniDB) -> None:
        """Build every endpoint in the group against the same client."""
        self.changes = TvSeriesChanges(client)
        self.details = TvSeriesDetails(client)
        self.episode_groups = TvSeriesEpisodeGroups(client)
        self.watch_providers = TvWatchProviders(client)
