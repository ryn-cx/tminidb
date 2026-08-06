from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import ConfigDict
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

class TvEpisodeDetailsModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    air_date: date
    crew: list[CrewItem]
    episode_number: int
    episode_type: str
    guest_stars: list[GuestStar]
    name: str
    overview: str
    id: int
    production_code: str
    runtime: int | None
    season_number: int
    still_path: str | None
    vote_average: float
    vote_count: int
