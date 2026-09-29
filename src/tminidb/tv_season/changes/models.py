# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import TvSeasonChangesModel as OptionalModel
from .strict_models import TvSeasonChangesModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        Change,
        Item,
        OriginalValue,
        Poster,
        TvSeasonChangesModel,
        Value,
    )
else:
    from .optional_models import (
        Change,
        Item,
        OriginalValue,
        Poster,
        TvSeasonChangesModel,
        Value,
    )

__all__ = [
    "Change",
    "Item",
    "OriginalValue",
    "Poster",
    "TvSeasonChangesModel",
    "Value",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> TvSeasonChangesModel:
    """Read a downloaded file into TvSeasonChangesModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
