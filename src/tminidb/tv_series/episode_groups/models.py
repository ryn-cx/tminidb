# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import TvSeriesEpisodeGroupsModel as OptionalModel
from .strict_models import TvSeriesEpisodeGroupsModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        Network,
        Result,
        TvSeriesEpisodeGroupsModel,
    )
else:
    from .optional_models import (
        Network,
        Result,
        TvSeriesEpisodeGroupsModel,
    )

__all__ = [
    "Network",
    "Result",
    "TvSeriesEpisodeGroupsModel",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> TvSeriesEpisodeGroupsModel:
    """Read a downloaded file into TvSeriesEpisodeGroupsModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
