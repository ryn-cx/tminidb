from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, Field

class FlatrateItem(BaseModel):
    logo_path: str
    provider_id: int
    provider_name: str
    display_priority: int

class Ad(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Ae(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Ag(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Al(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Ao(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Ar(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class BuyItem(BaseModel):
    logo_path: str
    provider_id: int
    provider_name: str
    display_priority: int

class At(BaseModel):
    link: str
    flatrate: list[FlatrateItem]
    buy: list[BuyItem]

class Au(BaseModel):
    link: str
    flatrate: list[FlatrateItem]
    buy: list[BuyItem]

class Az(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Ba(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Bb(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Be(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Bg(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Bh(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Bo(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Br(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Bs(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class By(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Bz(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Ca(BaseModel):
    link: str
    flatrate: list[FlatrateItem]
    buy: list[BuyItem]

class Ch(BaseModel):
    link: str
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]

class Ci(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Cl(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Cm(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Co(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Cr(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Cu(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Cv(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Cy(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Cz(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class De(BaseModel):
    link: str
    flatrate: list[FlatrateItem]
    buy: list[BuyItem]

class RentItem(BaseModel):
    logo_path: str
    provider_id: int
    provider_name: str
    display_priority: int

class Dk(BaseModel):
    link: str
    rent: list[RentItem]
    flatrate: list[FlatrateItem]
    buy: list[BuyItem]

class Do(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Dz(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Ec(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Ee(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Eg(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Es(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Fi(BaseModel):
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem]

class Fj(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Fr(BaseModel):
    link: str
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]

class Gb(BaseModel):
    link: str
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]

class Gf(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Gg(BaseModel):
    link: str
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]

class Gh(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Gq(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Gr(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Gt(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Hk(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Hn(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Hu(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Id(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Ie(BaseModel):
    link: str
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]

class Il(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class In(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Iq(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Is(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class It(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Jm(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Jo(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class FreeItem(BaseModel):
    logo_path: str
    provider_id: int
    provider_name: str
    display_priority: int

class Jp(BaseModel):
    link: str
    free: list[FreeItem]
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem]

class Ke(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Kr(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Kw(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Lb(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Lc(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Li(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Lt(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Lu(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Lv(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Ly(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Ma(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Mc(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Me(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Mg(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Mk(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Ml(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Mt(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Mu(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Mx(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class My(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Mz(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Ne(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Ng(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Ni(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Nl(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class No(BaseModel):
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]

class Nz(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Om(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Pa(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Pe(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Pf(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Ph(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Pk(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Pl(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Pt(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Py(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Qa(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Ro(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Rs(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Ad1(BaseModel):
    logo_path: str
    provider_id: int
    provider_name: str
    display_priority: int

class Ru(BaseModel):
    link: str
    ads: list[Ad1]

class Sa(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Sc(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Se(BaseModel):
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem]

class Sg(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Si(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Sk(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Sm(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Sn(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Sv(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Tc(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Td(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Th(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Tn(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Tr(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Tt(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Tw(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Tz(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Ug(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Us(BaseModel):
    link: str
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]

class Uy(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Ve(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Ye(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Za(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Zm(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Zw(BaseModel):
    link: str
    flatrate: list[FlatrateItem]

class Results(BaseModel):
    ad: Ad = Field(..., alias='AD')
    ae: Ae = Field(..., alias='AE')
    ag: Ag = Field(..., alias='AG')
    al: Al = Field(..., alias='AL')
    ao: Ao = Field(..., alias='AO')
    ar: Ar = Field(..., alias='AR')
    at: At = Field(..., alias='AT')
    au: Au = Field(..., alias='AU')
    az: Az = Field(..., alias='AZ')
    ba: Ba = Field(..., alias='BA')
    bb: Bb = Field(..., alias='BB')
    be: Be = Field(..., alias='BE')
    bg: Bg = Field(..., alias='BG')
    bh: Bh = Field(..., alias='BH')
    bo: Bo = Field(..., alias='BO')
    br: Br = Field(..., alias='BR')
    bs: Bs = Field(..., alias='BS')
    by: By = Field(..., alias='BY')
    bz: Bz = Field(..., alias='BZ')
    ca: Ca = Field(..., alias='CA')
    ch: Ch = Field(..., alias='CH')
    ci: Ci = Field(..., alias='CI')
    cl: Cl = Field(..., alias='CL')
    cm: Cm = Field(..., alias='CM')
    co: Co = Field(..., alias='CO')
    cr: Cr = Field(..., alias='CR')
    cu: Cu = Field(..., alias='CU')
    cv: Cv = Field(..., alias='CV')
    cy: Cy = Field(..., alias='CY')
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
    gh: Gh = Field(..., alias='GH')
    gq: Gq = Field(..., alias='GQ')
    gr: Gr = Field(..., alias='GR')
    gt: Gt = Field(..., alias='GT')
    hk: Hk = Field(..., alias='HK')
    hn: Hn = Field(..., alias='HN')
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
    ke: Ke = Field(..., alias='KE')
    kr: Kr = Field(..., alias='KR')
    kw: Kw = Field(..., alias='KW')
    lb: Lb = Field(..., alias='LB')
    lc: Lc = Field(..., alias='LC')
    li: Li = Field(..., alias='LI')
    lt: Lt = Field(..., alias='LT')
    lu: Lu = Field(..., alias='LU')
    lv: Lv = Field(..., alias='LV')
    ly: Ly = Field(..., alias='LY')
    ma: Ma = Field(..., alias='MA')
    mc: Mc = Field(..., alias='MC')
    me: Me = Field(..., alias='ME')
    mg: Mg = Field(..., alias='MG')
    mk: Mk = Field(..., alias='MK')
    ml: Ml = Field(..., alias='ML')
    mt: Mt = Field(..., alias='MT')
    mu: Mu = Field(..., alias='MU')
    mx: Mx = Field(..., alias='MX')
    my: My = Field(..., alias='MY')
    mz: Mz = Field(..., alias='MZ')
    ne: Ne = Field(..., alias='NE')
    ng: Ng = Field(..., alias='NG')
    ni: Ni = Field(..., alias='NI')
    nl: Nl = Field(..., alias='NL')
    no: No = Field(..., alias='NO')
    nz: Nz = Field(..., alias='NZ')
    om: Om = Field(..., alias='OM')
    pa: Pa = Field(..., alias='PA')
    pe: Pe = Field(..., alias='PE')
    pf: Pf = Field(..., alias='PF')
    ph: Ph = Field(..., alias='PH')
    pk: Pk = Field(..., alias='PK')
    pl: Pl = Field(..., alias='PL')
    pt: Pt = Field(..., alias='PT')
    py: Py = Field(..., alias='PY')
    qa: Qa = Field(..., alias='QA')
    ro: Ro = Field(..., alias='RO')
    rs: Rs = Field(..., alias='RS')
    ru: Ru = Field(..., alias='RU')
    sa: Sa = Field(..., alias='SA')
    sc: Sc = Field(..., alias='SC')
    se: Se = Field(..., alias='SE')
    sg: Sg = Field(..., alias='SG')
    si: Si = Field(..., alias='SI')
    sk: Sk = Field(..., alias='SK')
    sm: Sm = Field(..., alias='SM')
    sn: Sn = Field(..., alias='SN')
    sv: Sv = Field(..., alias='SV')
    tc: Tc = Field(..., alias='TC')
    td: Td = Field(..., alias='TD')
    th: Th = Field(..., alias='TH')
    tn: Tn = Field(..., alias='TN')
    tr: Tr = Field(..., alias='TR')
    tt: Tt = Field(..., alias='TT')
    tw: Tw = Field(..., alias='TW')
    tz: Tz = Field(..., alias='TZ')
    ug: Ug = Field(..., alias='UG')
    us: Us = Field(..., alias='US')
    uy: Uy = Field(..., alias='UY')
    ve: Ve = Field(..., alias='VE')
    ye: Ye = Field(..., alias='YE')
    za: Za = Field(..., alias='ZA')
    zm: Zm = Field(..., alias='ZM')
    zw: Zw = Field(..., alias='ZW')

class TvSeriesWatchProvidersModel(BaseModel):
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
