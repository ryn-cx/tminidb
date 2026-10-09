# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import MovieImagesModel as OptionalModel
from .strict_models import MovieImagesModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        Backdrop,
        Logo,
        MovieImagesModel,
        Poster,
    )
else:
    from .optional_models import (
        Backdrop,
        Logo,
        MovieImagesModel,
        Poster,
    )

__all__ = [
    "Backdrop",
    "Logo",
    "MovieImagesModel",
    "Poster",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> MovieImagesModel:
    """Read a downloaded file into MovieImagesModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
