# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import TvSeasonDetailsModel as OptionalModel
from .strict_models import TvSeasonDetailsModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        CrewItem,
        Episode,
        GuestStar,
        Network,
        TvSeasonDetailsModel,
    )
else:
    from .optional_models import (
        CrewItem,
        Episode,
        GuestStar,
        Network,
        TvSeasonDetailsModel,
    )

__all__ = [
    "CrewItem",
    "Episode",
    "GuestStar",
    "Network",
    "TvSeasonDetailsModel",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> TvSeasonDetailsModel:
    """Read a downloaded file into TvSeasonDetailsModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
