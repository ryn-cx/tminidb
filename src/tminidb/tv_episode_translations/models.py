from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import ConfigDict

class Data(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    name: str
    overview: str

class Translation(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    iso_3166_1: str
    iso_639_1: str
    name: str
    english_name: str
    data: Data

class TvEpisodeTranslationsModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: int
    translations: list[Translation]
