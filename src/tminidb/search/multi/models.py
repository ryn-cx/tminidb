# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import SearchMultiModel as OptionalModel
from .strict_models import SearchMultiModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        KnownForItem,
        Result,
        SearchMultiModel,
    )
else:
    from .optional_models import (
        KnownForItem,
        Result,
        SearchMultiModel,
    )

__all__ = [
    "KnownForItem",
    "Result",
    "SearchMultiModel",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> SearchMultiModel:
    """Read a downloaded file into SearchMultiModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
