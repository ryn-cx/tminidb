# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import TvSeriesDetailsModel as OptionalModel
from .strict_models import TvSeriesDetailsModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        CreatedByItem,
        Genre,
        LastEpisodeToAir,
        Network,
        NextEpisodeToAir,
        ProductionCompany,
        ProductionCountry,
        Season,
        SpokenLanguage,
        TvSeriesDetailsModel,
    )
else:
    from .optional_models import (
        CreatedByItem,
        Genre,
        LastEpisodeToAir,
        Network,
        NextEpisodeToAir,
        ProductionCompany,
        ProductionCountry,
        Season,
        SpokenLanguage,
        TvSeriesDetailsModel,
    )

__all__ = [
    "CreatedByItem",
    "Genre",
    "LastEpisodeToAir",
    "Network",
    "NextEpisodeToAir",
    "ProductionCompany",
    "ProductionCountry",
    "Season",
    "SpokenLanguage",
    "TvSeriesDetailsModel",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> TvSeriesDetailsModel:
    """Read a downloaded file into TvSeriesDetailsModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
