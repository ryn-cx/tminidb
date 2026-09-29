from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import Field
from pydantic import BaseModel, ConfigDict
from datetime import date

class CrewItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    department: str | Any = Field(default=None, union_mode='left_to_right')
    job: str | Any = Field(default=None, union_mode='left_to_right')
    credit_id: str | Any = Field(default=None, union_mode='left_to_right')
    adult: bool | Any = Field(default=None, union_mode='left_to_right')
    gender: int | Any = Field(default=None, union_mode='left_to_right')
    id: int | Any = Field(default=None, union_mode='left_to_right')
    known_for_department: str | Any = Field(default=None, union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    original_name: str | Any = Field(default=None, union_mode='left_to_right')
    popularity: float | Any = Field(default=None, union_mode='left_to_right')
    profile_path: str | Any = Field(default=None, union_mode='left_to_right')

class GuestStar(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    character: str | Any = Field(default=None, union_mode='left_to_right')
    credit_id: str | Any = Field(default=None, union_mode='left_to_right')
    order: int | Any = Field(default=None, union_mode='left_to_right')
    adult: bool | Any = Field(default=None, union_mode='left_to_right')
    gender: int | Any = Field(default=None, union_mode='left_to_right')
    id: int | Any = Field(default=None, union_mode='left_to_right')
    known_for_department: str | Any = Field(default=None, union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    original_name: str | Any = Field(default=None, union_mode='left_to_right')
    popularity: float | Any = Field(default=None, union_mode='left_to_right')
    profile_path: str | Any = Field(default=None, union_mode='left_to_right')

class TvEpisodeDetailsModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    air_date: date | Any = Field(default=None, union_mode='left_to_right')
    crew: list[CrewItem] | Any = Field(default=None, union_mode='left_to_right')
    episode_number: int | Any = Field(default=None, union_mode='left_to_right')
    episode_type: str | Any = Field(default=None, union_mode='left_to_right')
    guest_stars: list[GuestStar] | Any = Field(default=None, union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    overview: str | Any = Field(default=None, union_mode='left_to_right')
    id: int | Any = Field(default=None, union_mode='left_to_right')
    production_code: str | Any = Field(default=None, union_mode='left_to_right')
    runtime: int | Any = Field(default=None, union_mode='left_to_right')
    season_number: int | Any = Field(default=None, union_mode='left_to_right')
    still_path: str | Any = Field(default=None, union_mode='left_to_right')
    vote_average: float | Any = Field(default=None, union_mode='left_to_right')
    vote_count: int | Any = Field(default=None, union_mode='left_to_right')
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
