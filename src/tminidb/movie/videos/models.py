# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import MovieVideosModel as OptionalModel
from .strict_models import MovieVideosModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        MovieVideosModel,
        Result,
    )
else:
    from .optional_models import (
        MovieVideosModel,
        Result,
    )

__all__ = [
    "MovieVideosModel",
    "Result",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> MovieVideosModel:
    """Read a downloaded file into MovieVideosModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
