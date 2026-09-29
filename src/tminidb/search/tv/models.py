# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import SearchTvModel as OptionalModel
from .strict_models import SearchTvModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        Result,
        SearchTvModel,
    )
else:
    from .optional_models import (
        Result,
        SearchTvModel,
    )

__all__ = [
    "Result",
    "SearchTvModel",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> SearchTvModel:
    """Read a downloaded file into SearchTvModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
