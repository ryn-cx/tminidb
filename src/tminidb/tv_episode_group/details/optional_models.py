from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import Field
from datetime import date
from pydantic import BaseModel, ConfigDict

class Episode(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    air_date: date | Any = Field(default=None, union_mode='left_to_right')
    episode_number: int | Any = Field(default=None, union_mode='left_to_right')
    episode_type: str | Any = Field(default=None, union_mode='left_to_right')
    id: int | Any = Field(default=None, union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    overview: str | Any = Field(default=None, union_mode='left_to_right')
    production_code: str | Any = Field(default=None, union_mode='left_to_right')
    runtime: int | Any = Field(default=None, union_mode='left_to_right')
    season_number: int | Any = Field(default=None, union_mode='left_to_right')
    show_id: int | Any = Field(default=None, union_mode='left_to_right')
    still_path: str | Any = Field(default=None, union_mode='left_to_right')
    vote_average: float | Any = Field(default=None, union_mode='left_to_right')
    vote_count: int | Any = Field(default=None, union_mode='left_to_right')
    order: int | Any = Field(default=None, union_mode='left_to_right')

class Group(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    order: int | float | Any = Field(default=None, union_mode='left_to_right')
    episodes: list[Episode] | Any = Field(default=None, union_mode='left_to_right')
    locked: bool | Any = Field(default=None, union_mode='left_to_right')

class Network(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: int | Any = Field(default=None, union_mode='left_to_right')
    logo_path: str | Any = Field(default=None, union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    origin_country: str | Any = Field(default=None, union_mode='left_to_right')

class TvEpisodeGroupDetailsModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    description: str | Any = Field(default=None, union_mode='left_to_right')
    episode_count: int | Any = Field(default=None, union_mode='left_to_right')
    group_count: int | Any = Field(default=None, union_mode='left_to_right')
    groups: list[Group] | Any = Field(default=None, union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    network: Network | Any = Field(default=None, union_mode='left_to_right')
    type: int | Any = Field(default=None, union_mode='left_to_right')
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
