from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import BaseModel, Field

class BuyItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logo_path: str
    provider_id: int
    provider_name: str
    display_priority: int

class RentItem(BaseModel):
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

class Ar(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem] | None = None

class At(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem] | None = None

class Au(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem] | None = None

class Be(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem] | None = None

class Bg(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]

class Bo(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem] | None = None

class Br(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem] | None = None

class By(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]

class Bz(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem] | None = None

class Ad(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logo_path: str
    provider_id: int
    provider_name: str
    display_priority: int

class Ca(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    ads: list[Ad] | None = None
    flatrate: list[FlatrateItem] | None = None

class Ch(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem] | None = None

class Cl(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem] | None = None

class Co(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem] | None = None

class Cr(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem] | None = None

class Cv(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]

class Cz(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem] | None = None

class De(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem] | None = None

class Dk(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem] | None = None

class Ec(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem] | None = None

class Ee(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem] | None = None

class Es(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem] | None = None

class Fi(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem] | None = None

class Fr(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem] | None = None

class Gb(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem] | None = None

class Gg(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem] | None = None

class Gr(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]

class Gt(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem] | None = None

class Hk(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem] | None = None

class Hn(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem] | None = None

class Hu(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]

class Id(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem] | None = None

class Ie(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem] | None = None

class Il(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem] | None = None

class Is(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem] | None = None

class It(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem] | None = None

class Lt(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem] | None = None

class Lu(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem] | None = None

class Lv(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem] | None = None

class Mu(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]

class Mx(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem] | None = None

class My(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem] | None = None

class Mz(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]

class Ni(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem] | None = None

class Nl(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem] | None = None

class No(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem] | None = None

class Nz(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    ads: list[Ad] | None = None
    flatrate: list[FlatrateItem] | None = None

class Pe(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem] | None = None

class Ph(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem] | None = None

class Pl(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem] | None = None

class Pt(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem] | None = None

class Py(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem] | None = None

class Se(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem] | None = None

class Sg(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem] | None = None

class Si(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem] | None = None

class Sk(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]

class Th(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem] | None = None

class Tr(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    flatrate: list[FlatrateItem] | None = None
    rent: list[RentItem] | None = None

class Tw(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem] | None = None

class Tz(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]

class Ua(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]

class Us(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    ads: list[Ad] | None = None
    flatrate: list[FlatrateItem] | None = None

class Ve(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem] | None = None

class Ad3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Ae(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]
    rent: list[RentItem]
    buy: list[BuyItem]

class Ag(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Ao(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]

class Az(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]

class Bb(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Bf(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]

class Bh(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Bs(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Do(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Dz(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Eg(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]
    rent: list[RentItem]
    buy: list[BuyItem]

class Fj(BaseModel):
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

class Gy(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Hr(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]

class In(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]

class Iq(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Jm(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Jo(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Jp(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]

class Kr(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]
    buy: list[BuyItem]
    rent: list[RentItem]

class Lb(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Lc(BaseModel):
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

class Mc(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Ml(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]

class Mt(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Om(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Pa(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Pf(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Pg(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]
    rent: list[RentItem]

class Pk(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Qa(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Ro(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]

class Ad4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logo_path: str
    provider_id: int
    provider_name: str
    display_priority: int

class Ru(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    ads: list[Ad4]

class Sa(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]

class Sm(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Sv(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Tc(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Tn(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Tt(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Ug(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]

class Uy(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Va(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Za(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]

class Zw(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]

class Results(BaseModel):
    model_config = ConfigDict(defer_build=True)
    ar: Ar = Field(..., alias='AR')
    at: At = Field(..., alias='AT')
    au: Au = Field(..., alias='AU')
    be: Be = Field(..., alias='BE')
    bg: Bg = Field(..., alias='BG')
    bo: Bo = Field(..., alias='BO')
    br: Br = Field(..., alias='BR')
    by: By = Field(..., alias='BY')
    bz: Bz = Field(..., alias='BZ')
    ca: Ca = Field(..., alias='CA')
    ch: Ch = Field(..., alias='CH')
    cl: Cl = Field(..., alias='CL')
    co: Co = Field(..., alias='CO')
    cr: Cr = Field(..., alias='CR')
    cv: Cv = Field(..., alias='CV')
    cz: Cz = Field(..., alias='CZ')
    de: De = Field(..., alias='DE')
    dk: Dk = Field(..., alias='DK')
    ec: Ec = Field(..., alias='EC')
    ee: Ee = Field(..., alias='EE')
    es: Es = Field(..., alias='ES')
    fi: Fi = Field(..., alias='FI')
    fr: Fr = Field(..., alias='FR')
    gb: Gb = Field(..., alias='GB')
    gg: Gg = Field(..., alias='GG')
    gr: Gr | None = Field(None, alias='GR')
    gt: Gt = Field(..., alias='GT')
    hk: Hk = Field(..., alias='HK')
    hn: Hn = Field(..., alias='HN')
    hu: Hu = Field(..., alias='HU')
    id: Id = Field(..., alias='ID')
    ie: Ie = Field(..., alias='IE')
    il: Il = Field(..., alias='IL')
    is_: Is = Field(..., alias='IS')
    it: It = Field(..., alias='IT')
    lt: Lt = Field(..., alias='LT')
    lu: Lu = Field(..., alias='LU')
    lv: Lv = Field(..., alias='LV')
    mu: Mu = Field(..., alias='MU')
    mx: Mx = Field(..., alias='MX')
    my: My = Field(..., alias='MY')
    mz: Mz = Field(..., alias='MZ')
    ni: Ni = Field(..., alias='NI')
    nl: Nl = Field(..., alias='NL')
    no: No = Field(..., alias='NO')
    nz: Nz = Field(..., alias='NZ')
    pe: Pe = Field(..., alias='PE')
    ph: Ph = Field(..., alias='PH')
    pl: Pl = Field(..., alias='PL')
    pt: Pt = Field(..., alias='PT')
    py: Py = Field(..., alias='PY')
    se: Se = Field(..., alias='SE')
    sg: Sg = Field(..., alias='SG')
    si: Si = Field(..., alias='SI')
    sk: Sk = Field(..., alias='SK')
    th: Th = Field(..., alias='TH')
    tr: Tr = Field(..., alias='TR')
    tw: Tw = Field(..., alias='TW')
    tz: Tz = Field(..., alias='TZ')
    ua: Ua = Field(..., alias='UA')
    us: Us = Field(..., alias='US')
    ve: Ve = Field(..., alias='VE')
    ad: Ad3 | None = Field(None, alias='AD')
    ae: Ae | None = Field(None, alias='AE')
    ag: Ag | None = Field(None, alias='AG')
    ao: Ao | None = Field(None, alias='AO')
    az: Az | None = Field(None, alias='AZ')
    bb: Bb | None = Field(None, alias='BB')
    bf: Bf | None = Field(None, alias='BF')
    bh: Bh | None = Field(None, alias='BH')
    bs: Bs | None = Field(None, alias='BS')
    do: Do | None = Field(None, alias='DO')
    dz: Dz | None = Field(None, alias='DZ')
    eg: Eg | None = Field(None, alias='EG')
    fj: Fj | None = Field(None, alias='FJ')
    gf: Gf | None = Field(None, alias='GF')
    gi: Gi | None = Field(None, alias='GI')
    gy: Gy | None = Field(None, alias='GY')
    hr: Hr | None = Field(None, alias='HR')
    in_: In | None = Field(None, alias='IN')
    iq: Iq | None = Field(None, alias='IQ')
    jm: Jm | None = Field(None, alias='JM')
    jo: Jo | None = Field(None, alias='JO')
    jp: Jp | None = Field(None, alias='JP')
    kr: Kr | None = Field(None, alias='KR')
    lb: Lb | None = Field(None, alias='LB')
    lc: Lc | None = Field(None, alias='LC')
    li: Li | None = Field(None, alias='LI')
    ly: Ly | None = Field(None, alias='LY')
    ma: Ma | None = Field(None, alias='MA')
    mc: Mc | None = Field(None, alias='MC')
    ml: Ml | None = Field(None, alias='ML')
    mt: Mt | None = Field(None, alias='MT')
    om: Om | None = Field(None, alias='OM')
    pa: Pa | None = Field(None, alias='PA')
    pf: Pf | None = Field(None, alias='PF')
    pg: Pg | None = Field(None, alias='PG')
    pk: Pk | None = Field(None, alias='PK')
    qa: Qa | None = Field(None, alias='QA')
    ro: Ro | None = Field(None, alias='RO')
    ru: Ru | None = Field(None, alias='RU')
    sa: Sa | None = Field(None, alias='SA')
    sm: Sm | None = Field(None, alias='SM')
    sv: Sv | None = Field(None, alias='SV')
    tc: Tc | None = Field(None, alias='TC')
    tn: Tn | None = Field(None, alias='TN')
    tt: Tt | None = Field(None, alias='TT')
    ug: Ug | None = Field(None, alias='UG')
    uy: Uy | None = Field(None, alias='UY')
    va: Va | None = Field(None, alias='VA')
    za: Za | None = Field(None, alias='ZA')
    zw: Zw | None = Field(None, alias='ZW')

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
