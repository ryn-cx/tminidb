# TODO: Validate
"""Contains the TvEpisodeEndpoints class."""

from __future__ import annotations

from typing import TYPE_CHECKING

from tminidb.tv_episode.changes import TvEpisodeChanges
from tminidb.tv_episode.details import TvEpisodeDetails
from tminidb.tv_episode.translations import TvEpisodeTranslations

if TYPE_CHECKING:
    from tminidb import TMiniDB


# TODO: Validate
class TvEpisodeEndpoints:
    """The endpoints TMDB lists under TV Episodes.

    Source: https://developer.themoviedb.org/reference/tv-episode-details
    """

    # TODO: Validate
    def __init__(self, client: TMiniDB) -> None:
        """Build each endpoint under TV Episodes."""
        self.details = TvEpisodeDetails(client)
        self.changes = TvEpisodeChanges(client)
        self.translations = TvEpisodeTranslations(client)
