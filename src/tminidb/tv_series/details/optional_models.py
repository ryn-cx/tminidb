from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Any

class CreatedByItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: int | None = None
    credit_id: str | None = None
    name: str | None = None
    original_name: str | None = None
    gender: int | None = None
    profile_path: str | None = None

class Genre(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: int | None = None
    name: str | None = None

class LastEpisodeToAir(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: int | None = None
    name: str | None = None
    overview: str | None = None
    vote_average: float | None = None
    vote_count: int | None = None
    air_date: date | None = None
    episode_number: int | None = None
    episode_type: str | None = None
    production_code: str | None = None
    runtime: int | None = None
    season_number: int | None = None
    show_id: int | None = None
    still_path: str | None = None

class Network(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: int | None = None
    logo_path: str | None = None
    name: str | None = None
    origin_country: str | None = None

class ProductionCompany(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: int | None = None
    logo_path: str | None = None
    name: str | None = None
    origin_country: str | None = None

class ProductionCountry(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    iso_3166_1: str | None = None
    name: str | None = None

class Season(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    air_date: Any | date | None = None
    episode_count: int | None = None
    id: int | None = None
    name: str | None = None
    overview: str | None = None
    poster_path: str | None = None
    season_number: int | None = None
    vote_average: float | None = None

class SpokenLanguage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    english_name: str | None = None
    iso_639_1: str | None = None
    name: str | None = None

class TvSeriesDetailsModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    adult: bool | None = None
    backdrop_path: str | None = None
    created_by: list[CreatedByItem] | None = None
    episode_run_time: list[int] | None = None
    first_air_date: date | None = None
    genres: list[Genre] | None = None
    homepage: str | None = None
    id: int | None = None
    in_production: bool | None = None
    languages: list[str] | None = None
    last_air_date: date | None = None
    last_episode_to_air: LastEpisodeToAir | None = None
    name: str | None = None
    next_episode_to_air: Any | None = None
    networks: list[Network] | None = None
    number_of_episodes: int | None = None
    number_of_seasons: int | None = None
    origin_country: list[str] | None = None
    original_language: str | None = None
    original_name: str | None = None
    overview: str | None = None
    popularity: float | None = None
    poster_path: str | None = None
    production_companies: list[ProductionCompany] | None = None
    production_countries: list[ProductionCountry] | None = None
    seasons: list[Season] | None = None
    softcore: bool | None = None
    spoken_languages: list[SpokenLanguage] | None = None
    status: str | None = None
    tagline: str | None = None
    type: str | None = None
    vote_average: float | None = None
    vote_count: int | None = None
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
