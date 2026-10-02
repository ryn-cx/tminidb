from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import Field
from pydantic import BaseModel, ConfigDict
from datetime import date


class CreatedByItem(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    id: int | Any = Field(default=None, union_mode="left_to_right")
    credit_id: str | Any = Field(default=None, union_mode="left_to_right")
    name: str | Any = Field(default=None, union_mode="left_to_right")
    original_name: str | Any = Field(default=None, union_mode="left_to_right")
    gender: int | Any = Field(default=None, union_mode="left_to_right")
    profile_path: str | Any = Field(default=None, union_mode="left_to_right")


class Genre(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    id: int | Any = Field(default=None, union_mode="left_to_right")
    name: str | Any = Field(default=None, union_mode="left_to_right")


class LastEpisodeToAir(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    id: int | Any = Field(default=None, union_mode="left_to_right")
    name: str | Any = Field(default=None, union_mode="left_to_right")
    overview: str | Any = Field(default=None, union_mode="left_to_right")
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


class NextEpisodeToAir(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    id: int | Any = Field(default=None, union_mode="left_to_right")
    name: str | Any = Field(default=None, union_mode="left_to_right")
    overview: str | Any = Field(default=None, union_mode="left_to_right")
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


class Network(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    id: int | Any = Field(default=None, union_mode="left_to_right")
    logo_path: str | Any = Field(default=None, union_mode="left_to_right")
    name: str | Any = Field(default=None, union_mode="left_to_right")
    origin_country: str | Any = Field(default=None, union_mode="left_to_right")


class ProductionCompany(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    id: int | Any = Field(default=None, union_mode="left_to_right")
    logo_path: str | Any = Field(default=None, union_mode="left_to_right")
    name: str | Any = Field(default=None, union_mode="left_to_right")
    origin_country: str | Any = Field(default=None, union_mode="left_to_right")


class ProductionCountry(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    iso_3166_1: str | Any = Field(default=None, union_mode="left_to_right")
    name: str | Any = Field(default=None, union_mode="left_to_right")


class Season(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    air_date: date | Any = Field(default=None, union_mode="left_to_right")
    episode_count: int | Any = Field(default=None, union_mode="left_to_right")
    id: int | Any = Field(default=None, union_mode="left_to_right")
    name: str | Any = Field(default=None, union_mode="left_to_right")
    overview: str | Any = Field(default=None, union_mode="left_to_right")
    poster_path: str | Any = Field(default=None, union_mode="left_to_right")
    season_number: int | Any = Field(default=None, union_mode="left_to_right")
    vote_average: float | Any = Field(default=None, union_mode="left_to_right")


class SpokenLanguage(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    english_name: str | Any = Field(default=None, union_mode="left_to_right")
    iso_639_1: str | Any = Field(default=None, union_mode="left_to_right")
    name: str | Any = Field(default=None, union_mode="left_to_right")


class TvSeriesDetailsModel(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    adult: bool | Any = Field(default=None, union_mode="left_to_right")
    backdrop_path: str | Any = Field(default=None, union_mode="left_to_right")
    created_by: list[CreatedByItem] | Any = Field(
        default=None, union_mode="left_to_right"
    )
    episode_run_time: list[int] | Any = Field(default=None, union_mode="left_to_right")
    first_air_date: date | str | Any = Field(default=None, union_mode="left_to_right")
    genres: list[Genre] | Any = Field(default=None, union_mode="left_to_right")
    homepage: str | Any = Field(default=None, union_mode="left_to_right")
    id: int | Any = Field(default=None, union_mode="left_to_right")
    in_production: bool | Any = Field(default=None, union_mode="left_to_right")
    languages: list[str] | Any = Field(default=None, union_mode="left_to_right")
    last_air_date: date | Any = Field(default=None, union_mode="left_to_right")
    last_episode_to_air: LastEpisodeToAir | Any = Field(
        default=None, union_mode="left_to_right"
    )
    name: str | Any = Field(default=None, union_mode="left_to_right")
    next_episode_to_air: NextEpisodeToAir | Any = Field(
        default=None, union_mode="left_to_right"
    )
    networks: list[Network] | Any = Field(default=None, union_mode="left_to_right")
    number_of_episodes: int | Any = Field(default=None, union_mode="left_to_right")
    number_of_seasons: int | Any = Field(default=None, union_mode="left_to_right")
    origin_country: list[str] | Any = Field(default=None, union_mode="left_to_right")
    original_language: str | Any = Field(default=None, union_mode="left_to_right")
    original_name: str | Any = Field(default=None, union_mode="left_to_right")
    overview: str | Any = Field(default=None, union_mode="left_to_right")
    popularity: float | Any = Field(default=None, union_mode="left_to_right")
    poster_path: str | Any = Field(default=None, union_mode="left_to_right")
    production_companies: list[ProductionCompany] | Any = Field(
        default=None, union_mode="left_to_right"
    )
    production_countries: list[ProductionCountry] | Any = Field(
        default=None, union_mode="left_to_right"
    )
    seasons: list[Season] | Any = Field(default=None, union_mode="left_to_right")
    softcore: bool | Any = Field(default=None, union_mode="left_to_right")
    spoken_languages: list[SpokenLanguage] | Any = Field(
        default=None, union_mode="left_to_right"
    )
    status: str | Any = Field(default=None, union_mode="left_to_right")
    tagline: str | Any = Field(default=None, union_mode="left_to_right")
    type: str | Any = Field(default=None, union_mode="left_to_right")
    vote_average: float | Any = Field(default=None, union_mode="left_to_right")
    vote_count: int | Any = Field(default=None, union_mode="left_to_right")
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
