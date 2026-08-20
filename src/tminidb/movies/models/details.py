# TODO: Validate

from __future__ import annotations

from typing import Any, Self, override

from pydantic import BaseModel, ConfigDict, Field, SkipValidation

from tminidb.base_response_model import BaseResponseModel
from tminidb.models.common import (
    Genre,
    ProductionCompany,
    ProductionCountry,
    SpokenLanguage,
)

__all__ = [
    "Collection",
    "Genre",
    "Movie",
    "ProductionCompany",
    "ProductionCountry",
    "SpokenLanguage",
]


# TODO: Validate
class Collection(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: int
    name: str
    poster_path: str | None
    backdrop_path: str | None


# TODO: Validate
class Movie(BaseResponseModel):
    model_config = ConfigDict(frozen=True)

    adult: bool
    backdrop_path: str | None
    belongs_to_collection: Collection | None
    budget: int
    genres: tuple[Genre, ...]
    homepage: str
    id: int
    imdb_id: str | None
    origin_country: tuple[str, ...]
    original_language: str
    original_title: str
    overview: str
    popularity: float
    poster_path: str | None
    production_companies: tuple[ProductionCompany, ...]
    production_countries: tuple[ProductionCountry, ...]
    release_date: str
    revenue: int
    runtime: int | None
    spoken_languages: tuple[SpokenLanguage, ...]
    status: str
    tagline: str
    title: str
    video: bool
    vote_average: float
    vote_count: int
    raw: SkipValidation[dict[str, Any]] = Field(repr=False)

    # TODO: Validate
    @classmethod
    @override
    def from_response(cls, data: dict[str, Any]) -> Self:
        return cls.model_validate({**data, "raw": data})
