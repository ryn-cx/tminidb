from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, ConfigDict

class Backdrop(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    aspect_ratio: float | None = None
    height: int | None = None
    iso_3166_1: str | None = None
    iso_639_1: str | None = None
    file_path: str | None = None
    vote_average: float | None = None
    vote_count: int | None = None
    width: int | None = None

class Logo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    aspect_ratio: float | None = None
    height: int | None = None
    iso_3166_1: str | None = None
    iso_639_1: str | None = None
    file_path: str | None = None
    vote_average: float | None = None
    vote_count: int | None = None
    width: int | None = None

class Poster(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    aspect_ratio: float | None = None
    height: int | None = None
    iso_3166_1: str | None = None
    iso_639_1: str | None = None
    file_path: str | None = None
    vote_average: float | None = None
    vote_count: int | None = None
    width: int | None = None

class TvSeriesImagesModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    backdrops: list[Backdrop] | None = None
    id: int | None = None
    logos: list[Logo] | None = None
    posters: list[Poster] | None = None
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
