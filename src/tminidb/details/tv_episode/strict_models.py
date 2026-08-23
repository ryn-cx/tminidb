from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel
from datetime import date

class CrewItem(BaseModel):
    department: str
    job: str
    credit_id: str
    adult: bool
    gender: int
    id: int
    known_for_department: str
    name: str
    original_name: str
    popularity: float
    profile_path: str | None

class GuestStar(BaseModel):
    character: str
    credit_id: str
    order: int
    adult: bool
    gender: int
    id: int
    known_for_department: str
    name: str
    original_name: str
    popularity: float
    profile_path: str | None

class TvEpisodeModel(BaseModel):
    air_date: date
    crew: list[CrewItem]
    episode_number: int
    episode_type: str
    guest_stars: list[GuestStar]
    name: str
    overview: str
    id: int
    production_code: str
    runtime: int
    season_number: int
    still_path: str
    vote_average: float
    vote_count: int
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
