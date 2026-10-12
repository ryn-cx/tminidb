# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import TvSeriesAlternativeTitlesModel as OptionalModel
from .strict_models import TvSeriesAlternativeTitlesModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        Result,
        TvSeriesAlternativeTitlesModel,
    )
else:
    from .optional_models import (
        Result,
        TvSeriesAlternativeTitlesModel,
    )

__all__ = [
    "Result",
    "TvSeriesAlternativeTitlesModel",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> TvSeriesAlternativeTitlesModel:
    """Read a downloaded file into TvSeriesAlternativeTitlesModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
