from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import BaseModel, Field

class RentItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logo_path: str
    provider_id: int
    provider_name: str
    display_priority: int

class BuyItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logo_path: str
    provider_id: int
    provider_name: str
    display_priority: int

class FlatrateItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logo_path: str
    provider_id: int
    provider_name: str
    display_priority: int

class Ae(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Ag(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Al(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Ao(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Ar(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None
    rent: list[RentItem] | None = None

class At(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None
    rent: list[RentItem] | None = None

class Au(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem] | None = None
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None

class Az(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Ba(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Bb(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Be(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Bf(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]

class Bg(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Bo(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None
    rent: list[RentItem] | None = None

class Ad(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logo_path: str
    provider_id: int
    provider_name: str
    display_priority: int

class Br(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None
    ads: list[Ad] | None = None
    flatrate: list[FlatrateItem] | None = None

class Bs(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class By(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Bz(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None
    rent: list[RentItem] | None = None

class Ca(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None
    ads: list[Ad] | None = None

class Ch(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Cl(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem] | None = None
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None

class Co(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None
    buy: list[BuyItem] | None = None

class Cr(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None
    rent: list[RentItem] | None = None

class Cv(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Cy(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Cz(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class De(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Dk(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Do(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Ec(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None
    buy: list[BuyItem] | None = None

class Ee(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Eg(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Es(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem] | None = None
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None

class Fi(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Fj(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Fr(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem] | None = None
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None

class Gb(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None
    buy: list[BuyItem] | None = None

class Gg(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None
    rent: list[RentItem] | None = None

class Gh(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Gr(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Gt(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None
    rent: list[RentItem] | None = None

class Gy(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Hk(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem] | None = None
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None

class Hn(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None
    rent: list[RentItem] | None = None

class Hr(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Hu(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None
    rent: list[RentItem] | None = None

class Id(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem] | None = None
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None

class Ie(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Il(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class In(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem]
    rent: list[RentItem] | None = None

class Is(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem] | None = None
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None

class It(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Jm(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Jp(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem]
    buy: list[BuyItem] | None = None

class Kr(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Lc(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Lt(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Lu(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Lv(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Mc(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Me(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Mk(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Ml(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Mt(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Mu(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Mx(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class My(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem] | None = None
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None

class Mz(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Ni(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem] | None = None
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None

class Nl(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class No(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Nz(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem] | None = None
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None
    ads: list[Ad] | None = None

class Pa(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Pe(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Pg(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    flatrate: list[FlatrateItem] | None = None
    rent: list[RentItem] | None = None

class Ph(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None
    buy: list[BuyItem] | None = None

class Pk(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Pl(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Pt(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None
    rent: list[RentItem] | None = None

class Py(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem] | None = None
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None

class Ro(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Rs(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Ru(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    ads: list[Ad]
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Sa(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Se(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Sg(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None
    buy: list[BuyItem] | None = None

class Si(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Sk(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Sv(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Tc(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Th(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem] | None = None
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None

class Tr(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Tt(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Tw(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Tz(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Ua(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Ug(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Us(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    ads: list[Ad] | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None
    buy: list[BuyItem] | None = None

class Uy(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Ve(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None
    rent: list[RentItem] | None = None

class Za(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Zw(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Ad5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Bh(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Dz(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Gf(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Gi(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Iq(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Jo(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Lb(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Li(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Ly(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Ma(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Om(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Pf(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Qa(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Sm(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Tn(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Va(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Bm(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Ci(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Cm(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Cu(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Gq(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Ke(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Kw(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Md(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Mg(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Ne(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Ng(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Ps(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Sc(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Sn(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Td(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Ye(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Zm(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Results(BaseModel):
    model_config = ConfigDict(defer_build=True)
    ae: Ae | None = Field(None, alias='AE')
    ag: Ag | None = Field(None, alias='AG')
    al: Al | None = Field(None, alias='AL')
    ao: Ao | None = Field(None, alias='AO')
    ar: Ar = Field(..., alias='AR')
    at: At = Field(..., alias='AT')
    au: Au = Field(..., alias='AU')
    az: Az | None = Field(None, alias='AZ')
    ba: Ba | None = Field(None, alias='BA')
    bb: Bb | None = Field(None, alias='BB')
    be: Be = Field(..., alias='BE')
    bf: Bf | None = Field(None, alias='BF')
    bg: Bg = Field(..., alias='BG')
    bo: Bo = Field(..., alias='BO')
    br: Br = Field(..., alias='BR')
    bs: Bs | None = Field(None, alias='BS')
    by: By = Field(..., alias='BY')
    bz: Bz = Field(..., alias='BZ')
    ca: Ca = Field(..., alias='CA')
    ch: Ch = Field(..., alias='CH')
    cl: Cl = Field(..., alias='CL')
    co: Co = Field(..., alias='CO')
    cr: Cr = Field(..., alias='CR')
    cv: Cv = Field(..., alias='CV')
    cy: Cy | None = Field(None, alias='CY')
    cz: Cz = Field(..., alias='CZ')
    de: De = Field(..., alias='DE')
    dk: Dk = Field(..., alias='DK')
    do: Do | None = Field(None, alias='DO')
    ec: Ec = Field(..., alias='EC')
    ee: Ee = Field(..., alias='EE')
    eg: Eg | None = Field(None, alias='EG')
    es: Es = Field(..., alias='ES')
    fi: Fi = Field(..., alias='FI')
    fj: Fj | None = Field(None, alias='FJ')
    fr: Fr = Field(..., alias='FR')
    gb: Gb = Field(..., alias='GB')
    gg: Gg = Field(..., alias='GG')
    gh: Gh | None = Field(None, alias='GH')
    gr: Gr | None = Field(None, alias='GR')
    gt: Gt = Field(..., alias='GT')
    gy: Gy | None = Field(None, alias='GY')
    hk: Hk = Field(..., alias='HK')
    hn: Hn = Field(..., alias='HN')
    hr: Hr | None = Field(None, alias='HR')
    hu: Hu = Field(..., alias='HU')
    id: Id = Field(..., alias='ID')
    ie: Ie = Field(..., alias='IE')
    il: Il = Field(..., alias='IL')
    in_: In | None = Field(None, alias='IN')
    is_: Is = Field(..., alias='IS')
    it: It = Field(..., alias='IT')
    jm: Jm | None = Field(None, alias='JM')
    jp: Jp | None = Field(None, alias='JP')
    kr: Kr | None = Field(None, alias='KR')
    lc: Lc | None = Field(None, alias='LC')
    lt: Lt = Field(..., alias='LT')
    lu: Lu = Field(..., alias='LU')
    lv: Lv = Field(..., alias='LV')
    mc: Mc | None = Field(None, alias='MC')
    me: Me | None = Field(None, alias='ME')
    mk: Mk | None = Field(None, alias='MK')
    ml: Ml | None = Field(None, alias='ML')
    mt: Mt | None = Field(None, alias='MT')
    mu: Mu = Field(..., alias='MU')
    mx: Mx = Field(..., alias='MX')
    my: My = Field(..., alias='MY')
    mz: Mz = Field(..., alias='MZ')
    ni: Ni = Field(..., alias='NI')
    nl: Nl = Field(..., alias='NL')
    no: No = Field(..., alias='NO')
    nz: Nz = Field(..., alias='NZ')
    pa: Pa | None = Field(None, alias='PA')
    pe: Pe = Field(..., alias='PE')
    pg: Pg | None = Field(None, alias='PG')
    ph: Ph = Field(..., alias='PH')
    pk: Pk | None = Field(None, alias='PK')
    pl: Pl = Field(..., alias='PL')
    pt: Pt = Field(..., alias='PT')
    py: Py = Field(..., alias='PY')
    ro: Ro | None = Field(None, alias='RO')
    rs: Rs | None = Field(None, alias='RS')
    ru: Ru | None = Field(None, alias='RU')
    sa: Sa | None = Field(None, alias='SA')
    se: Se = Field(..., alias='SE')
    sg: Sg = Field(..., alias='SG')
    si: Si = Field(..., alias='SI')
    sk: Sk = Field(..., alias='SK')
    sv: Sv | None = Field(None, alias='SV')
    tc: Tc | None = Field(None, alias='TC')
    th: Th = Field(..., alias='TH')
    tr: Tr = Field(..., alias='TR')
    tt: Tt | None = Field(None, alias='TT')
    tw: Tw = Field(..., alias='TW')
    tz: Tz = Field(..., alias='TZ')
    ua: Ua = Field(..., alias='UA')
    ug: Ug | None = Field(None, alias='UG')
    us: Us = Field(..., alias='US')
    uy: Uy | None = Field(None, alias='UY')
    ve: Ve = Field(..., alias='VE')
    za: Za | None = Field(None, alias='ZA')
    zw: Zw | None = Field(None, alias='ZW')
    ad: Ad5 | None = Field(None, alias='AD')
    bh: Bh | None = Field(None, alias='BH')
    dz: Dz | None = Field(None, alias='DZ')
    gf: Gf | None = Field(None, alias='GF')
    gi: Gi | None = Field(None, alias='GI')
    iq: Iq | None = Field(None, alias='IQ')
    jo: Jo | None = Field(None, alias='JO')
    lb: Lb | None = Field(None, alias='LB')
    li: Li | None = Field(None, alias='LI')
    ly: Ly | None = Field(None, alias='LY')
    ma: Ma | None = Field(None, alias='MA')
    om: Om | None = Field(None, alias='OM')
    pf: Pf | None = Field(None, alias='PF')
    qa: Qa | None = Field(None, alias='QA')
    sm: Sm | None = Field(None, alias='SM')
    tn: Tn | None = Field(None, alias='TN')
    va: Va | None = Field(None, alias='VA')
    bm: Bm | None = Field(None, alias='BM')
    ci: Ci | None = Field(None, alias='CI')
    cm: Cm | None = Field(None, alias='CM')
    cu: Cu | None = Field(None, alias='CU')
    gq: Gq | None = Field(None, alias='GQ')
    ke: Ke | None = Field(None, alias='KE')
    kw: Kw | None = Field(None, alias='KW')
    md: Md | None = Field(None, alias='MD')
    mg: Mg | None = Field(None, alias='MG')
    ne: Ne | None = Field(None, alias='NE')
    ng: Ng | None = Field(None, alias='NG')
    ps: Ps | None = Field(None, alias='PS')
    sc: Sc | None = Field(None, alias='SC')
    sn: Sn | None = Field(None, alias='SN')
    td: Td | None = Field(None, alias='TD')
    ye: Ye | None = Field(None, alias='YE')
    zm: Zm | None = Field(None, alias='ZM')

class MovieWatchProvidersModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: int
    results: Results
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
