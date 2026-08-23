from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, ConfigDict

class Poster(BaseModel):
    model_config = ConfigDict(extra='ignore')
    file_path: str | None = None
    iso_639_1: str | None = None
    iso_3166_1: str | None = None

class Value(BaseModel):
    model_config = ConfigDict(extra='ignore')
    episode_id: int | None = None
    episode_number: int | None = None
    poster: Poster | None = None

class OriginalValue(BaseModel):
    model_config = ConfigDict(extra='ignore')
    poster: Poster | None = None

class Item(BaseModel):
    model_config = ConfigDict(extra='ignore')
    id: str | None = None
    action: str | None = None
    time: str | None = None
    iso_639_1: str | None = None
    iso_3166_1: str | None = None
    value: str | Value | None = None
    original_value: str | OriginalValue | None = None

class Change(BaseModel):
    model_config = ConfigDict(extra='ignore')
    key: str | None = None
    items: list[Item] | None = None

class TvSeasonChangesModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    changes: list[Change] | None = None
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
