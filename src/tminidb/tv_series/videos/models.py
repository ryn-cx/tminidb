# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import TvSeriesVideosModel as OptionalModel
from .strict_models import TvSeriesVideosModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        Result,
        TvSeriesVideosModel,
    )
else:
    from .optional_models import (
        Result,
        TvSeriesVideosModel,
    )

__all__ = [
    "Result",
    "TvSeriesVideosModel",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> TvSeriesVideosModel:
    """Read a downloaded file into TvSeriesVideosModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
