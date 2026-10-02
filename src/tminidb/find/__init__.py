# TODO: Validate
"""Contains the FindEndpoints class."""

from __future__ import annotations

from typing import TYPE_CHECKING

from tminidb.find.by_id import FindById

if TYPE_CHECKING:
    from tminidb import TMiniDB


# TODO: Validate
class FindEndpoints:
    """The endpoints TMDB lists under Find.

    Source: https://developer.themoviedb.org/reference/find-by-id
    """

    # TODO: Validate
    def __init__(self, client: TMiniDB) -> None:
        """Build each endpoint under Find."""
        self.by_id = FindById(client)
