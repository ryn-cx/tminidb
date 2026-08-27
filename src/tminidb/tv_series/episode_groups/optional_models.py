from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, ConfigDict
from typing import Any

class Network(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: int | None = None
    logo_path: str | None = None
    name: str | None = None
    origin_country: str | None = None

class Result(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    description: str | None = None
    episode_count: int | None = None
    group_count: int | None = None
    id: str | None = None
    name: str | None = None
    network: Any | Network | None = None
    type: int | None = None

class TvSeriesEpisodeGroupsModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    results: list[Result] | None = None
    id: int | None = None
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
