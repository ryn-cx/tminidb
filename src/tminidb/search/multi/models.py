# TODO: Validate

from __future__ import annotations

from typing import Any, Self

from pydantic import BaseModel, ConfigDict, Field, SkipValidation


# TODO: Validate
class MultiResult(BaseModel):
    model_config = ConfigDict(frozen=True)

    adult: bool
    id: int
    media_type: str
    popularity: float
    # A result carries only the fields its own kind uses and leaves the rest
    # out entirely rather than leaving them empty, so every field that is not
    # common to all three kinds is defaulted here.
    backdrop_path: str | None = None
    title: str = ""
    original_language: str = ""
    original_title: str = ""
    overview: str = ""
    poster_path: str | None = None
    genre_ids: tuple[int, ...] = ()
    release_date: str = ""
    video: bool = False
    vote_average: float = 0.0
    vote_count: int = 0
    name: str = ""
    original_name: str = ""
    first_air_date: str = ""


# TODO: Validate
class MultiSearchResults(BaseModel):
    model_config = ConfigDict(frozen=True)

    page: int
    total_pages: int
    total_results: int
    results: tuple[MultiResult, ...]
    raw: SkipValidation[dict[str, Any]] = Field(repr=False)

    # TODO: Validate
    @classmethod
    def from_response(cls, data: dict[str, Any]) -> Self:
        return cls.model_validate({**data, "raw": data})
