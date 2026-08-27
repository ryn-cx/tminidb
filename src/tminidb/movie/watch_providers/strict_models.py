from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import BaseModel, Field

class FlatrateItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logo_path: str
    provider_id: int
    provider_name: str
    display_priority: int

class Ad(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

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

class Ar(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]
    rent: list[RentItem]

class At(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]
    rent: list[RentItem]

class Au(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]
    rent: list[RentItem]
    buy: list[BuyItem]

class Az(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]

class Bb(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Be(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem]

class Bf(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]

class Bg(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]

class Bh(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Bo(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem]

class Br(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]
    rent: list[RentItem]

class Bs(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class By(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]

class Bz(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    flatrate: list[FlatrateItem]
    buy: list[BuyItem]

class Ad1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logo_path: str
    provider_id: int
    provider_name: str
    display_priority: int

class Ca(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    ads: list[Ad1]
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]

class Ch(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]
    rent: list[RentItem]

class Cl(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem]

class Co(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]

class Cr(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]
    rent: list[RentItem]

class Cv(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]

class Cz(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem]

class De(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem]

class Dk(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]
    rent: list[RentItem]
    buy: list[BuyItem]

class Do(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Dz(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Ec(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]

class Ee(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]

class Eg(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]
    rent: list[RentItem]
    buy: list[BuyItem]

class Es(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]
    rent: list[RentItem]
    buy: list[BuyItem]

class Fi(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem]

class Fj(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Fr(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]
    rent: list[RentItem]

class Gb(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]
    buy: list[BuyItem]
    rent: list[RentItem]

class Gf(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Gg(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]

class Gi(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Gt(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]
    rent: list[RentItem]
    buy: list[BuyItem]

class Gy(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Hk(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]
    buy: list[BuyItem]
    rent: list[RentItem]

class Hn(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    flatrate: list[FlatrateItem]
    buy: list[BuyItem]

class Hr(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]

class Hu(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]

class Id(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]
    buy: list[BuyItem]
    rent: list[RentItem]

class Ie(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]
    buy: list[BuyItem]
    rent: list[RentItem]

class Il(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]
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

class Is(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]
    rent: list[RentItem]

class It(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]
    buy: list[BuyItem]
    rent: list[RentItem]

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

class Lt(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]
    rent: list[RentItem]
    buy: list[BuyItem]

class Lu(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]
    rent: list[RentItem]
    buy: list[BuyItem]

class Lv(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
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

class Mu(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]

class Mx(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]
    buy: list[BuyItem]
    rent: list[RentItem]

class My(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]
    rent: list[RentItem]

class Mz(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]

class Ni(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]
    rent: list[RentItem]
    buy: list[BuyItem]

class Nl(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]
    rent: list[RentItem]
    buy: list[BuyItem]

class No(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]

class Nz(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    ads: list[Ad1]
    flatrate: list[FlatrateItem]
    buy: list[BuyItem]

class Om(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Pa(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Pe(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
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

class Ph(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]
    rent: list[RentItem]
    buy: list[BuyItem]

class Pk(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Pl(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem]

class Pt(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]

class Py(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]
    rent: list[RentItem]
    buy: list[BuyItem]

class Qa(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Ro(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]

class Ru(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    ads: list[Ad1]

class Sa(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]

class Se(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem]

class Sg(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem]

class Si(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]

class Sk(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]

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

class Th(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem]

class Tn(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Tr(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]
    buy: list[BuyItem]
    rent: list[RentItem]

class Tt(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Tw(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]
    buy: list[BuyItem]
    rent: list[RentItem]

class Tz(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]

class Ua(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]

class Ug(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]

class Us(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    rent: list[RentItem]
    flatrate: list[FlatrateItem]
    buy: list[BuyItem]

class Uy(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Va(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]

class Ve(BaseModel):
    model_config = ConfigDict(defer_build=True)
    link: str
    flatrate: list[FlatrateItem]
    buy: list[BuyItem]
    rent: list[RentItem]

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
    ad: Ad = Field(..., alias='AD')
    ae: Ae = Field(..., alias='AE')
    ag: Ag = Field(..., alias='AG')
    ao: Ao = Field(..., alias='AO')
    ar: Ar = Field(..., alias='AR')
    at: At = Field(..., alias='AT')
    au: Au = Field(..., alias='AU')
    az: Az = Field(..., alias='AZ')
    bb: Bb = Field(..., alias='BB')
    be: Be = Field(..., alias='BE')
    bf: Bf = Field(..., alias='BF')
    bg: Bg = Field(..., alias='BG')
    bh: Bh = Field(..., alias='BH')
    bo: Bo = Field(..., alias='BO')
    br: Br = Field(..., alias='BR')
    bs: Bs = Field(..., alias='BS')
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
    do: Do = Field(..., alias='DO')
    dz: Dz = Field(..., alias='DZ')
    ec: Ec = Field(..., alias='EC')
    ee: Ee = Field(..., alias='EE')
    eg: Eg = Field(..., alias='EG')
    es: Es = Field(..., alias='ES')
    fi: Fi = Field(..., alias='FI')
    fj: Fj = Field(..., alias='FJ')
    fr: Fr = Field(..., alias='FR')
    gb: Gb = Field(..., alias='GB')
    gf: Gf = Field(..., alias='GF')
    gg: Gg = Field(..., alias='GG')
    gi: Gi = Field(..., alias='GI')
    gt: Gt = Field(..., alias='GT')
    gy: Gy = Field(..., alias='GY')
    hk: Hk = Field(..., alias='HK')
    hn: Hn = Field(..., alias='HN')
    hr: Hr = Field(..., alias='HR')
    hu: Hu = Field(..., alias='HU')
    id: Id = Field(..., alias='ID')
    ie: Ie = Field(..., alias='IE')
    il: Il = Field(..., alias='IL')
    in_: In = Field(..., alias='IN')
    iq: Iq = Field(..., alias='IQ')
    is_: Is = Field(..., alias='IS')
    it: It = Field(..., alias='IT')
    jm: Jm = Field(..., alias='JM')
    jo: Jo = Field(..., alias='JO')
    jp: Jp = Field(..., alias='JP')
    kr: Kr = Field(..., alias='KR')
    lb: Lb = Field(..., alias='LB')
    lc: Lc = Field(..., alias='LC')
    li: Li = Field(..., alias='LI')
    lt: Lt = Field(..., alias='LT')
    lu: Lu = Field(..., alias='LU')
    lv: Lv = Field(..., alias='LV')
    ly: Ly = Field(..., alias='LY')
    ma: Ma = Field(..., alias='MA')
    mc: Mc = Field(..., alias='MC')
    ml: Ml = Field(..., alias='ML')
    mt: Mt = Field(..., alias='MT')
    mu: Mu = Field(..., alias='MU')
    mx: Mx = Field(..., alias='MX')
    my: My = Field(..., alias='MY')
    mz: Mz = Field(..., alias='MZ')
    ni: Ni = Field(..., alias='NI')
    nl: Nl = Field(..., alias='NL')
    no: No = Field(..., alias='NO')
    nz: Nz = Field(..., alias='NZ')
    om: Om = Field(..., alias='OM')
    pa: Pa = Field(..., alias='PA')
    pe: Pe = Field(..., alias='PE')
    pf: Pf = Field(..., alias='PF')
    pg: Pg = Field(..., alias='PG')
    ph: Ph = Field(..., alias='PH')
    pk: Pk = Field(..., alias='PK')
    pl: Pl = Field(..., alias='PL')
    pt: Pt = Field(..., alias='PT')
    py: Py = Field(..., alias='PY')
    qa: Qa = Field(..., alias='QA')
    ro: Ro = Field(..., alias='RO')
    ru: Ru = Field(..., alias='RU')
    sa: Sa = Field(..., alias='SA')
    se: Se = Field(..., alias='SE')
    sg: Sg = Field(..., alias='SG')
    si: Si = Field(..., alias='SI')
    sk: Sk = Field(..., alias='SK')
    sm: Sm = Field(..., alias='SM')
    sv: Sv = Field(..., alias='SV')
    tc: Tc = Field(..., alias='TC')
    th: Th = Field(..., alias='TH')
    tn: Tn = Field(..., alias='TN')
    tr: Tr = Field(..., alias='TR')
    tt: Tt = Field(..., alias='TT')
    tw: Tw = Field(..., alias='TW')
    tz: Tz = Field(..., alias='TZ')
    ua: Ua = Field(..., alias='UA')
    ug: Ug = Field(..., alias='UG')
    us: Us = Field(..., alias='US')
    uy: Uy = Field(..., alias='UY')
    va: Va = Field(..., alias='VA')
    ve: Ve = Field(..., alias='VE')
    za: Za = Field(..., alias='ZA')
    zw: Zw = Field(..., alias='ZW')

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
