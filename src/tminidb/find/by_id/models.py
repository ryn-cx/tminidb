# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import FindByIdModel as OptionalModel
from .strict_models import FindByIdModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        FindByIdModel,
        KnownForItem,
        MovieResult,
        PersonResult,
        TvEpisodeResult,
        TvResult,
    )
else:
    from .optional_models import (
        FindByIdModel,
        KnownForItem,
        MovieResult,
        PersonResult,
        TvEpisodeResult,
        TvResult,
    )

__all__ = [
    "FindByIdModel",
    "KnownForItem",
    "MovieResult",
    "PersonResult",
    "TvEpisodeResult",
    "TvResult",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> FindByIdModel:
    """Read a downloaded file into FindByIdModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
