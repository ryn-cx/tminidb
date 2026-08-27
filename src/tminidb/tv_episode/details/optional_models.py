from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, ConfigDict
from datetime import date

class CrewItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    department: str | None = None
    job: str | None = None
    credit_id: str | None = None
    adult: bool | None = None
    gender: int | None = None
    id: int | None = None
    known_for_department: str | None = None
    name: str | None = None
    original_name: str | None = None
    popularity: float | None = None
    profile_path: str | None = None

class GuestStar(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    character: str | None = None
    credit_id: str | None = None
    order: int | None = None
    adult: bool | None = None
    gender: int | None = None
    id: int | None = None
    known_for_department: str | None = None
    name: str | None = None
    original_name: str | None = None
    popularity: float | None = None
    profile_path: str | None = None

class TvEpisodeDetailsModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    air_date: date | None = None
    crew: list[CrewItem] | None = None
    episode_number: int | None = None
    episode_type: str | None = None
    guest_stars: list[GuestStar] | None = None
    name: str | None = None
    overview: str | None = None
    id: int | None = None
    production_code: str | None = None
    runtime: int | None = None
    season_number: int | None = None
    still_path: str | None = None
    vote_average: float | None = None
    vote_count: int | None = None
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
