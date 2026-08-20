# TODO: Validate

from __future__ import annotations

from typing import Any, Self, override

from pydantic import BaseModel, ConfigDict, Field, SkipValidation

from tminidb.base_response_model import BaseResponseModel


# TODO: Validate
class Data(BaseModel):
    model_config = ConfigDict(frozen=True)

    name: str
    overview: str


# TODO: Validate
class Translation(BaseModel):
    model_config = ConfigDict(frozen=True)

    iso_3166_1: str
    iso_639_1: str
    name: str
    english_name: str
    data: Data


# TODO: Validate
class Translations(BaseResponseModel):
    model_config = ConfigDict(frozen=True)

    id: int
    translations: tuple[Translation, ...]
    raw: SkipValidation[dict[str, Any]] = Field(repr=False)

    # TODO: Validate
    @classmethod
    @override
    def from_response(cls, data: dict[str, Any]) -> Self:
        return cls.model_validate({**data, "raw": data})
