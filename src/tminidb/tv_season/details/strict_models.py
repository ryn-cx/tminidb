from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import BaseModel, Field
from datetime import date

class CrewItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
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
    model_config = ConfigDict(defer_build=True)
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

class Episode(BaseModel):
    model_config = ConfigDict(defer_build=True)
    air_date: date | None
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
    crew: list[CrewItem]
    guest_stars: list[GuestStar]

class Network(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: int
    logo_path: str | None
    name: str
    origin_country: str

class TvSeasonDetailsModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_id: str = Field(..., alias='_id')
    air_date: date | None
    episodes: list[Episode]
    name: str
    networks: list[Network]
    overview: str
    id: int
    poster_path: str | None
    season_number: int
    vote_average: float
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
