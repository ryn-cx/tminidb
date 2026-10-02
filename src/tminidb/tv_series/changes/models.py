# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import TvSeriesChangesModel as OptionalModel
from .strict_models import TvSeriesChangesModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        Backdrop,
        Change,
        Item,
        OriginalValue,
        Poster,
        TitleLogo,
        TvSeriesChangesModel,
        Value,
    )
else:
    from .optional_models import (
        Backdrop,
        Change,
        Item,
        OriginalValue,
        Poster,
        TitleLogo,
        TvSeriesChangesModel,
        Value,
    )

__all__ = [
    "Backdrop",
    "Change",
    "Item",
    "OriginalValue",
    "Poster",
    "TitleLogo",
    "TvSeriesChangesModel",
    "Value",
    "model_validate_json",
]


def model_validate_json(
    data: str | bytes | object, log_id: str
) -> TvSeriesChangesModel:
    """Read a downloaded file into TvSeriesChangesModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
