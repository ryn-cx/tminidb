# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import ChangesTvListModel as OptionalModel
from .strict_models import ChangesTvListModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        ChangesTvListModel,
        Result,
    )
else:
    from .optional_models import (
        ChangesTvListModel,
        Result,
    )

__all__ = [
    "ChangesTvListModel",
    "Result",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> ChangesTvListModel:
    """Read a downloaded file into ChangesTvListModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
