from datetime import date
from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import ConfigDict

class Result(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    adult: bool
    backdrop_path: str | None
    genre_ids: list[int]
    id: int
    title: str
    original_language: str
    original_title: str
    overview: str
    popularity: float
    poster_path: str | None
    release_date: str | date
    softcore: bool
    video: bool
    vote_average: float
    vote_count: int

class SearchMovieModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    page: int
    results: list[Result]
    total_pages: int
    total_results: int
