from pydantic import Field
from datetime import date
from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import ConfigDict

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
    release_date: date | str | None = Field(default=None, union_mode='left_to_right')
    softcore: bool
    video: bool | None = None
    vote_average: float
    vote_count: int
    name: str | None = None
    original_name: str | None = None
    first_air_date: date | None = None
    origin_country: list[str] | None = None

class Result(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    adult: bool
    id: int
    name: str | None = None
    original_name: str | None = None
    media_type: str
    popularity: float
    gender: int | None = None
    known_for_department: str | None = None
    profile_path: str | None = None
    known_for: list[KnownForItem] | None = None
    backdrop_path: str | None = None
    title: str | None = None
    original_title: str | None = None
    overview: str | None = None
    poster_path: str | None = None
    original_language: str | None = None
    genre_ids: list[int] | None = None
    release_date: date | None = None
    softcore: bool | None = None
    video: bool | None = None
    vote_average: float | None = None
    vote_count: int | None = None
    first_air_date: date | None = None
    origin_country: list[str] | None = None

class SearchMultiModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    page: int
    results: list[Result]
    total_pages: int
    total_results: int
