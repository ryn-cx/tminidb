from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import Field
from pydantic import BaseModel, ConfigDict

class Data(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | Any = Field(default=None, union_mode='left_to_right')
    overview: str | Any = Field(default=None, union_mode='left_to_right')

class Translation(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    iso_3166_1: str | Any = Field(default=None, union_mode='left_to_right')
    iso_639_1: str | Any = Field(default=None, union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    english_name: str | Any = Field(default=None, union_mode='left_to_right')
    data: Data | Any = Field(default=None, union_mode='left_to_right')

class TvEpisodeTranslationsModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: int | Any = Field(default=None, union_mode='left_to_right')
    translations: list[Translation] | Any = Field(default=None, union_mode='left_to_right')
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
