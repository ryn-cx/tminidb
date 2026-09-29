# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import MovieKeywordsModel as OptionalModel
from .strict_models import MovieKeywordsModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        Keyword,
        MovieKeywordsModel,
    )
else:
    from .optional_models import (
        Keyword,
        MovieKeywordsModel,
    )

__all__ = [
    "Keyword",
    "MovieKeywordsModel",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> MovieKeywordsModel:
    """Read a downloaded file into MovieKeywordsModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
