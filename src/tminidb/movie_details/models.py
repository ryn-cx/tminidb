# TODO: Validate
from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import ConfigDict
from datetime import date

class BelongsToCollection(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: int
    name: str
    poster_path: str
    backdrop_path: str

class Genre(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: int
    name: str

class ProductionCompany(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: int
    logo_path: str | None
    name: str
    origin_country: str

class ProductionCountry(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    iso_3166_1: str
    name: str

class SpokenLanguage(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    english_name: str
    iso_639_1: str
    name: str

class MovieDetailsModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    adult: bool
    backdrop_path: str
    belongs_to_collection: BelongsToCollection
    budget: int
    genres: list[Genre]
    homepage: str
    id: int
    imdb_id: str
    origin_country: list[str]
    original_language: str
    original_title: str
    overview: str
    popularity: float
    poster_path: str
    production_companies: list[ProductionCompany]
    production_countries: list[ProductionCountry]
    release_date: date
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
