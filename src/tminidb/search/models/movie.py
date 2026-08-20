# TODO: Validate

from __future__ import annotations

from typing import Any, Self, override

from pydantic import BaseModel, ConfigDict, Field, SkipValidation

from tminidb.base_response_model import BaseResponseModel


# TODO: Validate
class MovieResult(BaseModel):
    model_config = ConfigDict(frozen=True)

    adult: bool
    backdrop_path: str | None
    genre_ids: tuple[int, ...]
    id: int
    original_language: str
    original_title: str
    overview: str
    popularity: float
    poster_path: str | None
    # A movie with no known release date has the field left out entirely rather
    # than left empty.
    release_date: str = ""
    title: str
    video: bool
    vote_average: float
    vote_count: int


# TODO: Validate
class MovieSearchResults(BaseResponseModel):
    model_config = ConfigDict(frozen=True)

    page: int
    total_pages: int
    total_results: int
    results: tuple[MovieResult, ...]
    raw: SkipValidation[dict[str, Any]] = Field(repr=False)

    # TODO: Validate
    @classmethod
    @override
    def from_response(cls, data: dict[str, Any]) -> Self:
        return cls.model_validate({**data, "raw": data})
