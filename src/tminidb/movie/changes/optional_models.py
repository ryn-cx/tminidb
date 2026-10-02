from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import Field
from pydantic import BaseModel, ConfigDict
from datetime import date


class Backdrop(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    file_path: str | Any = Field(default=None, union_mode="left_to_right")
    iso_639_1: str | Any = Field(default=None, union_mode="left_to_right")
    iso_3166_1: str | Any = Field(default=None, union_mode="left_to_right")


class Poster(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    file_path: str | Any = Field(default=None, union_mode="left_to_right")
    iso_639_1: str | Any = Field(default=None, union_mode="left_to_right")
    iso_3166_1: str | Any = Field(default=None, union_mode="left_to_right")


class TitleLogo(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    file_path: str | Any = Field(default=None, union_mode="left_to_right")
    iso_639_1: str | Any = Field(default=None, union_mode="left_to_right")
    iso_3166_1: str | Any = Field(default=None, union_mode="left_to_right")


class Value(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    name: str | Any = Field(default=None, union_mode="left_to_right")
    id: int | str | Any = Field(default=None, union_mode="left_to_right")
    key: str | Any = Field(default=None, union_mode="left_to_right")
    size: int | Any = Field(default=None, union_mode="left_to_right")
    site: str | Any = Field(default=None, union_mode="left_to_right")
    type: int | str | Any = Field(default=None, union_mode="left_to_right")
    person_id: int | Any = Field(default=None, union_mode="left_to_right")
    department: str | Any = Field(default=None, union_mode="left_to_right")
    job: str | Any = Field(default=None, union_mode="left_to_right")
    cast_id: int | Any = Field(default=None, union_mode="left_to_right")
    credit_id: str | Any = Field(default=None, union_mode="left_to_right")
    backdrop: Backdrop | Any = Field(default=None, union_mode="left_to_right")
    poster: Poster | Any = Field(default=None, union_mode="left_to_right")
    title_logo: TitleLogo | Any = Field(default=None, union_mode="left_to_right")
    primary: bool | Any = Field(default=None, union_mode="left_to_right")
    tagline: str | Any = Field(default=None, union_mode="left_to_right")
    character: str | Any = Field(default=None, union_mode="left_to_right")
    order: int | Any = Field(default=None, union_mode="left_to_right")
    group: str | Any = Field(default=None, union_mode="left_to_right")
    title: str | Any = Field(default=None, union_mode="left_to_right")
    iso_3166_1: str | Any = Field(default=None, union_mode="left_to_right")
    certification: str | Any = Field(default=None, union_mode="left_to_right")
    descriptors: list[str] | Any = Field(default=None, union_mode="left_to_right")
    iso_639_1: str | Any = Field(default=None, union_mode="left_to_right")
    note: str | Any = Field(default=None, union_mode="left_to_right")
    release_date: date | Any = Field(default=None, union_mode="left_to_right")


class OriginalValue(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    name: str | Any = Field(default=None, union_mode="left_to_right")
    id: int | str | Any = Field(default=None, union_mode="left_to_right")
    key: str | Any = Field(default=None, union_mode="left_to_right")
    size: int | Any = Field(default=None, union_mode="left_to_right")
    site: str | Any = Field(default=None, union_mode="left_to_right")
    type: int | str | Any = Field(default=None, union_mode="left_to_right")
    job: str | Any = Field(default=None, union_mode="left_to_right")
    department: str | Any = Field(default=None, union_mode="left_to_right")
    person_id: int | Any = Field(default=None, union_mode="left_to_right")
    cast_id: int | Any = Field(default=None, union_mode="left_to_right")
    credit_id: str | Any = Field(default=None, union_mode="left_to_right")
    backdrop: Backdrop | Any = Field(default=None, union_mode="left_to_right")
    poster: Poster | Any = Field(default=None, union_mode="left_to_right")
    title_logo: TitleLogo | Any = Field(default=None, union_mode="left_to_right")
    primary: bool | Any = Field(default=None, union_mode="left_to_right")
    tagline: str | Any = Field(default=None, union_mode="left_to_right")
    character: str | Any = Field(default=None, union_mode="left_to_right")
    order: int | Any = Field(default=None, union_mode="left_to_right")
    group: str | Any = Field(default=None, union_mode="left_to_right")
    title: str | Any = Field(default=None, union_mode="left_to_right")
    iso_3166_1: str | Any = Field(default=None, union_mode="left_to_right")
    certification: str | Any = Field(default=None, union_mode="left_to_right")
    descriptors: list[str] | Any = Field(default=None, union_mode="left_to_right")
    iso_639_1: str | Any = Field(default=None, union_mode="left_to_right")
    note: str | Any = Field(default=None, union_mode="left_to_right")
    release_date: date | Any = Field(default=None, union_mode="left_to_right")


class Item(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    id: str | Any = Field(default=None, union_mode="left_to_right")
    action: str | Any = Field(default=None, union_mode="left_to_right")
    time: str | Any = Field(default=None, union_mode="left_to_right")
    iso_639_1: str | Any = Field(default=None, union_mode="left_to_right")
    iso_3166_1: str | Any = Field(default=None, union_mode="left_to_right")
    value: int | str | Value | list[str] | Any = Field(
        default=None, union_mode="left_to_right"
    )
    original_value: int | str | OriginalValue | list[str] | Any = Field(
        default=None, union_mode="left_to_right"
    )


class Change(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    key: str | Any = Field(default=None, union_mode="left_to_right")
    items: list[Item] | Any = Field(default=None, union_mode="left_to_right")


class MovieChangesModel(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    changes: list[Change] | Any = Field(default=None, union_mode="left_to_right")
    _raw_input: Any = PrivateAttr(default=None)

    @model_validator(mode="wrap")
    @classmethod
    def _capture_raw_input(
        cls, data: Any, handler: ModelWrapValidatorHandler[Self]
    ) -> Self:
        """Validate the model and keep the input it was built from."""
        model = handler(data)
        model._raw_input = data
        return model

    @property
    def raw_input(self) -> Any:
        """The input this model was validated from, as it was handed over."""
        return self._raw_input
