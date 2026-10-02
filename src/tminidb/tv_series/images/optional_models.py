from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import Field
from pydantic import BaseModel, ConfigDict


class Backdrop(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    aspect_ratio: float | Any = Field(default=None, union_mode="left_to_right")
    height: int | Any = Field(default=None, union_mode="left_to_right")
    iso_3166_1: str | Any = Field(default=None, union_mode="left_to_right")
    iso_639_1: str | Any = Field(default=None, union_mode="left_to_right")
    file_path: str | Any = Field(default=None, union_mode="left_to_right")
    vote_average: float | Any = Field(default=None, union_mode="left_to_right")
    vote_count: int | Any = Field(default=None, union_mode="left_to_right")
    width: int | Any = Field(default=None, union_mode="left_to_right")


class Logo(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    aspect_ratio: float | Any = Field(default=None, union_mode="left_to_right")
    height: int | Any = Field(default=None, union_mode="left_to_right")
    iso_3166_1: str | Any = Field(default=None, union_mode="left_to_right")
    iso_639_1: str | Any = Field(default=None, union_mode="left_to_right")
    file_path: str | Any = Field(default=None, union_mode="left_to_right")
    vote_average: float | Any = Field(default=None, union_mode="left_to_right")
    vote_count: int | Any = Field(default=None, union_mode="left_to_right")
    width: int | Any = Field(default=None, union_mode="left_to_right")


class Poster(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    aspect_ratio: float | Any = Field(default=None, union_mode="left_to_right")
    height: int | Any = Field(default=None, union_mode="left_to_right")
    iso_3166_1: str | Any = Field(default=None, union_mode="left_to_right")
    iso_639_1: str | Any = Field(default=None, union_mode="left_to_right")
    file_path: str | Any = Field(default=None, union_mode="left_to_right")
    vote_average: float | Any = Field(default=None, union_mode="left_to_right")
    vote_count: int | Any = Field(default=None, union_mode="left_to_right")
    width: int | Any = Field(default=None, union_mode="left_to_right")


class TvSeriesImagesModel(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    backdrops: list[Backdrop] | Any = Field(default=None, union_mode="left_to_right")
    id: int | Any = Field(default=None, union_mode="left_to_right")
    logos: list[Logo] | Any = Field(default=None, union_mode="left_to_right")
    posters: list[Poster] | Any = Field(default=None, union_mode="left_to_right")
    _raw_input: Any = PrivateAttr(default=None)

    @model_validator(mode="wrap")
    @classmethod
    def _capture_raw_input(
        cls, data: Any, handler: ModelWrapValidatorHandler[Self]
    ) -> Self:
        """Validate the model and keep the input it was built from."""
        model = handler(data)
        model._raw_input = data
        return model

    @property
    def raw_input(self) -> Any:
        """The input this model was validated from, as it was handed over."""
        return self._raw_input
