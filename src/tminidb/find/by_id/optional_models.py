from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import Field
from datetime import date
from pydantic import BaseModel, ConfigDict
from typing import Any


class MovieResult(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    adult: bool | Any = Field(default=None, union_mode="left_to_right")
    backdrop_path: str | Any = Field(default=None, union_mode="left_to_right")
    id: int | Any = Field(default=None, union_mode="left_to_right")
    title: str | Any = Field(default=None, union_mode="left_to_right")
    original_title: str | Any = Field(default=None, union_mode="left_to_right")
    overview: str | Any = Field(default=None, union_mode="left_to_right")
    poster_path: str | Any = Field(default=None, union_mode="left_to_right")
    media_type: str | Any = Field(default=None, union_mode="left_to_right")
    original_language: str | Any = Field(default=None, union_mode="left_to_right")
    genre_ids: list[int] | Any = Field(default=None, union_mode="left_to_right")
    popularity: float | Any = Field(default=None, union_mode="left_to_right")
    release_date: date | Any = Field(default=None, union_mode="left_to_right")
    softcore: bool | Any = Field(default=None, union_mode="left_to_right")
    video: bool | Any = Field(default=None, union_mode="left_to_right")
    vote_average: float | Any = Field(default=None, union_mode="left_to_right")
    vote_count: int | Any = Field(default=None, union_mode="left_to_right")


class KnownForItem(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    adult: bool | Any = Field(default=None, union_mode="left_to_right")
    backdrop_path: str | Any = Field(default=None, union_mode="left_to_right")
    id: int | Any = Field(default=None, union_mode="left_to_right")
    title: str | Any = Field(default=None, union_mode="left_to_right")
    original_title: str | Any = Field(default=None, union_mode="left_to_right")
    overview: str | Any = Field(default=None, union_mode="left_to_right")
    poster_path: str | Any = Field(default=None, union_mode="left_to_right")
    media_type: str | Any = Field(default=None, union_mode="left_to_right")
    original_language: str | Any = Field(default=None, union_mode="left_to_right")
    genre_ids: list[int] | Any = Field(default=None, union_mode="left_to_right")
    popularity: float | Any = Field(default=None, union_mode="left_to_right")
    release_date: date | Any = Field(default=None, union_mode="left_to_right")
    softcore: bool | Any = Field(default=None, union_mode="left_to_right")
    video: bool | Any = Field(default=None, union_mode="left_to_right")
    vote_average: float | Any = Field(default=None, union_mode="left_to_right")
    vote_count: int | Any = Field(default=None, union_mode="left_to_right")


class PersonResult(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    adult: bool | Any = Field(default=None, union_mode="left_to_right")
    id: int | Any = Field(default=None, union_mode="left_to_right")
    name: str | Any = Field(default=None, union_mode="left_to_right")
    original_name: str | Any = Field(default=None, union_mode="left_to_right")
    media_type: str | Any = Field(default=None, union_mode="left_to_right")
    popularity: float | Any = Field(default=None, union_mode="left_to_right")
    gender: int | Any = Field(default=None, union_mode="left_to_right")
    known_for_department: str | Any = Field(default=None, union_mode="left_to_right")
    profile_path: str | Any = Field(default=None, union_mode="left_to_right")
    known_for: list[KnownForItem] | Any = Field(
        default=None, union_mode="left_to_right"
    )


class TvResult(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    adult: bool | Any = Field(default=None, union_mode="left_to_right")
    backdrop_path: str | Any = Field(default=None, union_mode="left_to_right")
    id: int | Any = Field(default=None, union_mode="left_to_right")
    name: str | Any = Field(default=None, union_mode="left_to_right")
    original_name: str | Any = Field(default=None, union_mode="left_to_right")
    overview: str | Any = Field(default=None, union_mode="left_to_right")
    poster_path: str | Any = Field(default=None, union_mode="left_to_right")
    media_type: str | Any = Field(default=None, union_mode="left_to_right")
    original_language: str | Any = Field(default=None, union_mode="left_to_right")
    genre_ids: list[int] | Any = Field(default=None, union_mode="left_to_right")
    popularity: float | Any = Field(default=None, union_mode="left_to_right")
    first_air_date: date | Any = Field(default=None, union_mode="left_to_right")
    softcore: bool | Any = Field(default=None, union_mode="left_to_right")
    vote_average: float | Any = Field(default=None, union_mode="left_to_right")
    vote_count: int | Any = Field(default=None, union_mode="left_to_right")
    origin_country: list[str] | Any = Field(default=None, union_mode="left_to_right")


class TvEpisodeResult(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    id: int | Any = Field(default=None, union_mode="left_to_right")
    name: str | Any = Field(default=None, union_mode="left_to_right")
    overview: str | Any = Field(default=None, union_mode="left_to_right")
    media_type: str | Any = Field(default=None, union_mode="left_to_right")
    vote_average: float | Any = Field(default=None, union_mode="left_to_right")
    vote_count: int | Any = Field(default=None, union_mode="left_to_right")
    air_date: date | Any = Field(default=None, union_mode="left_to_right")
    episode_number: int | Any = Field(default=None, union_mode="left_to_right")
    episode_type: str | Any = Field(default=None, union_mode="left_to_right")
    production_code: str | Any = Field(default=None, union_mode="left_to_right")
    runtime: int | Any = Field(default=None, union_mode="left_to_right")
    season_number: int | Any = Field(default=None, union_mode="left_to_right")
    show_id: int | Any = Field(default=None, union_mode="left_to_right")
    still_path: str | Any = Field(default=None, union_mode="left_to_right")


class FindByIdModel(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    movie_results: list[MovieResult] | Any = Field(
        default=None, union_mode="left_to_right"
    )
    person_results: list[PersonResult] | Any = Field(
        default=None, union_mode="left_to_right"
    )
    tv_results: list[TvResult] | Any = Field(default=None, union_mode="left_to_right")
    tv_episode_results: list[TvEpisodeResult] | Any = Field(
        default=None, union_mode="left_to_right"
    )
    tv_season_results: list[Any] | Any = Field(default=None, union_mode="left_to_right")
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
