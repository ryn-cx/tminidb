# TODO: Validate

from __future__ import annotations

from typing import Any, Self, override

from pydantic import ConfigDict, Field, SkipValidation

from tminidb.base_response_model import BaseResponseModel
from tminidb.models.common import CrewMember, GuestStar

__all__ = ["CrewMember", "Details", "GuestStar"]


# TODO: Validate
class Details(BaseResponseModel):
    model_config = ConfigDict(frozen=True)

    air_date: str
    crew: tuple[CrewMember, ...]
    episode_number: int
    episode_type: str  # Not documented, but the API returns this field.
    guest_stars: tuple[GuestStar, ...]
    name: str
    overview: str
    id: int
    production_code: str
    runtime: int
    season_number: int
    still_path: str
    vote_average: float
    vote_count: int
    raw: SkipValidation[dict[str, Any]] = Field(repr=False)

    # TODO: Validate
    @classmethod
    @override
    def from_response(cls, data: dict[str, Any]) -> Self:
        return cls.model_validate({**data, "raw": data})
