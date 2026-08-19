# TODO: Validate

from __future__ import annotations

from typing import Any, Self

from pydantic import BaseModel, ConfigDict, Field, SkipValidation

from tminidb.models.common import CrewMember, GuestStar

__all__ = ["CrewMember", "Episode", "GuestStar", "TvSeason"]


# TODO: Validate
class Episode(BaseModel):
    model_config = ConfigDict(frozen=True)

    air_date: str | None
    episode_number: int
    episode_type: str
    id: int
    name: str
    overview: str
    production_code: str
    runtime: int | None
    season_number: int
    show_id: int
    still_path: str | None
    vote_average: float
    vote_count: int
    crew: tuple[CrewMember, ...]
    guest_stars: tuple[GuestStar, ...]


# TODO: Validate
class TvSeason(BaseModel):
    model_config = ConfigDict(frozen=True, populate_by_name=True)

    object_id: str = Field(validation_alias="_id")
    air_date: str | None
    episodes: tuple[Episode, ...]
    name: str
    overview: str
    # The documentation lists `_id` but not this, though the response carries
    # both and this is the one the rest of the API is asked with.
    id: int
    poster_path: str | None
    season_number: int
    vote_average: float
    raw: SkipValidation[dict[str, Any]] = Field(repr=False)

    # TODO: Validate
    @classmethod
    def from_response(cls, data: dict[str, Any]) -> Self:
        return cls.model_validate({**data, "raw": data})
