# TODO: Validate
"""Contains the TvEpisodeEndpoints class."""

from __future__ import annotations

from typing import TYPE_CHECKING

from tminidb.tv_episodes.changes import TvEpisodeChanges
from tminidb.tv_episodes.details import TvEpisodeDetails
from tminidb.tv_episodes.translations import TvEpisodeTranslations

if TYPE_CHECKING:
    from tminidb import TMiniDB


# TODO: Validate
class TvEpisodeEndpoints:
    """The endpoints the API's docs file under TV Episodes.

    [Official Documentation](https://developer.themoviedb.org/reference/tv-episode-details)
    """

    # TODO: Validate
    def __init__(self, client: TMiniDB) -> None:
        """Build every endpoint in the group against the same client."""
        self.changes = TvEpisodeChanges(client)
        self.details = TvEpisodeDetails(client)
        self.translations = TvEpisodeTranslations(client)
