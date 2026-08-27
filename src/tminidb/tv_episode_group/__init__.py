# TODO: Validate
"""Contains the TvEpisodeGroupEndpoints class."""

from __future__ import annotations

from typing import TYPE_CHECKING

from tminidb.tv_episode_group.details import TvEpisodeGroupDetails

if TYPE_CHECKING:
    from tminidb import TMiniDB


# TODO: Validate
class TvEpisodeGroupEndpoints:
    """The endpoints TMDB lists under TV Episode Groups.

    Source: https://developer.themoviedb.org/reference/tv-episode-group-details
    """

    # TODO: Validate
    def __init__(self, client: TMiniDB) -> None:
        """Build each endpoint under TV Episode Groups."""
        self.details = TvEpisodeGroupDetails(client)
