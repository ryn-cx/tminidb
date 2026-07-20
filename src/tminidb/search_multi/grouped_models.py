from datetime import date
from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import ConfigDict

class MovieItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    adult: bool
    backdrop_path: str | None
    id: int
    title: str
    original_title: str
    overview: str
    poster_path: str | None
    original_language: str
    genre_ids: list[int]
    popularity: float
    release_date: date
    softcore: bool
    video: bool
    vote_average: float
    vote_count: int

class TvItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    adult: bool
    backdrop_path: str
    id: int
    name: str
    original_name: str
    overview: str
    poster_path: str
    original_language: str
    genre_ids: list[int]
    popularity: float
    first_air_date: date
    softcore: bool
    vote_average: float
    vote_count: int
    origin_country: list[str]

class KnownForItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    adult: bool
    backdrop_path: str | None
    id: int
    title: str | None = None
    original_title: str | None = None
    overview: str
    poster_path: str | None
    media_type: str
    original_language: str
    genre_ids: list[int]
    popularity: float
    release_date: str | date | None = None
    softcore: bool
    video: bool | None = None
    vote_average: float
    vote_count: int
    name: str | None = None
    original_name: str | None = None
    first_air_date: date | None = None
    origin_country: list[str] | None = None

class PersonItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    adult: bool
    id: int
    name: str
    original_name: str
    popularity: float
    gender: int
    known_for_department: str
    profile_path: str | None
    known_for: list[KnownForItem]

class Results(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    movie: list[MovieItem]
    tv: list[TvItem]
    person: list[PersonItem]

class SearchMultiGroupedModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    page: int
    results: Results
    total_pages: int
    total_results: int
