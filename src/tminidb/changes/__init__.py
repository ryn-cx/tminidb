# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

from tminidb.changes.movie_list import ChangesMovieList
from tminidb.changes.tv_list import ChangesTvList

if TYPE_CHECKING:
    from tminidb import TMiniDB


# TODO: Validate
class ChangesEndpoints:
    # TODO: Validate
    def __init__(self, client: TMiniDB) -> None:
        self.movie_list = ChangesMovieList(client)
        self.tv_list = ChangesTvList(client)
