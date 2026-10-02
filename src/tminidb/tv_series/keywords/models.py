# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import TvSeriesKeywordsModel as OptionalModel
from .strict_models import TvSeriesKeywordsModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        Result,
        TvSeriesKeywordsModel,
    )
else:
    from .optional_models import (
        Result,
        TvSeriesKeywordsModel,
    )

__all__ = [
    "Result",
    "TvSeriesKeywordsModel",
    "model_validate_json",
]


def model_validate_json(
    data: str | bytes | object, log_id: str
) -> TvSeriesKeywordsModel:
    """Read a downloaded file into TvSeriesKeywordsModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
