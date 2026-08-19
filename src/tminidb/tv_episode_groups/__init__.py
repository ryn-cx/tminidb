# TODO: Validate
"""Contains the TvEpisodeGroupEndpoints class."""

from __future__ import annotations

from typing import TYPE_CHECKING

from tminidb.tv_episode_groups.details import TvEpisodeGroupDetails

if TYPE_CHECKING:
    from tminidb import TMiniDB


# TODO: Validate
class TvEpisodeGroupEndpoints:
    """The endpoints the API's docs file under TV Episode Groups.

    [Official Documentation](https://developer.themoviedb.org/reference/tv-episode-group-details)
    """

    # TODO: Validate
    def __init__(self, client: TMiniDB) -> None:
        """Build every endpoint in the group against the same client."""
        self.details = TvEpisodeGroupDetails(client)
