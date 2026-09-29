# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import TvSeriesRecommendationsModel as OptionalModel
from .strict_models import TvSeriesRecommendationsModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        Result,
        TvSeriesRecommendationsModel,
    )
else:
    from .optional_models import (
        Result,
        TvSeriesRecommendationsModel,
    )

__all__ = [
    "Result",
    "TvSeriesRecommendationsModel",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> TvSeriesRecommendationsModel:
    """Read a downloaded file into TvSeriesRecommendationsModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
