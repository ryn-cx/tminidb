from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from datetime import date
from pydantic import BaseModel

class Episode(BaseModel):
    model_config = ConfigDict(defer_build=True)
    air_date: date
    episode_number: int
    episode_type: str
    id: int
    name: str
    overview: str
    production_code: str
    runtime: int | None
    season_number: int
    show_id: int
    still_path: str | None
    vote_average: float
    vote_count: int
    order: int

class Group(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    name: str
    order: int
    episodes: list[Episode]
    locked: bool | None = None

class Network(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: int
    logo_path: str
    name: str
    origin_country: str

class TvEpisodeGroupDetailsModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    description: str
    episode_count: int
    group_count: int
    groups: list[Group]
    id: str
    name: str
    network: Network | None
    type: int
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
