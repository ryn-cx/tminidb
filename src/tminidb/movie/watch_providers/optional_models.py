from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, ConfigDict, Field

class FlatrateItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logo_path: str | None = None
    provider_id: int | None = None
    provider_name: str | None = None
    display_priority: int | None = None

class Ad(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class RentItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logo_path: str | None = None
    provider_id: int | None = None
    provider_name: str | None = None
    display_priority: int | None = None

class BuyItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logo_path: str | None = None
    provider_id: int | None = None
    provider_name: str | None = None
    display_priority: int | None = None

class Ae(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None

class Ag(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Ao(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None

class Ar(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None
    rent: list[RentItem] | None = None

class At(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None
    rent: list[RentItem] | None = None

class Au(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None

class Az(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None

class Bb(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Be(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Bf(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None

class Bg(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None

class Bh(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Bo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Br(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None
    rent: list[RentItem] | None = None

class Bs(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class By(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None

class Bz(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None
    buy: list[BuyItem] | None = None

class Ad1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logo_path: str | None = None
    provider_id: int | None = None
    provider_name: str | None = None
    display_priority: int | None = None

class Ca(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    ads: list[Ad1] | None = None
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Ch(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None
    rent: list[RentItem] | None = None

class Cl(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Co(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Cr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None
    rent: list[RentItem] | None = None

class Cv(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None

class Cz(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class De(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Dk(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None

class Do(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Dz(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Ec(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Ee(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Eg(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None

class Es(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None

class Fi(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Fj(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Fr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None
    rent: list[RentItem] | None = None

class Gb(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None

class Gf(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Gg(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Gi(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Gt(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None

class Gy(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Hk(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None

class Hn(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None
    buy: list[BuyItem] | None = None

class Hr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None

class Hu(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None

class Id(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None

class Ie(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None

class Il(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None
    rent: list[RentItem] | None = None

class In(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Iq(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Is(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None
    rent: list[RentItem] | None = None

class It(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None

class Jm(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Jo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Jp(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Kr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None

class Lb(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Lc(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Li(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Lt(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None

class Lu(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None

class Lv(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Ly(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Ma(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Mc(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Ml(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None

class Mt(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Mu(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None

class Mx(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None

class My(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None
    rent: list[RentItem] | None = None

class Mz(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None

class Ni(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None

class Nl(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None

class No(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Nz(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    rent: list[RentItem] | None = None
    ads: list[Ad1] | None = None
    flatrate: list[FlatrateItem] | None = None
    buy: list[BuyItem] | None = None

class Om(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Pa(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Pe(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Pf(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Pg(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None
    rent: list[RentItem] | None = None

class Ph(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None

class Pk(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Pl(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Pt(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Py(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None

class Qa(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Ro(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None

class Ru(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    ads: list[Ad1] | None = None

class Sa(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Se(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Sg(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Si(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None

class Sk(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None

class Sm(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Sv(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Tc(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Th(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Tn(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Tr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None

class Tt(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Tw(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None

class Tz(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None

class Ua(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None

class Ug(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None

class Us(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None
    buy: list[BuyItem] | None = None

class Uy(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Va(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Ve(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None

class Za(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None

class Zw(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None

class Results(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    ad: Ad | None = Field(None, alias='AD')
    ae: Ae | None = Field(None, alias='AE')
    ag: Ag | None = Field(None, alias='AG')
    ao: Ao | None = Field(None, alias='AO')
    ar: Ar | None = Field(None, alias='AR')
    at: At | None = Field(None, alias='AT')
    au: Au | None = Field(None, alias='AU')
    az: Az | None = Field(None, alias='AZ')
    bb: Bb | None = Field(None, alias='BB')
    be: Be | None = Field(None, alias='BE')
    bf: Bf | None = Field(None, alias='BF')
    bg: Bg | None = Field(None, alias='BG')
    bh: Bh | None = Field(None, alias='BH')
    bo: Bo | None = Field(None, alias='BO')
    br: Br | None = Field(None, alias='BR')
    bs: Bs | None = Field(None, alias='BS')
    by: By | None = Field(None, alias='BY')
    bz: Bz | None = Field(None, alias='BZ')
    ca: Ca | None = Field(None, alias='CA')
    ch: Ch | None = Field(None, alias='CH')
    cl: Cl | None = Field(None, alias='CL')
    co: Co | None = Field(None, alias='CO')
    cr: Cr | None = Field(None, alias='CR')
    cv: Cv | None = Field(None, alias='CV')
    cz: Cz | None = Field(None, alias='CZ')
    de: De | None = Field(None, alias='DE')
    dk: Dk | None = Field(None, alias='DK')
    do: Do | None = Field(None, alias='DO')
    dz: Dz | None = Field(None, alias='DZ')
    ec: Ec | None = Field(None, alias='EC')
    ee: Ee | None = Field(None, alias='EE')
    eg: Eg | None = Field(None, alias='EG')
    es: Es | None = Field(None, alias='ES')
    fi: Fi | None = Field(None, alias='FI')
    fj: Fj | None = Field(None, alias='FJ')
    fr: Fr | None = Field(None, alias='FR')
    gb: Gb | None = Field(None, alias='GB')
    gf: Gf | None = Field(None, alias='GF')
    gg: Gg | None = Field(None, alias='GG')
    gi: Gi | None = Field(None, alias='GI')
    gt: Gt | None = Field(None, alias='GT')
    gy: Gy | None = Field(None, alias='GY')
    hk: Hk | None = Field(None, alias='HK')
    hn: Hn | None = Field(None, alias='HN')
    hr: Hr | None = Field(None, alias='HR')
    hu: Hu | None = Field(None, alias='HU')
    id: Id | None = Field(None, alias='ID')
    ie: Ie | None = Field(None, alias='IE')
    il: Il | None = Field(None, alias='IL')
    in_: In | None = Field(None, alias='IN')
    iq: Iq | None = Field(None, alias='IQ')
    is_: Is | None = Field(None, alias='IS')
    it: It | None = Field(None, alias='IT')
    jm: Jm | None = Field(None, alias='JM')
    jo: Jo | None = Field(None, alias='JO')
    jp: Jp | None = Field(None, alias='JP')
    kr: Kr | None = Field(None, alias='KR')
    lb: Lb | None = Field(None, alias='LB')
    lc: Lc | None = Field(None, alias='LC')
    li: Li | None = Field(None, alias='LI')
    lt: Lt | None = Field(None, alias='LT')
    lu: Lu | None = Field(None, alias='LU')
    lv: Lv | None = Field(None, alias='LV')
    ly: Ly | None = Field(None, alias='LY')
    ma: Ma | None = Field(None, alias='MA')
    mc: Mc | None = Field(None, alias='MC')
    ml: Ml | None = Field(None, alias='ML')
    mt: Mt | None = Field(None, alias='MT')
    mu: Mu | None = Field(None, alias='MU')
    mx: Mx | None = Field(None, alias='MX')
    my: My | None = Field(None, alias='MY')
    mz: Mz | None = Field(None, alias='MZ')
    ni: Ni | None = Field(None, alias='NI')
    nl: Nl | None = Field(None, alias='NL')
    no: No | None = Field(None, alias='NO')
    nz: Nz | None = Field(None, alias='NZ')
    om: Om | None = Field(None, alias='OM')
    pa: Pa | None = Field(None, alias='PA')
    pe: Pe | None = Field(None, alias='PE')
    pf: Pf | None = Field(None, alias='PF')
    pg: Pg | None = Field(None, alias='PG')
    ph: Ph | None = Field(None, alias='PH')
    pk: Pk | None = Field(None, alias='PK')
    pl: Pl | None = Field(None, alias='PL')
    pt: Pt | None = Field(None, alias='PT')
    py: Py | None = Field(None, alias='PY')
    qa: Qa | None = Field(None, alias='QA')
    ro: Ro | None = Field(None, alias='RO')
    ru: Ru | None = Field(None, alias='RU')
    sa: Sa | None = Field(None, alias='SA')
    se: Se | None = Field(None, alias='SE')
    sg: Sg | None = Field(None, alias='SG')
    si: Si | None = Field(None, alias='SI')
    sk: Sk | None = Field(None, alias='SK')
    sm: Sm | None = Field(None, alias='SM')
    sv: Sv | None = Field(None, alias='SV')
    tc: Tc | None = Field(None, alias='TC')
    th: Th | None = Field(None, alias='TH')
    tn: Tn | None = Field(None, alias='TN')
    tr: Tr | None = Field(None, alias='TR')
    tt: Tt | None = Field(None, alias='TT')
    tw: Tw | None = Field(None, alias='TW')
    tz: Tz | None = Field(None, alias='TZ')
    ua: Ua | None = Field(None, alias='UA')
    ug: Ug | None = Field(None, alias='UG')
    us: Us | None = Field(None, alias='US')
    uy: Uy | None = Field(None, alias='UY')
    va: Va | None = Field(None, alias='VA')
    ve: Ve | None = Field(None, alias='VE')
    za: Za | None = Field(None, alias='ZA')
    zw: Zw | None = Field(None, alias='ZW')

class MovieWatchProvidersModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: int | None = None
    results: Results | None = None
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
