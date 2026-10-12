# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import MovieAlternativeTitlesModel as OptionalModel
from .strict_models import MovieAlternativeTitlesModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        MovieAlternativeTitlesModel,
        Title,
    )
else:
    from .optional_models import (
        MovieAlternativeTitlesModel,
        Title,
    )

__all__ = [
    "MovieAlternativeTitlesModel",
    "Title",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> MovieAlternativeTitlesModel:
    """Read a downloaded file into MovieAlternativeTitlesModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
