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

class Ae(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Ag(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Al(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Ao(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Ar(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class BuyItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logo_path: str | None = None
    provider_id: int | None = None
    provider_name: str | None = None
    display_priority: int | None = None

class At(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None
    buy: list[BuyItem] | None = None

class Au(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None
    buy: list[BuyItem] | None = None

class Az(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Ba(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Bb(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Be(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Bg(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Bh(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Bo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Br(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Bs(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class By(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Bz(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Ca(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None
    buy: list[BuyItem] | None = None

class Ch(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Ci(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Cl(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Cm(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Co(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Cr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Cu(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Cv(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Cy(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Cz(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class De(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None
    buy: list[BuyItem] | None = None

class RentItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logo_path: str | None = None
    provider_id: int | None = None
    provider_name: str | None = None
    display_priority: int | None = None

class Dk(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None
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
    flatrate: list[FlatrateItem] | None = None

class Ee(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Eg(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Es(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

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

class Gb(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Gf(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Gg(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Gh(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Gq(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Gr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Gt(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Hk(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Hn(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Hu(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Id(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Ie(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Il(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class In(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Iq(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Is(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class It(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Jm(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Jo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class FreeItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logo_path: str | None = None
    provider_id: int | None = None
    provider_name: str | None = None
    display_priority: int | None = None

class Jp(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    free: list[FreeItem] | None = None
    buy: list[BuyItem] | None = None
    rent: list[RentItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Ke(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Kr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Kw(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

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

class Lu(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Lv(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
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

class Me(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Mg(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Mk(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Ml(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Mt(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Mu(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Mx(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class My(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Mz(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Ne(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Ng(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Ni(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Nl(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class No(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    rent: list[RentItem] | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Nz(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

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
    flatrate: list[FlatrateItem] | None = None

class Pf(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Ph(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Pk(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Pl(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Pt(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Py(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Qa(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Ro(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Rs(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Ad1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logo_path: str | None = None
    provider_id: int | None = None
    provider_name: str | None = None
    display_priority: int | None = None

class Ru(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    ads: list[Ad1] | None = None

class Sa(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Sc(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
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
    flatrate: list[FlatrateItem] | None = None

class Si(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Sk(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Sm(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Sn(BaseModel):
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

class Td(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Th(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Tn(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Tr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Tt(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Tw(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Tz(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Ug(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Us(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    buy: list[BuyItem] | None = None
    flatrate: list[FlatrateItem] | None = None

class Uy(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Ve(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Ye(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Za(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Zm(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Zw(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    link: str | None = None
    flatrate: list[FlatrateItem] | None = None

class Results(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    ad: Ad | None = Field(None, alias='AD')
    ae: Ae | None = Field(None, alias='AE')
    ag: Ag | None = Field(None, alias='AG')
    al: Al | None = Field(None, alias='AL')
    ao: Ao | None = Field(None, alias='AO')
    ar: Ar | None = Field(None, alias='AR')
    at: At | None = Field(None, alias='AT')
    au: Au | None = Field(None, alias='AU')
    az: Az | None = Field(None, alias='AZ')
    ba: Ba | None = Field(None, alias='BA')
    bb: Bb | None = Field(None, alias='BB')
    be: Be | None = Field(None, alias='BE')
    bg: Bg | None = Field(None, alias='BG')
    bh: Bh | None = Field(None, alias='BH')
    bo: Bo | None = Field(None, alias='BO')
    br: Br | None = Field(None, alias='BR')
    bs: Bs | None = Field(None, alias='BS')
    by: By | None = Field(None, alias='BY')
    bz: Bz | None = Field(None, alias='BZ')
    ca: Ca | None = Field(None, alias='CA')
    ch: Ch | None = Field(None, alias='CH')
    ci: Ci | None = Field(None, alias='CI')
    cl: Cl | None = Field(None, alias='CL')
    cm: Cm | None = Field(None, alias='CM')
    co: Co | None = Field(None, alias='CO')
    cr: Cr | None = Field(None, alias='CR')
    cu: Cu | None = Field(None, alias='CU')
    cv: Cv | None = Field(None, alias='CV')
    cy: Cy | None = Field(None, alias='CY')
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
    gh: Gh | None = Field(None, alias='GH')
    gq: Gq | None = Field(None, alias='GQ')
    gr: Gr | None = Field(None, alias='GR')
    gt: Gt | None = Field(None, alias='GT')
    hk: Hk | None = Field(None, alias='HK')
    hn: Hn | None = Field(None, alias='HN')
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
    ke: Ke | None = Field(None, alias='KE')
    kr: Kr | None = Field(None, alias='KR')
    kw: Kw | None = Field(None, alias='KW')
    lb: Lb | None = Field(None, alias='LB')
    lc: Lc | None = Field(None, alias='LC')
    li: Li | None = Field(None, alias='LI')
    lt: Lt | None = Field(None, alias='LT')
    lu: Lu | None = Field(None, alias='LU')
    lv: Lv | None = Field(None, alias='LV')
    ly: Ly | None = Field(None, alias='LY')
    ma: Ma | None = Field(None, alias='MA')
    mc: Mc | None = Field(None, alias='MC')
    me: Me | None = Field(None, alias='ME')
    mg: Mg | None = Field(None, alias='MG')
    mk: Mk | None = Field(None, alias='MK')
    ml: Ml | None = Field(None, alias='ML')
    mt: Mt | None = Field(None, alias='MT')
    mu: Mu | None = Field(None, alias='MU')
    mx: Mx | None = Field(None, alias='MX')
    my: My | None = Field(None, alias='MY')
    mz: Mz | None = Field(None, alias='MZ')
    ne: Ne | None = Field(None, alias='NE')
    ng: Ng | None = Field(None, alias='NG')
    ni: Ni | None = Field(None, alias='NI')
    nl: Nl | None = Field(None, alias='NL')
    no: No | None = Field(None, alias='NO')
    nz: Nz | None = Field(None, alias='NZ')
    om: Om | None = Field(None, alias='OM')
    pa: Pa | None = Field(None, alias='PA')
    pe: Pe | None = Field(None, alias='PE')
    pf: Pf | None = Field(None, alias='PF')
    ph: Ph | None = Field(None, alias='PH')
    pk: Pk | None = Field(None, alias='PK')
    pl: Pl | None = Field(None, alias='PL')
    pt: Pt | None = Field(None, alias='PT')
    py: Py | None = Field(None, alias='PY')
    qa: Qa | None = Field(None, alias='QA')
    ro: Ro | None = Field(None, alias='RO')
    rs: Rs | None = Field(None, alias='RS')
    ru: Ru | None = Field(None, alias='RU')
    sa: Sa | None = Field(None, alias='SA')
    sc: Sc | None = Field(None, alias='SC')
    se: Se | None = Field(None, alias='SE')
    sg: Sg | None = Field(None, alias='SG')
    si: Si | None = Field(None, alias='SI')
    sk: Sk | None = Field(None, alias='SK')
    sm: Sm | None = Field(None, alias='SM')
    sn: Sn | None = Field(None, alias='SN')
    sv: Sv | None = Field(None, alias='SV')
    tc: Tc | None = Field(None, alias='TC')
    td: Td | None = Field(None, alias='TD')
    th: Th | None = Field(None, alias='TH')
    tn: Tn | None = Field(None, alias='TN')
    tr: Tr | None = Field(None, alias='TR')
    tt: Tt | None = Field(None, alias='TT')
    tw: Tw | None = Field(None, alias='TW')
    tz: Tz | None = Field(None, alias='TZ')
    ug: Ug | None = Field(None, alias='UG')
    us: Us | None = Field(None, alias='US')
    uy: Uy | None = Field(None, alias='UY')
    ve: Ve | None = Field(None, alias='VE')
    ye: Ye | None = Field(None, alias='YE')
    za: Za | None = Field(None, alias='ZA')
    zm: Zm | None = Field(None, alias='ZM')
    zw: Zw | None = Field(None, alias='ZW')

class TvSeriesWatchProvidersModel(BaseModel):
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
