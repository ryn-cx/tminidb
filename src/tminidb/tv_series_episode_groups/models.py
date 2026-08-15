from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import ConfigDict

class Network(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: int
    logo_path: str
    name: str
    origin_country: str

class Result(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    description: str
    episode_count: int
    group_count: int
    id: str
    name: str
    network: Network | None
    type: int

class TvSeriesEpisodeGroupsModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    results: list[Result]
    id: int
