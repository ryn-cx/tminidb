# TODO: Validate

from __future__ import annotations

from typing import Any, Self, override

from pydantic import BaseModel, ConfigDict, Field, SkipValidation

from tminidb.base_response_model import BaseResponseModel
from tminidb.models.common import Network

__all__ = ["EpisodeGroup", "Group", "GroupEpisode", "Network"]


# TODO: Validate
class GroupEpisode(BaseModel):
    model_config = ConfigDict(frozen=True)

    air_date: str | None
    episode_number: int
    # The documentation does not list it, though the response carries it and
    # the season and episode endpoints answer with it too.
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
    order: int


# TODO: Validate
class Group(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: str
    name: str
    order: int
    episodes: tuple[GroupEpisode, ...]
    locked: bool


# TODO: Validate
class EpisodeGroup(BaseResponseModel):
    model_config = ConfigDict(frozen=True)

    description: str
    episode_count: int
    group_count: int
    groups: tuple[Group, ...]
    id: str
    name: str
    network: Network | None
    type: int
    raw: SkipValidation[dict[str, Any]] = Field(repr=False)

    # TODO: Validate
    @classmethod
    @override
    def from_response(cls, data: dict[str, Any]) -> Self:
        return cls.model_validate({**data, "raw": data})
