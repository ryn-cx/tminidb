from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel

class OriginalValue(BaseModel):
    person_id: int
    character: str
    order: int
    credit_id: str

class Value(BaseModel):
    person_id: int
    character: str
    order: int
    credit_id: str

class Item(BaseModel):
    id: str
    action: str
    time: str
    iso_639_1: str
    iso_3166_1: str
    original_value: OriginalValue | None = None
    value: Value | None = None

class Change(BaseModel):
    key: str
    items: list[Item]

class TvEpisodeChangesModel(BaseModel):
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
