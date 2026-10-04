from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import BaseModel
from datetime import date

class Backdrop(BaseModel):
    model_config = ConfigDict(defer_build=True)
    file_path: str
    iso_639_1: str | None = None
    iso_3166_1: str | None = None

class Poster(BaseModel):
    model_config = ConfigDict(defer_build=True)
    file_path: str
    iso_639_1: str | None = None
    iso_3166_1: str | None = None

class TitleLogo(BaseModel):
    model_config = ConfigDict(defer_build=True)
    file_path: str
    iso_639_1: str | None = None
    iso_3166_1: str | None = None

class Value(BaseModel):
    model_config = ConfigDict(defer_build=True)
    name: str | None = None
    id: int | str | None = None
    key: str | None = None
    size: int | None = None
    site: str | None = None
    type: int | str | None = None
    person_id: int | None = None
    department: str | None = None
    job: str | None = None
    cast_id: int | None = None
    credit_id: str | None = None
    backdrop: Backdrop | None = None
    poster: Poster | None = None
    title_logo: TitleLogo | None = None
    primary: bool | None = None
    tagline: str | None = None
    character: str | None = None
    order: int | None = None
    group: str | None = None
    title: str | None = None
    iso_3166_1: str | None = None
    certification: str | None = None
    descriptors: list[str] | None = None
    iso_639_1: str | None = None
    note: str | None = None
    release_date: date | None = None

class OriginalValue(BaseModel):
    model_config = ConfigDict(defer_build=True)
    name: str | None = None
    id: int | str | None = None
    key: str | None = None
    size: int | None = None
    site: str | None = None
    type: int | str | None = None
    job: str | None = None
    department: str | None = None
    person_id: int | None = None
    cast_id: int | None = None
    credit_id: str | None = None
    backdrop: Backdrop | None = None
    poster: Poster | None = None
    title_logo: TitleLogo | None = None
    primary: bool | None = None
    tagline: str | None = None
    character: str | None = None
    order: int | None = None
    group: str | None = None
    title: str | None = None
    iso_3166_1: str | None = None
    certification: str | None = None
    descriptors: list[str] | None = None
    iso_639_1: str | None = None
    note: str | None = None
    release_date: date | None = None

class Item(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    action: str
    time: str
    iso_639_1: str
    iso_3166_1: str
    value: int | str | Value | list[str] | None = None
    original_value: int | str | OriginalValue | list[str] | None = None

class Change(BaseModel):
    model_config = ConfigDict(defer_build=True)
    key: str
    items: list[Item]

class MovieChangesModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    changes: list[Change]
    _raw_input: Any = PrivateAttr(default=None)

    @model_validator(mode='wrap')
    @classmethod
    def _capture_raw_input(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
        """Validate the model and keep the input it was built from."""
        model = handler(data)
        model._raw_input = data
        return model

    @property
    def raw_input(self) -> Any:
        """The input this model was validated from, as it was handed over."""
        return self._raw_input
