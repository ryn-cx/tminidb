from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import ConfigDict, Field
from datetime import date

class CrewItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
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

class GuestStar(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
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

class Episode(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    air_date: date
    episode_number: int
    episode_type: str
    id: int
    name: str
    overview: str
    production_code: str
    runtime: int
    season_number: int
    show_id: int
    still_path: str
    vote_average: float
    vote_count: int
    crew: list[CrewItem]
    guest_stars: list[GuestStar]

class Network(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: int
    logo_path: str
    name: str
    origin_country: str

class TvSeasonDetailsModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_id: str = Field(..., alias='_id')
    air_date: date
    episodes: list[Episode]
    name: str
    networks: list[Network]
    overview: str
    id: int
    poster_path: str
    season_number: int
    vote_average: float
