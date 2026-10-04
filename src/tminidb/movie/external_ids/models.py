# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import MovieExternalIdsModel as OptionalModel
from .strict_models import MovieExternalIdsModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        MovieExternalIdsModel,
    )
else:
    from .optional_models import (
        MovieExternalIdsModel,
    )

__all__ = [
    "MovieExternalIdsModel",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> MovieExternalIdsModel:
    """Read a downloaded file into MovieExternalIdsModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
