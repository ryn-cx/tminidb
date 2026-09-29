# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import MovieSimilarModel as OptionalModel
from .strict_models import MovieSimilarModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        MovieSimilarModel,
        Result,
    )
else:
    from .optional_models import (
        MovieSimilarModel,
        Result,
    )

__all__ = [
    "MovieSimilarModel",
    "Result",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> MovieSimilarModel:
    """Read a downloaded file into MovieSimilarModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
