from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import Field
from pydantic import BaseModel, ConfigDict

class OriginalValue(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    person_id: int | Any = Field(default=None, union_mode='left_to_right')
    character: str | Any = Field(default=None, union_mode='left_to_right')
    order: int | Any = Field(default=None, union_mode='left_to_right')
    credit_id: str | Any = Field(default=None, union_mode='left_to_right')

class Value(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    person_id: int | Any = Field(default=None, union_mode='left_to_right')
    character: str | Any = Field(default=None, union_mode='left_to_right')
    order: int | Any = Field(default=None, union_mode='left_to_right')
    credit_id: str | Any = Field(default=None, union_mode='left_to_right')

class Item(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    action: str | Any = Field(default=None, union_mode='left_to_right')
    time: str | Any = Field(default=None, union_mode='left_to_right')
    iso_639_1: str | Any = Field(default=None, union_mode='left_to_right')
    iso_3166_1: str | Any = Field(default=None, union_mode='left_to_right')
    original_value: OriginalValue | Any = Field(default=None, union_mode='left_to_right')
    value: Value | Any = Field(default=None, union_mode='left_to_right')

class Change(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    key: str | Any = Field(default=None, union_mode='left_to_right')
    items: list[Item] | Any = Field(default=None, union_mode='left_to_right')

class TvEpisodeChangesModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    changes: list[Change] | Any = Field(default=None, union_mode='left_to_right')
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
