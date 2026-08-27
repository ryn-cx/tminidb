# TODO: Validate
"""Contains the TvSeasonEndpoints class."""

from __future__ import annotations

from typing import TYPE_CHECKING

from tminidb.tv_season.changes import TvSeasonChanges
from tminidb.tv_season.details import TvSeasonDetails

if TYPE_CHECKING:
    from tminidb import TMiniDB


# TODO: Validate
class TvSeasonEndpoints:
    """The endpoints TMDB lists under TV Seasons.

    Source: https://developer.themoviedb.org/reference/tv-season-details
    """

    # TODO: Validate
    def __init__(self, client: TMiniDB) -> None:
        """Build each endpoint under TV Seasons."""
        self.details = TvSeasonDetails(client)
        self.changes = TvSeasonChanges(client)
