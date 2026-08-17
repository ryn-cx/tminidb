from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import ConfigDict

class Poster(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    file_path: str
    iso_639_1: str | None = None
    iso_3166_1: str | None = None

class Value(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    episode_id: int | None = None
    episode_number: int | None = None
    poster: Poster | None = None

class Poster1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    file_path: str
    iso_639_1: str
    iso_3166_1: str

class OriginalValue(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    poster: Poster1

class Item(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str
    action: str
    time: str
    iso_639_1: str
    iso_3166_1: str
    value: str | Value
    original_value: str | OriginalValue | None = None

class Change(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    key: str
    items: list[Item]

class TvSeasonChangesModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    changes: list[Change]
