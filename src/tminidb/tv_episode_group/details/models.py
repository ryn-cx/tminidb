# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import TvEpisodeGroupDetailsModel as OptionalModel
from .strict_models import TvEpisodeGroupDetailsModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        Episode,
        Group,
        Network,
        TvEpisodeGroupDetailsModel,
    )
else:
    from .optional_models import (
        Episode,
        Group,
        Network,
        TvEpisodeGroupDetailsModel,
    )

__all__ = [
    "Episode",
    "Group",
    "Network",
    "TvEpisodeGroupDetailsModel",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> TvEpisodeGroupDetailsModel:
    """Read a downloaded file into TvEpisodeGroupDetailsModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
