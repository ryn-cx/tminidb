from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import Field
from datetime import date
from pydantic import BaseModel, ConfigDict

class Result(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    adult: bool | Any = Field(default=None, union_mode='left_to_right')
    backdrop_path: str | Any = Field(default=None, union_mode='left_to_right')
    id: int | Any = Field(default=None, union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    original_name: str | Any = Field(default=None, union_mode='left_to_right')
    overview: str | Any = Field(default=None, union_mode='left_to_right')
    poster_path: str | Any = Field(default=None, union_mode='left_to_right')
    media_type: str | Any = Field(default=None, union_mode='left_to_right')
    original_language: str | Any = Field(default=None, union_mode='left_to_right')
    genre_ids: list[int] | Any = Field(default=None, union_mode='left_to_right')
    popularity: float | Any = Field(default=None, union_mode='left_to_right')
    first_air_date: date | Any = Field(default=None, union_mode='left_to_right')
    softcore: bool | Any = Field(default=None, union_mode='left_to_right')
    vote_average: float | Any = Field(default=None, union_mode='left_to_right')
    vote_count: int | Any = Field(default=None, union_mode='left_to_right')
    origin_country: list[str] | Any = Field(default=None, union_mode='left_to_right')

class TvSeriesRecommendationsModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    page: int | Any = Field(default=None, union_mode='left_to_right')
    results: list[Result] | Any = Field(default=None, union_mode='left_to_right')
    total_pages: int | Any = Field(default=None, union_mode='left_to_right')
    total_results: int | Any = Field(default=None, union_mode='left_to_right')
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
