# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import SearchMovieModel as OptionalModel
from .strict_models import SearchMovieModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        Result,
        SearchMovieModel,
    )
else:
    from .optional_models import (
        Result,
        SearchMovieModel,
    )

__all__ = [
    "Result",
    "SearchMovieModel",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> SearchMovieModel:
    """Read a downloaded file into SearchMovieModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
