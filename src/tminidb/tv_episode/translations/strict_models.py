from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import BaseModel

class Data(BaseModel):
    model_config = ConfigDict(defer_build=True)
    name: str
    overview: str

class Translation(BaseModel):
    model_config = ConfigDict(defer_build=True)
    iso_3166_1: str
    iso_639_1: str
    name: str
    english_name: str
    data: Data

class TvEpisodeTranslationsModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: int
    translations: list[Translation]
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
