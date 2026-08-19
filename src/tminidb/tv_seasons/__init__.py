# TODO: Validate
"""Contains the TvSeasonEndpoints class."""

from __future__ import annotations

from typing import TYPE_CHECKING

from tminidb.tv_seasons.changes import TvSeasonChanges
from tminidb.tv_seasons.details import TvSeasonDetails

if TYPE_CHECKING:
    from tminidb import TMiniDB


# TODO: Validate
class TvSeasonEndpoints:
    """The endpoints the API's docs file under TV Seasons.

    [Official Documentation](https://developer.themoviedb.org/reference/tv-season-details)
    """

    # TODO: Validate
    def __init__(self, client: TMiniDB) -> None:
        """Build every endpoint in the group against the same client."""
        self.changes = TvSeasonChanges(client)
        self.details = TvSeasonDetails(client)
