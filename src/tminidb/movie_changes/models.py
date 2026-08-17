from typing import Any
from datetime import date
from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import ConfigDict

class Value(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    person_id: int | None = None
    department: str | None = None
    job: str | None = None
    cast_id: int | None = None
    credit_id: str | None = None
    character: str | None = None
    order: int | None = None
    certification: str | None = None
    descriptors: list[None] | None = None
    iso_3166_1: str | None = None
    iso_639_1: str | None = None
    note: str | None = None
    release_date: date | None = None
    type: int | None = None
    name: str | None = None
    id: int | None = None

class Item(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str
    action: str
    time: str
    iso_639_1: str
    iso_3166_1: str
    value: int | str | Value | None = None

class Change(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    key: str
    items: list[Item]

class MovieChangesModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    changes: list[Change]
