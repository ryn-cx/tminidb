# TODO: Validate

from __future__ import annotations

from typing import Any, Self

from pydantic import BaseModel, ConfigDict, Field, SkipValidation

from tminidb.models.common import Network

__all__ = ["EpisodeGroupSummary", "EpisodeGroups", "Network"]


# TODO: Validate
class EpisodeGroupSummary(BaseModel):
    model_config = ConfigDict(frozen=True)

    description: str
    episode_count: int
    group_count: int
    id: str
    name: str
    network: Network | None
    type: int


# TODO: Validate
class EpisodeGroups(BaseModel):
    model_config = ConfigDict(frozen=True)

    results: tuple[EpisodeGroupSummary, ...]
    id: int
    raw: SkipValidation[dict[str, Any]] = Field(repr=False)

    # TODO: Validate
    @classmethod
    def from_response(cls, data: dict[str, Any]) -> Self:
        return cls.model_validate({**data, "raw": data})
