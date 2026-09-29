# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import TvEpisodeChangesModel as OptionalModel
from .strict_models import TvEpisodeChangesModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        Change,
        Item,
        OriginalValue,
        TvEpisodeChangesModel,
        Value,
    )
else:
    from .optional_models import (
        Change,
        Item,
        OriginalValue,
        TvEpisodeChangesModel,
        Value,
    )

__all__ = [
    "Change",
    "Item",
    "OriginalValue",
    "TvEpisodeChangesModel",
    "Value",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> TvEpisodeChangesModel:
    """Read a downloaded file into TvEpisodeChangesModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
