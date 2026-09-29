# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import WatchProvidersTvListModel as OptionalModel
from .strict_models import WatchProvidersTvListModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        DisplayPriorities,
        Result,
        WatchProvidersTvListModel,
    )
else:
    from .optional_models import (
        DisplayPriorities,
        Result,
        WatchProvidersTvListModel,
    )

__all__ = [
    "DisplayPriorities",
    "Result",
    "WatchProvidersTvListModel",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> WatchProvidersTvListModel:
    """Read a downloaded file into WatchProvidersTvListModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
