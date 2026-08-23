from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import Field
from pydantic import BaseModel, ConfigDict
from typing import Any
from datetime import date

class BelongsToCollection(BaseModel):
    model_config = ConfigDict(extra='ignore')
    id: int | None = None
    name: str | None = None
    poster_path: str | None = None
    backdrop_path: str | None = None

class Genre(BaseModel):
    model_config = ConfigDict(extra='ignore')
    id: int | None = None
    name: str | None = None

class ProductionCompany(BaseModel):
    model_config = ConfigDict(extra='ignore')
    id: int | None = None
    logo_path: str | None = None
    name: str | None = None
    origin_country: str | None = None

class ProductionCountry(BaseModel):
    model_config = ConfigDict(extra='ignore')
    iso_3166_1: str | None = None
    name: str | None = None

class SpokenLanguage(BaseModel):
    model_config = ConfigDict(extra='ignore')
    english_name: str | None = None
    iso_639_1: str | None = None
    name: str | None = None

class MovieModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    adult: bool | None = None
    backdrop_path: str | None = None
    belongs_to_collection: Any | BelongsToCollection | None = None
    budget: int | None = None
    genres: list[Genre] | None = None
    homepage: str | None = None
    id: int | None = None
    imdb_id: str | None = None
    origin_country: list[str] | None = None
    original_language: str | None = None
    original_title: str | None = None
    overview: str | None = None
    popularity: float | None = None
    poster_path: str | None = None
    production_companies: list[ProductionCompany] | None = None
    production_countries: list[ProductionCountry] | None = None
    release_date: date | str | None = Field(default=None, union_mode='left_to_right')
    revenue: int | None = None
    runtime: int | None = None
    softcore: bool | None = None
    spoken_languages: list[SpokenLanguage] | None = None
    status: str | None = None
    tagline: str | None = None
    title: str | None = None
    video: bool | None = None
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
