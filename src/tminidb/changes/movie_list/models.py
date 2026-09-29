# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import ChangesMovieListModel as OptionalModel
from .strict_models import ChangesMovieListModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        ChangesMovieListModel,
        Result,
    )
else:
    from .optional_models import (
        ChangesMovieListModel,
        Result,
    )

__all__ = [
    "ChangesMovieListModel",
    "Result",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> ChangesMovieListModel:
    """Read a downloaded file into ChangesMovieListModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
