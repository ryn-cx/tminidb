from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from datetime import date
from pydantic import BaseModel
from typing import Any

class MovieResult(BaseModel):
    model_config = ConfigDict(defer_build=True)
    adult: bool
    backdrop_path: str | None
    id: int
    title: str
    original_title: str
    overview: str
    poster_path: str
    media_type: str
    original_language: str
    genre_ids: list[int]
    popularity: float
    release_date: date
    softcore: bool
    video: bool
    vote_average: float
    vote_count: int

class KnownForItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    adult: bool
    backdrop_path: str
    id: int
    title: str
    original_title: str
    overview: str
    poster_path: str
    media_type: str
    original_language: str
    genre_ids: list[int]
    popularity: float
    release_date: date
    softcore: bool
    video: bool
    vote_average: float
    vote_count: int

class PersonResult(BaseModel):
    model_config = ConfigDict(defer_build=True)
    adult: bool
    id: int
    name: str
    original_name: str
    media_type: str
    popularity: float
    gender: int
    known_for_department: str
    profile_path: str
    known_for: list[KnownForItem]

class TvResult(BaseModel):
    model_config = ConfigDict(defer_build=True)
    adult: bool
    backdrop_path: str | None
    id: int
    name: str
    original_name: str
    overview: str
    poster_path: str
    media_type: str
    original_language: str
    genre_ids: list[int]
    popularity: float
    first_air_date: date
    softcore: bool
    vote_average: float
    vote_count: int
    origin_country: list[str]

class TvEpisodeResult(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: int
    name: str
    overview: str
    media_type: str
    vote_average: float
    vote_count: int
    air_date: date
    episode_number: int
    episode_type: str
    production_code: str
    runtime: int
    season_number: int
    show_id: int
    still_path: str | None

class FindByIdModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    movie_results: list[MovieResult]
    person_results: list[PersonResult]
    tv_results: list[TvResult]
    tv_episode_results: list[TvEpisodeResult]
    tv_season_results: list[None]
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
