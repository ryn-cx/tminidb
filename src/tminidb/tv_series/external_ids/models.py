# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import TvSeriesExternalIdsModel as OptionalModel
from .strict_models import TvSeriesExternalIdsModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        TvSeriesExternalIdsModel,
    )
else:
    from .optional_models import (
        TvSeriesExternalIdsModel,
    )

__all__ = [
    "TvSeriesExternalIdsModel",
    "model_validate_json",
]


def model_validate_json(
    data: str | bytes | object, log_id: str
) -> TvSeriesExternalIdsModel:
    """Read a downloaded file into TvSeriesExternalIdsModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
