from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import Field
from pydantic import ConfigDict
from datetime import date
from pydantic import BaseModel

class KnownForItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    adult: bool
    backdrop_path: str | None
    id: int
    title: str | None = None
    original_title: str | None = None
    overview: str
    poster_path: str | None
    media_type: str
    original_language: str
    genre_ids: list[int]
    popularity: float
    release_date: date | str | None = Field(default=None, union_mode='left_to_right')
    softcore: bool
    video: bool | None = None
    vote_average: float
    vote_count: int
    name: str | None = None
    original_name: str | None = None
    first_air_date: date | None = None
    origin_country: list[str] | None = None

class Result(BaseModel):
    model_config = ConfigDict(defer_build=True)
    adult: bool
    backdrop_path: str | None = None
    id: int
    title: str | None = None
    original_title: str | None = None
    overview: str | None = None
    poster_path: str | None = None
    media_type: str
    original_language: str | None = None
    genre_ids: list[int] | None = None
    popularity: float
    release_date: date | str | None = Field(default=None, union_mode='left_to_right')
    softcore: bool | None = None
    video: bool | None = None
    vote_average: float | None = None
    vote_count: int | None = None
    name: str | None = None
    original_name: str | None = None
    gender: int | None = None
    known_for_department: str | None = None
    profile_path: str | None = None
    known_for: list[KnownForItem] | None = None
    first_air_date: date | str | None = Field(default=None, union_mode='left_to_right')
    origin_country: list[str] | None = None

class SearchMultiModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    page: int
    results: list[Result]
    total_pages: int
    total_results: int
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
