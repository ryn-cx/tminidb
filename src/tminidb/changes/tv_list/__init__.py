# TODO: Validate
from __future__ import annotations

from logging import NullHandler, getLogger

from tminidb.base_changes_list import BaseChangesList
from tminidb.changes.tv_list.models import (
    ChangesTvListModel,
    model_validate_json,
)

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class ChangesTvList(BaseChangesList[ChangesTvListModel]):
    MODEL = ChangesTvListModel
    LOAD = staticmethod(model_validate_json)
    ENDPOINT = "tv/changes"
