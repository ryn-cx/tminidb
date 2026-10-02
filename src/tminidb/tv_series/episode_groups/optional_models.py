from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import Field
from pydantic import BaseModel, ConfigDict


class Network(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    id: int | Any = Field(default=None, union_mode="left_to_right")
    logo_path: str | Any = Field(default=None, union_mode="left_to_right")
    name: str | Any = Field(default=None, union_mode="left_to_right")
    origin_country: str | Any = Field(default=None, union_mode="left_to_right")


class Result(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    description: str | Any = Field(default=None, union_mode="left_to_right")
    episode_count: int | Any = Field(default=None, union_mode="left_to_right")
    group_count: int | Any = Field(default=None, union_mode="left_to_right")
    id: str | Any = Field(default=None, union_mode="left_to_right")
    name: str | Any = Field(default=None, union_mode="left_to_right")
    network: Network | Any = Field(default=None, union_mode="left_to_right")
    type: int | Any = Field(default=None, union_mode="left_to_right")


class TvSeriesEpisodeGroupsModel(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    results: list[Result] | Any = Field(default=None, union_mode="left_to_right")
    id: int | Any = Field(default=None, union_mode="left_to_right")
    _raw_input: Any = PrivateAttr(default=None)

    @model_validator(mode="wrap")
    @classmethod
    def _capture_raw_input(
        cls, data: Any, handler: ModelWrapValidatorHandler[Self]
    ) -> Self:
        """Validate the model and keep the input it was built from."""
        model = handler(data)
        model._raw_input = data
        return model

    @property
    def raw_input(self) -> Any:
        """The input this model was validated from, as it was handed over."""
        return self._raw_input
