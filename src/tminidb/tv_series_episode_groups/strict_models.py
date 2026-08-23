from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel

class Network(BaseModel):
    id: int
    logo_path: str
    name: str
    origin_country: str

class Result(BaseModel):
    description: str
    episode_count: int
    group_count: int
    id: str
    name: str
    network: Network | None
    type: int

class TvSeriesEpisodeGroupsModel(BaseModel):
    results: list[Result]
    id: int
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
