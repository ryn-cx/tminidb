from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import Field
from pydantic import ConfigDict
from pydantic import BaseModel
from datetime import date

class CreatedByItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: int
    credit_id: str
    name: str
    original_name: str
    gender: int
    profile_path: str | None

class Genre(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: int
    name: str

class LastEpisodeToAir(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: int
    name: str
    overview: str
    vote_average: float
    vote_count: int
    air_date: date
    episode_number: int
    episode_type: str
    production_code: str
    runtime: int | None
    season_number: int
    show_id: int
    still_path: str | None

class NextEpisodeToAir(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: int
    name: str
    overview: str
    vote_average: float
    vote_count: int
    air_date: date
    episode_number: int
    episode_type: str
    production_code: str
    runtime: int | None
    season_number: int
    show_id: int
    still_path: None

class Network(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: int
    logo_path: str | None
    name: str
    origin_country: str

class ProductionCompany(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: int
    logo_path: str | None
    name: str
    origin_country: str

class ProductionCountry(BaseModel):
    model_config = ConfigDict(defer_build=True)
    iso_3166_1: str
    name: str

class Season(BaseModel):
    model_config = ConfigDict(defer_build=True)
    air_date: date | None
    episode_count: int
    id: int
    name: str
    overview: str
    poster_path: str | None
    season_number: int
    vote_average: float

class SpokenLanguage(BaseModel):
    model_config = ConfigDict(defer_build=True)
    english_name: str
    iso_639_1: str
    name: str

class TvSeriesDetailsModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    adult: bool
    backdrop_path: str | None
    created_by: list[CreatedByItem]
    episode_run_time: list[int]
    first_air_date: date | str = Field(union_mode='left_to_right')
    genres: list[Genre]
    homepage: str
    id: int
    in_production: bool
    languages: list[str]
    last_air_date: date
    last_episode_to_air: LastEpisodeToAir
    name: str
    next_episode_to_air: NextEpisodeToAir | None
    networks: list[Network]
    number_of_episodes: int
    number_of_seasons: int
    origin_country: list[str]
    original_language: str
    original_name: str
    overview: str
    popularity: float
    poster_path: str
    production_companies: list[ProductionCompany]
    production_countries: list[ProductionCountry]
    seasons: list[Season]
    softcore: bool
    spoken_languages: list[SpokenLanguage]
    status: str
    tagline: str
    type: str
    vote_average: float
    vote_count: int
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
