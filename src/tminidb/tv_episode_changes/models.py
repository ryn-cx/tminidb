from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import ConfigDict

class OriginalValue(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    person_id: int
    character: str
    order: int
    credit_id: str

class Value(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    person_id: int
    character: str
    order: int
    credit_id: str

class Item(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str
    action: str
    time: str
    iso_639_1: str
    iso_3166_1: str
    original_value: OriginalValue | None = None
    value: Value | None = None

class Change(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    key: str
    items: list[Item]

class TvEpisodeChangesModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    changes: list[Change]
