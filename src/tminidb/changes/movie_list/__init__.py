# TODO: Validate
from __future__ import annotations

from logging import NullHandler, getLogger

from tminidb.base_changes_list import BaseChangesList
from tminidb.changes.movie_list.models import (
    ChangesMovieListModel,
    model_validate_json,
)

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class ChangesMovieList(BaseChangesList[ChangesMovieListModel]):
    MODEL = ChangesMovieListModel
    LOAD = staticmethod(model_validate_json)
    ENDPOINT = "movie/changes"
