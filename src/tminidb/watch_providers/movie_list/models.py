# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import WatchProvidersMovieListModel as OptionalModel
from .strict_models import WatchProvidersMovieListModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        DisplayPriorities,
        Result,
        WatchProvidersMovieListModel,
    )
else:
    from .optional_models import (
        DisplayPriorities,
        Result,
        WatchProvidersMovieListModel,
    )

__all__ = [
    "DisplayPriorities",
    "Result",
    "WatchProvidersMovieListModel",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> WatchProvidersMovieListModel:
    """Read a downloaded file into WatchProvidersMovieListModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
