from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, ConfigDict, Field

class BuyItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logo_path: str | Any = Field(default=None, union_mode='left_to_right')
    provider_id: int | Any = Field(default=None, union_mode='left_to_right')
    provider_name: str | Any = Field(default=None, union_mode='left_to_right')
    display_priority: int | Any = Field(default=None, union_mode='left_to_right')

class FlatrateItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logo_path: str | Any = Field(default=None, union_mode='left_to_right')
    provider_id: int | Any = Field(default=None, union_mode='left_to_right')
    provider_name: str | Any = Field(default=None, union_mode='left_to_right')
    display_priority: int | Any = Field(default=None, union_mode='left_to_right')

class Ad(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logo_path: str | Any = Field(default=None, union_mode='left_to_right')
    provider_id: int | Any = Field(default=None, union_mode='left_to_right')
    provider_name: str | Any = Field(default=None, union_mode='left_to_right')
    display_priority: int | Any = Field(default=None, union_mode='left_to_right')

class FreeItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logo_path: str | Any = Field(default=None, union_mode='left_to_right')
    provider_id: int | Any = Field(default=None, union_mode='left_to_right')
    provider_name: str | Any = Field(default=None, union_mode='left_to_right')
    display_priority: int | Any = Field(default=None, union_mode='left_to_right')

class At(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    buy: list[BuyItem] | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Au(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad] | Any = Field(default=None, union_mode='left_to_right')
    buy: list[BuyItem] | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Ca(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    buy: list[BuyItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class De(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    buy: list[BuyItem] | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Gb(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    buy: list[BuyItem] | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Gg(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    buy: list[BuyItem] | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad] | Any = Field(default=None, union_mode='left_to_right')

class Kr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad] | Any = Field(default=None, union_mode='left_to_right')

class Us(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    buy: list[BuyItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Ae(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad] | Any = Field(default=None, union_mode='left_to_right')

class Bh(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad] | Any = Field(default=None, union_mode='left_to_right')

class Cz(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    buy: list[BuyItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Eg(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad] | Any = Field(default=None, union_mode='left_to_right')

class Ie(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    buy: list[BuyItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class In(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad] | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Jo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad] | Any = Field(default=None, union_mode='left_to_right')

class Lb(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad] | Any = Field(default=None, union_mode='left_to_right')

class Mx(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad] | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    buy: list[BuyItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Nl(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    buy: list[BuyItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Om(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Qa(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad] | Any = Field(default=None, union_mode='left_to_right')

class Sa(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad] | Any = Field(default=None, union_mode='left_to_right')

class Ad21(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad] | Any = Field(default=None, union_mode='left_to_right')

class Ad23(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logo_path: str | Any = Field(default=None, union_mode='left_to_right')
    provider_id: int | Any = Field(default=None, union_mode='left_to_right')
    provider_name: str | Any = Field(default=None, union_mode='left_to_right')
    display_priority: int | Any = Field(default=None, union_mode='left_to_right')

class Ag(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Al(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Ao(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Ar(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    buy: list[BuyItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Az(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Ba(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Bb(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Be(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    buy: list[BuyItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Bg(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    buy: list[BuyItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Bo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Br(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    buy: list[BuyItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Bs(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class By(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Bz(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Ch(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    buy: list[BuyItem] | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Ci(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Cl(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    buy: list[BuyItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Cm(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Co(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    buy: list[BuyItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Cr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Cu(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Cv(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Cy(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class RentItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logo_path: str | Any = Field(default=None, union_mode='left_to_right')
    provider_id: int | Any = Field(default=None, union_mode='left_to_right')
    provider_name: str | Any = Field(default=None, union_mode='left_to_right')
    display_priority: int | Any = Field(default=None, union_mode='left_to_right')

class Dk(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    rent: list[RentItem] | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    buy: list[BuyItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Do(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Dz(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Ec(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Ee(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    buy: list[BuyItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Es(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    buy: list[BuyItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Fi(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    buy: list[BuyItem] | Any = Field(default=None, union_mode='left_to_right')
    rent: list[RentItem] | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Fj(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Fr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    buy: list[BuyItem] | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    rent: list[RentItem] | Any = Field(default=None, union_mode='left_to_right')

class Gf(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Gh(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Gq(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Gr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    buy: list[BuyItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Gt(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Hk(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    rent: list[RentItem] | Any = Field(default=None, union_mode='left_to_right')

class Hn(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Hu(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    buy: list[BuyItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Id(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Il(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Iq(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Is(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    buy: list[BuyItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    rent: list[RentItem] | Any = Field(default=None, union_mode='left_to_right')

class It(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    buy: list[BuyItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Jm(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Jp(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    buy: list[BuyItem] | Any = Field(default=None, union_mode='left_to_right')
    rent: list[RentItem] | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Ke(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Kw(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Lc(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Li(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Lt(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    buy: list[BuyItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Lu(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Lv(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    buy: list[BuyItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Ly(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Ma(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Mc(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Me(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Mg(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Mk(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Ml(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Mt(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Mu(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class My(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Mz(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Ne(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Ng(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Ni(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class No(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    rent: list[RentItem] | Any = Field(default=None, union_mode='left_to_right')
    buy: list[BuyItem] | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Nz(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    buy: list[BuyItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Pa(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Pe(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Pf(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Ph(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Pk(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Pl(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    buy: list[BuyItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Pt(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    buy: list[BuyItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Py(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Ro(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    buy: list[BuyItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Rs(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Ru(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    buy: list[BuyItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Sc(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Se(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    buy: list[BuyItem] | Any = Field(default=None, union_mode='left_to_right')
    rent: list[RentItem] | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Sg(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Si(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Sk(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    buy: list[BuyItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    rent: list[RentItem] | Any = Field(default=None, union_mode='left_to_right')

class Sm(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Sn(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Sv(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Tc(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Td(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Th(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Tn(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Tr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    buy: list[BuyItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Tt(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Tw(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    rent: list[RentItem] | Any = Field(default=None, union_mode='left_to_right')

class Tz(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Ug(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Uy(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Ve(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Ye(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Za(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Zm(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Zw(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Bm(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Gi(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Hr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    buy: list[BuyItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Md(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Ps(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Ua(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Va(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Bf(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Cd(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Gy(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Mw(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')

class Pg(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')

class Xk(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | Any = Field(default=None, union_mode='left_to_right')
    ads: list[Ad23] | Any = Field(default=None, union_mode='left_to_right')
    free: list[FreeItem] | Any = Field(default=None, union_mode='left_to_right')
    flatrate: list[FlatrateItem] | Any = Field(default=None, union_mode='left_to_right')

class Results(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    at: At | Any = Field(None, alias='AT', union_mode='left_to_right')
    au: Au | Any = Field(None, alias='AU', union_mode='left_to_right')
    ca: Ca | Any = Field(None, alias='CA', union_mode='left_to_right')
    de: De | Any = Field(None, alias='DE', union_mode='left_to_right')
    gb: Gb | Any = Field(None, alias='GB', union_mode='left_to_right')
    gg: Gg | Any = Field(None, alias='GG', union_mode='left_to_right')
    kr: Kr | Any = Field(None, alias='KR', union_mode='left_to_right')
    us: Us | Any = Field(None, alias='US', union_mode='left_to_right')
    ae: Ae | Any = Field(None, alias='AE', union_mode='left_to_right')
    bh: Bh | Any = Field(None, alias='BH', union_mode='left_to_right')
    cz: Cz | Any = Field(None, alias='CZ', union_mode='left_to_right')
    eg: Eg | Any = Field(None, alias='EG', union_mode='left_to_right')
    ie: Ie | Any = Field(None, alias='IE', union_mode='left_to_right')
    in_: In | Any = Field(None, alias='IN', union_mode='left_to_right')
    jo: Jo | Any = Field(None, alias='JO', union_mode='left_to_right')
    lb: Lb | Any = Field(None, alias='LB', union_mode='left_to_right')
    mx: Mx | Any = Field(None, alias='MX', union_mode='left_to_right')
    nl: Nl | Any = Field(None, alias='NL', union_mode='left_to_right')
    om: Om | Any = Field(None, alias='OM', union_mode='left_to_right')
    qa: Qa | Any = Field(None, alias='QA', union_mode='left_to_right')
    sa: Sa | Any = Field(None, alias='SA', union_mode='left_to_right')
    ad: Ad21 | Any = Field(None, alias='AD', union_mode='left_to_right')
    ag: Ag | Any = Field(None, alias='AG', union_mode='left_to_right')
    al: Al | Any = Field(None, alias='AL', union_mode='left_to_right')
    ao: Ao | Any = Field(None, alias='AO', union_mode='left_to_right')
    ar: Ar | Any = Field(None, alias='AR', union_mode='left_to_right')
    az: Az | Any = Field(None, alias='AZ', union_mode='left_to_right')
    ba: Ba | Any = Field(None, alias='BA', union_mode='left_to_right')
    bb: Bb | Any = Field(None, alias='BB', union_mode='left_to_right')
    be: Be | Any = Field(None, alias='BE', union_mode='left_to_right')
    bg: Bg | Any = Field(None, alias='BG', union_mode='left_to_right')
    bo: Bo | Any = Field(None, alias='BO', union_mode='left_to_right')
    br: Br | Any = Field(None, alias='BR', union_mode='left_to_right')
    bs: Bs | Any = Field(None, alias='BS', union_mode='left_to_right')
    by: By | Any = Field(None, alias='BY', union_mode='left_to_right')
    bz: Bz | Any = Field(None, alias='BZ', union_mode='left_to_right')
    ch: Ch | Any = Field(None, alias='CH', union_mode='left_to_right')
    ci: Ci | Any = Field(None, alias='CI', union_mode='left_to_right')
    cl: Cl | Any = Field(None, alias='CL', union_mode='left_to_right')
    cm: Cm | Any = Field(None, alias='CM', union_mode='left_to_right')
    co: Co | Any = Field(None, alias='CO', union_mode='left_to_right')
    cr: Cr | Any = Field(None, alias='CR', union_mode='left_to_right')
    cu: Cu | Any = Field(None, alias='CU', union_mode='left_to_right')
    cv: Cv | Any = Field(None, alias='CV', union_mode='left_to_right')
    cy: Cy | Any = Field(None, alias='CY', union_mode='left_to_right')
    dk: Dk | Any = Field(None, alias='DK', union_mode='left_to_right')
    do: Do | Any = Field(None, alias='DO', union_mode='left_to_right')
    dz: Dz | Any = Field(None, alias='DZ', union_mode='left_to_right')
    ec: Ec | Any = Field(None, alias='EC', union_mode='left_to_right')
    ee: Ee | Any = Field(None, alias='EE', union_mode='left_to_right')
    es: Es | Any = Field(None, alias='ES', union_mode='left_to_right')
    fi: Fi | Any = Field(None, alias='FI', union_mode='left_to_right')
    fj: Fj | Any = Field(None, alias='FJ', union_mode='left_to_right')
    fr: Fr | Any = Field(None, alias='FR', union_mode='left_to_right')
    gf: Gf | Any = Field(None, alias='GF', union_mode='left_to_right')
    gh: Gh | Any = Field(None, alias='GH', union_mode='left_to_right')
    gq: Gq | Any = Field(None, alias='GQ', union_mode='left_to_right')
    gr: Gr | Any = Field(None, alias='GR', union_mode='left_to_right')
    gt: Gt | Any = Field(None, alias='GT', union_mode='left_to_right')
    hk: Hk | Any = Field(None, alias='HK', union_mode='left_to_right')
    hn: Hn | Any = Field(None, alias='HN', union_mode='left_to_right')
    hu: Hu | Any = Field(None, alias='HU', union_mode='left_to_right')
    id: Id | Any = Field(None, alias='ID', union_mode='left_to_right')
    il: Il | Any = Field(None, alias='IL', union_mode='left_to_right')
    iq: Iq | Any = Field(None, alias='IQ', union_mode='left_to_right')
    is_: Is | Any = Field(None, alias='IS', union_mode='left_to_right')
    it: It | Any = Field(None, alias='IT', union_mode='left_to_right')
    jm: Jm | Any = Field(None, alias='JM', union_mode='left_to_right')
    jp: Jp | Any = Field(None, alias='JP', union_mode='left_to_right')
    ke: Ke | Any = Field(None, alias='KE', union_mode='left_to_right')
    kw: Kw | Any = Field(None, alias='KW', union_mode='left_to_right')
    lc: Lc | Any = Field(None, alias='LC', union_mode='left_to_right')
    li: Li | Any = Field(None, alias='LI', union_mode='left_to_right')
    lt: Lt | Any = Field(None, alias='LT', union_mode='left_to_right')
    lu: Lu | Any = Field(None, alias='LU', union_mode='left_to_right')
    lv: Lv | Any = Field(None, alias='LV', union_mode='left_to_right')
    ly: Ly | Any = Field(None, alias='LY', union_mode='left_to_right')
    ma: Ma | Any = Field(None, alias='MA', union_mode='left_to_right')
    mc: Mc | Any = Field(None, alias='MC', union_mode='left_to_right')
    me: Me | Any = Field(None, alias='ME', union_mode='left_to_right')
    mg: Mg | Any = Field(None, alias='MG', union_mode='left_to_right')
    mk: Mk | Any = Field(None, alias='MK', union_mode='left_to_right')
    ml: Ml | Any = Field(None, alias='ML', union_mode='left_to_right')
    mt: Mt | Any = Field(None, alias='MT', union_mode='left_to_right')
    mu: Mu | Any = Field(None, alias='MU', union_mode='left_to_right')
    my: My | Any = Field(None, alias='MY', union_mode='left_to_right')
    mz: Mz | Any = Field(None, alias='MZ', union_mode='left_to_right')
    ne: Ne | Any = Field(None, alias='NE', union_mode='left_to_right')
    ng: Ng | Any = Field(None, alias='NG', union_mode='left_to_right')
    ni: Ni | Any = Field(None, alias='NI', union_mode='left_to_right')
    no: No | Any = Field(None, alias='NO', union_mode='left_to_right')
    nz: Nz | Any = Field(None, alias='NZ', union_mode='left_to_right')
    pa: Pa | Any = Field(None, alias='PA', union_mode='left_to_right')
    pe: Pe | Any = Field(None, alias='PE', union_mode='left_to_right')
    pf: Pf | Any = Field(None, alias='PF', union_mode='left_to_right')
    ph: Ph | Any = Field(None, alias='PH', union_mode='left_to_right')
    pk: Pk | Any = Field(None, alias='PK', union_mode='left_to_right')
    pl: Pl | Any = Field(None, alias='PL', union_mode='left_to_right')
    pt: Pt | Any = Field(None, alias='PT', union_mode='left_to_right')
    py: Py | Any = Field(None, alias='PY', union_mode='left_to_right')
    ro: Ro | Any = Field(None, alias='RO', union_mode='left_to_right')
    rs: Rs | Any = Field(None, alias='RS', union_mode='left_to_right')
    ru: Ru | Any = Field(None, alias='RU', union_mode='left_to_right')
    sc: Sc | Any = Field(None, alias='SC', union_mode='left_to_right')
    se: Se | Any = Field(None, alias='SE', union_mode='left_to_right')
    sg: Sg | Any = Field(None, alias='SG', union_mode='left_to_right')
    si: Si | Any = Field(None, alias='SI', union_mode='left_to_right')
    sk: Sk | Any = Field(None, alias='SK', union_mode='left_to_right')
    sm: Sm | Any = Field(None, alias='SM', union_mode='left_to_right')
    sn: Sn | Any = Field(None, alias='SN', union_mode='left_to_right')
    sv: Sv | Any = Field(None, alias='SV', union_mode='left_to_right')
    tc: Tc | Any = Field(None, alias='TC', union_mode='left_to_right')
    td: Td | Any = Field(None, alias='TD', union_mode='left_to_right')
    th: Th | Any = Field(None, alias='TH', union_mode='left_to_right')
    tn: Tn | Any = Field(None, alias='TN', union_mode='left_to_right')
    tr: Tr | Any = Field(None, alias='TR', union_mode='left_to_right')
    tt: Tt | Any = Field(None, alias='TT', union_mode='left_to_right')
    tw: Tw | Any = Field(None, alias='TW', union_mode='left_to_right')
    tz: Tz | Any = Field(None, alias='TZ', union_mode='left_to_right')
    ug: Ug | Any = Field(None, alias='UG', union_mode='left_to_right')
    uy: Uy | Any = Field(None, alias='UY', union_mode='left_to_right')
    ve: Ve | Any = Field(None, alias='VE', union_mode='left_to_right')
    ye: Ye | Any = Field(None, alias='YE', union_mode='left_to_right')
    za: Za | Any = Field(None, alias='ZA', union_mode='left_to_right')
    zm: Zm | Any = Field(None, alias='ZM', union_mode='left_to_right')
    zw: Zw | Any = Field(None, alias='ZW', union_mode='left_to_right')
    bm: Bm | Any = Field(None, alias='BM', union_mode='left_to_right')
    gi: Gi | Any = Field(None, alias='GI', union_mode='left_to_right')
    hr: Hr | Any = Field(None, alias='HR', union_mode='left_to_right')
    md: Md | Any = Field(None, alias='MD', union_mode='left_to_right')
    ps: Ps | Any = Field(None, alias='PS', union_mode='left_to_right')
    ua: Ua | Any = Field(None, alias='UA', union_mode='left_to_right')
    va: Va | Any = Field(None, alias='VA', union_mode='left_to_right')
    bf: Bf | Any = Field(None, alias='BF', union_mode='left_to_right')
    cd: Cd | Any = Field(None, alias='CD', union_mode='left_to_right')
    gy: Gy | Any = Field(None, alias='GY', union_mode='left_to_right')
    mw: Mw | Any = Field(None, alias='MW', union_mode='left_to_right')
    pg: Pg | Any = Field(None, alias='PG', union_mode='left_to_right')
    xk: Xk | Any = Field(None, alias='XK', union_mode='left_to_right')

class TvSeriesWatchProvidersModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: int | Any = Field(default=None, union_mode='left_to_right')
    results: Results | Any = Field(default=None, union_mode='left_to_right')
    _raw_input: Any = PrivateAttr(default=None)

    @model_validator(mode='wrap')
    @classmethod
    def _capture_raw_input(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
        """Validate the model and keep the input it was built from."""
        model = handler(data)
        model._raw_input = data
        return model

    @property
    def raw_input(self) -> Any:
        """The input this model was validated from, as it was handed over."""
        return self._raw_input
