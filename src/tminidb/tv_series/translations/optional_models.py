from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, ConfigDict

class Data(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    overview: str | None = None
    homepage: str | None = None
    tagline: str | None = None

class Translation(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    iso_3166_1: str | None = None
    iso_639_1: str | None = None
    name: str | None = None
    english_name: str | None = None
    data: Data | None = None

class TvSeriesTranslationsModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: int | None = None
    translations: list[Translation] | None = None
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
