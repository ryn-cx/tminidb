from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import Field
from pydantic import AwareDatetime, BaseModel, ConfigDict

class Result(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    iso_639_1: str | Any = Field(default=None, union_mode='left_to_right')
    iso_3166_1: str | Any = Field(default=None, union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    key: str | Any = Field(default=None, union_mode='left_to_right')
    site: str | Any = Field(default=None, union_mode='left_to_right')
    size: int | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    official: bool | Any = Field(default=None, union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    published_at: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')

class TvSeriesVideosModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: int | Any = Field(default=None, union_mode='left_to_right')
    results: list[Result] | Any = Field(default=None, union_mode='left_to_right')
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
