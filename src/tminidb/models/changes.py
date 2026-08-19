from __future__ import annotations

from typing import Any, Self

from pydantic import BaseModel, ConfigDict, Field, SkipValidation


class Item(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: str
    action: str
    time: str
    iso_639_1: str
    iso_3166_1: str
    # TODO: Add complete type hints to these fields.
    value: Any = None
    original_value: Any = None


class Change(BaseModel):
    model_config = ConfigDict(frozen=True)

    key: str
    items: tuple[Item, ...]


class Changes(BaseModel):
    model_config = ConfigDict(frozen=True)

    changes: tuple[Change, ...]
    raw: SkipValidation[dict[str, Any]] = Field(repr=False)

    @classmethod
    def from_response(cls, data: dict[str, Any]) -> Self:
        return cls.model_validate({**data, "raw": data})
