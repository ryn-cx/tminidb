from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from datetime import date
from pydantic import BaseModel, ConfigDict
from typing import Any

class Episode(BaseModel):
    model_config = ConfigDict(extra='ignore')
    air_date: date | None = None
    episode_number: int | None = None
    episode_type: str | None = None
    id: int | None = None
    name: str | None = None
    overview: str | None = None
    production_code: str | None = None
    runtime: int | None = None
    season_number: int | None = None
    show_id: int | None = None
    still_path: str | None = None
    vote_average: float | None = None
    vote_count: int | None = None
    order: int | None = None

class Group(BaseModel):
    model_config = ConfigDict(extra='ignore')
    id: str | None = None
    name: str | None = None
    order: int | None = None
    episodes: list[Episode] | None = None
    locked: bool | None = None

class Network(BaseModel):
    model_config = ConfigDict(extra='ignore')
    id: int | None = None
    logo_path: str | None = None
    name: str | None = None
    origin_country: str | None = None

class TvEpisodeGroupModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    description: str | None = None
    episode_count: int | None = None
    group_count: int | None = None
    groups: list[Group] | None = None
    id: str | None = None
    name: str | None = None
    network: Any | Network | None = None
    type: int | None = None
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
