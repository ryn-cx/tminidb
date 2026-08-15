from datetime import date
from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import ConfigDict

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
    order: int

class Group(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str
    name: str
    order: int
    episodes: list[Episode]
    locked: bool

class Network(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: int
    logo_path: str
    name: str
    origin_country: str

class TvEpisodeGroupDetailsModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    description: str
    episode_count: int
    group_count: int
    groups: list[Group]
    id: str
    name: str
    network: Network | None
    type: int
