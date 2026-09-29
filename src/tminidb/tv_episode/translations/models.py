# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import TvEpisodeTranslationsModel as OptionalModel
from .strict_models import TvEpisodeTranslationsModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        Data,
        Translation,
        TvEpisodeTranslationsModel,
    )
else:
    from .optional_models import (
        Data,
        Translation,
        TvEpisodeTranslationsModel,
    )

__all__ = [
    "Data",
    "Translation",
    "TvEpisodeTranslationsModel",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> TvEpisodeTranslationsModel:
    """Read a downloaded file into TvEpisodeTranslationsModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
