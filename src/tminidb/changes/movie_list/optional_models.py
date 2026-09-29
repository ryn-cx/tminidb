from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import Field
from pydantic import BaseModel, ConfigDict

class Result(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: int | Any = Field(default=None, union_mode='left_to_right')
    adult: bool | Any = Field(default=None, union_mode='left_to_right')
    softcore: bool | Any = Field(default=None, union_mode='left_to_right')

class ChangesMovieListModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    results: list[Result] | Any = Field(default=None, union_mode='left_to_right')
    page: int | Any = Field(default=None, union_mode='left_to_right')
    total_pages: int | Any = Field(default=None, union_mode='left_to_right')
    total_results: int | Any = Field(default=None, union_mode='left_to_right')
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
