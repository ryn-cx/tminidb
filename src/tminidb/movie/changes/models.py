# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import MovieChangesModel as OptionalModel
from .strict_models import MovieChangesModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        Backdrop,
        Change,
        Item,
        MovieChangesModel,
        OriginalValue,
        Poster,
        TitleLogo,
        Value,
    )
else:
    from .optional_models import (
        Backdrop,
        Change,
        Item,
        MovieChangesModel,
        OriginalValue,
        Poster,
        TitleLogo,
        Value,
    )

__all__ = [
    "Backdrop",
    "Change",
    "Item",
    "MovieChangesModel",
    "OriginalValue",
    "Poster",
    "TitleLogo",
    "Value",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> MovieChangesModel:
    """Read a downloaded file into MovieChangesModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
