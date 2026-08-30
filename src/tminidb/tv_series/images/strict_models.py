from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import BaseModel

class Backdrop(BaseModel):
    model_config = ConfigDict(defer_build=True)
    aspect_ratio: float
    height: int
    iso_3166_1: str
    iso_639_1: str
    file_path: str
    vote_average: float
    vote_count: int
    width: int

class Logo(BaseModel):
    model_config = ConfigDict(defer_build=True)
    aspect_ratio: float
    height: int
    iso_3166_1: str
    iso_639_1: str
    file_path: str
    vote_average: float
    vote_count: int
    width: int

class Poster(BaseModel):
    model_config = ConfigDict(defer_build=True)
    aspect_ratio: float
    height: int
    iso_3166_1: str
    iso_639_1: str
    file_path: str
    vote_average: float
    vote_count: int
    width: int

class TvSeriesImagesModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    backdrops: list[Backdrop]
    id: int
    logos: list[Logo]
    posters: list[Poster]
    _raw_input: Any = PrivateAttr(default=None)

    @model_validator(mode='wrap')
    @classmethod
    def _capture_raw_input(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
        """Validate the model and keep the input it was built from."""
        model = handler(data)
        model._raw_input = data
        return model

    @property
    def raw_input(self) -> Any:
        """The input this model was validated from, as it was handed over."""
        return self._raw_input
