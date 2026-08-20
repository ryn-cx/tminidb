# TODO: Validate

from __future__ import annotations

from typing import Any, Self, override

from pydantic import BaseModel, ConfigDict, Field, SkipValidation

from tminidb.base_response_model import BaseResponseModel
from tminidb.models.common import (
    Genre,
    Network,
    ProductionCompany,
    ProductionCountry,
    SpokenLanguage,
)

__all__ = [
    "Creator",
    "EpisodeSummary",
    "Genre",
    "Network",
    "ProductionCompany",
    "ProductionCountry",
    "Season",
    "SpokenLanguage",
    "TvSeries",
]


# TODO: Validate
class Creator(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: int
    credit_id: str
    name: str
    gender: int
    profile_path: str | None


# TODO: Validate
class EpisodeSummary(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: int
    name: str
    overview: str
    vote_average: float
    vote_count: int
    air_date: str | None
    episode_number: int
    production_code: str
    runtime: int | None
    season_number: int
    show_id: int
    still_path: str | None


# TODO: Validate
class Season(BaseModel):
    model_config = ConfigDict(frozen=True)

    air_date: str | None
    episode_count: int
    id: int
    name: str
    overview: str
    poster_path: str | None
    season_number: int
    vote_average: float


# TODO: Validate
class TvSeries(BaseResponseModel):
    model_config = ConfigDict(frozen=True)

    adult: bool
    backdrop_path: str | None
    created_by: tuple[Creator, ...]
    episode_run_time: tuple[int, ...]
    first_air_date: str | None
    genres: tuple[Genre, ...]
    homepage: str
    id: int
    in_production: bool
    languages: tuple[str, ...]
    last_air_date: str | None
    last_episode_to_air: EpisodeSummary | None
    name: str
    next_episode_to_air: EpisodeSummary | None
    networks: tuple[Network, ...]
    number_of_episodes: int
    number_of_seasons: int
    origin_country: tuple[str, ...]
    original_language: str
    original_name: str
    overview: str
    popularity: float
    poster_path: str | None
    production_companies: tuple[ProductionCompany, ...]
    production_countries: tuple[ProductionCountry, ...]
    seasons: tuple[Season, ...]
    spoken_languages: tuple[SpokenLanguage, ...]
    status: str
    tagline: str
    type: str
    vote_average: float
    vote_count: int
    raw: SkipValidation[dict[str, Any]] = Field(repr=False)

    # TODO: Validate
    @classmethod
    @override
    def from_response(cls, data: dict[str, Any]) -> Self:
        return cls.model_validate({**data, "raw": data})
