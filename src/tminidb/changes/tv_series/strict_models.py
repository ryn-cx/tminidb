from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel

class Backdrop(BaseModel):
    file_path: str
    iso_639_1: str | None = None
    iso_3166_1: str | None = None

class Poster(BaseModel):
    file_path: str
    iso_639_1: str | None = None
    iso_3166_1: str | None = None

class TitleLogo(BaseModel):
    file_path: str
    iso_639_1: str | None = None
    iso_3166_1: str | None = None

class Value(BaseModel):
    primary: bool | None = None
    tagline: str | None = None
    id: int | str | None = None
    name: str | None = None
    key: str | None = None
    size: int | None = None
    site: str | None = None
    type: str | None = None
    add_to_every_season: bool | None = None
    character: str | None = None
    credit_id: str | None = None
    order: int | None = None
    person_id: int | None = None
    season_id: int | None = None
    group: str | None = None
    season_number: int | None = None
    backdrop: Backdrop | None = None
    poster: Poster | None = None
    title_logo: TitleLogo | None = None
    department: str | None = None
    job: str | None = None

class OriginalValue(BaseModel):
    id: int | str | None = None
    name: str | None = None
    key: str | None = None
    size: int | None = None
    site: str | None = None
    type: str | None = None
    add_to_every_season: bool | None = None
    character: str | None = None
    credit_id: str | None = None
    person_id: int | None = None
    season_id: int | None = None
    order: int | None = None
    group: str | None = None
    poster: Poster | None = None
    backdrop: Backdrop | None = None
    title_logo: TitleLogo | None = None
    department: str | None = None
    job: str | None = None

class Item(BaseModel):
    id: str
    action: str
    time: str
    iso_639_1: str
    iso_3166_1: str
    value: str | Value | None = None
    original_value: str | OriginalValue | None = None

class Change(BaseModel):
    key: str
    items: list[Item]

class TvSeriesChangesModel(BaseModel):
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
