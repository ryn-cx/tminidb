from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import Field
from pydantic import BaseModel
from datetime import date

class BelongsToCollection(BaseModel):
    id: int
    name: str
    poster_path: str
    backdrop_path: str

class Genre(BaseModel):
    id: int
    name: str

class ProductionCompany(BaseModel):
    id: int
    logo_path: str | None
    name: str
    origin_country: str

class ProductionCountry(BaseModel):
    iso_3166_1: str
    name: str

class SpokenLanguage(BaseModel):
    english_name: str
    iso_639_1: str
    name: str

class MovieModel(BaseModel):
    adult: bool
    backdrop_path: str | None
    belongs_to_collection: BelongsToCollection | None
    budget: int
    genres: list[Genre]
    homepage: str
    id: int
    imdb_id: str | None
    origin_country: list[str]
    original_language: str
    original_title: str
    overview: str
    popularity: float
    poster_path: str
    production_companies: list[ProductionCompany]
    production_countries: list[ProductionCountry]
    release_date: date | str = Field(union_mode='left_to_right')
    revenue: int
    runtime: int
    softcore: bool
    spoken_languages: list[SpokenLanguage]
    status: str
    tagline: str
    title: str
    video: bool
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
