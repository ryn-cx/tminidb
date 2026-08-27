from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import BaseModel

class Poster(BaseModel):
    model_config = ConfigDict(defer_build=True)
    file_path: str
    iso_639_1: str | None = None
    iso_3166_1: str | None = None

class Value(BaseModel):
    model_config = ConfigDict(defer_build=True)
    episode_id: int | None = None
    episode_number: int | None = None
    poster: Poster | None = None

class Poster1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    file_path: str
    iso_639_1: str
    iso_3166_1: str

class OriginalValue(BaseModel):
    model_config = ConfigDict(defer_build=True)
    poster: Poster1

class Item(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    action: str
    time: str
    iso_639_1: str
    iso_3166_1: str
    value: str | Value
    original_value: str | OriginalValue | None = None

class Change(BaseModel):
    model_config = ConfigDict(defer_build=True)
    key: str
    items: list[Item]

class TvSeasonChangesModel(BaseModel):
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
