from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import ConfigDict

class Poster(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    file_path: str
    iso_639_1: str | None = None
    iso_3166_1: str | None = None

class Value(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    season_id: int | None = None
    season_number: int | None = None
    poster: Poster | None = None

class OriginalValue(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    poster: Poster | None = None
    name: str | None = None
    id: int | None = None
    group: str | None = None

class Item(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str
    action: str
    time: str
    iso_639_1: str
    iso_3166_1: str
    value: Value | None = None
    original_value: OriginalValue | None = None

class Change(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    key: str
    items: list[Item]

class TvSeriesChangesModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    changes: list[Change]
