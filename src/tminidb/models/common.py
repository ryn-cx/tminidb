# TODO: Validate

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


# TODO: Validate
class Genre(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: int
    name: str


# TODO: Validate
class ProductionCompany(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: int
    logo_path: str | None
    name: str
    origin_country: str


# TODO: Validate
class ProductionCountry(BaseModel):
    model_config = ConfigDict(frozen=True)

    iso_3166_1: str
    name: str


# TODO: Validate
class SpokenLanguage(BaseModel):
    model_config = ConfigDict(frozen=True)

    english_name: str
    iso_639_1: str
    name: str


# TODO: Validate
class Network(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: int
    logo_path: str | None
    name: str
    origin_country: str


# TODO: Validate
class CrewMember(BaseModel):
    model_config = ConfigDict(frozen=True)

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


# TODO: Validate
class GuestStar(BaseModel):
    model_config = ConfigDict(frozen=True)

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
