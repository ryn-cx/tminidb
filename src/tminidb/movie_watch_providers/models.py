# TODO: Validate
from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import ConfigDict, Field

class FlatrateItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    logo_path: str
    provider_id: int
    provider_name: str
    display_priority: int

class Ad(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]

class RentItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    logo_path: str
    provider_id: int
    provider_name: str
    display_priority: int

class BuyItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    logo_path: str
    provider_id: int
    provider_name: str
    display_priority: int

class Ae(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]

class Ag(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]

class Ao(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]

class Ar(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]
    rent: list[RentItem]
    buy: list[BuyItem]

class At(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem]

class Au(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]

class Az(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]

class Ba(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]

class Bb(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]

class Be(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem]

class Bf(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]

class Bg(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]
    rent: list[RentItem]
    buy: list[BuyItem]

class Bh(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]

class Bo(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]
    rent: list[RentItem]

class Br(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem]

class Bs(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]

class By(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]

class Bz(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    rent: list[RentItem]
    flatrate: list[FlatrateItem]
    buy: list[BuyItem]

class Ca(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]
    rent: list[RentItem]

class Ch(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]
    buy: list[BuyItem]
    rent: list[RentItem]

class Cl(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    rent: list[RentItem]
    flatrate: list[FlatrateItem]
    buy: list[BuyItem]

class Co(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]

class Cr(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]

class Cv(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]

class Cz(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]
    buy: list[BuyItem]
    rent: list[RentItem]

class De(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]
    buy: list[BuyItem]
    rent: list[RentItem]

class Dk(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem]

class Do(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]

class Dz(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]

class Ec(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    rent: list[RentItem]
    flatrate: list[FlatrateItem]
    buy: list[BuyItem]

class Ee(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]
    buy: list[BuyItem]
    rent: list[RentItem]

class Eg(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]
    rent: list[RentItem]
    buy: list[BuyItem]

class Es(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]
    rent: list[RentItem]
    buy: list[BuyItem]

class Fi(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem]

class Fj(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]

class Fr(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]
    buy: list[BuyItem]
    rent: list[RentItem]

class Gb(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]
    buy: list[BuyItem]
    rent: list[RentItem]

class Gf(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]

class Gg(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]

class Gt(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]
    rent: list[RentItem]

class Gy(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]

class Hk(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]
    rent: list[RentItem]

class Hn(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    rent: list[RentItem]
    flatrate: list[FlatrateItem]
    buy: list[BuyItem]

class Hr(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    rent: list[RentItem]
    flatrate: list[FlatrateItem]
    buy: list[BuyItem]

class Hu(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]

class Id(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]
    rent: list[RentItem]
    buy: list[BuyItem]

class Ie(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]
    rent: list[RentItem]
    buy: list[BuyItem]

class Il(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem]

class In(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]

class Iq(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]

class Is(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]
    rent: list[RentItem]

class It(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem]

class Jm(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]

class Jo(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]

class Jp(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    rent: list[RentItem]
    flatrate: list[FlatrateItem]
    buy: list[BuyItem]

class Kr(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    rent: list[RentItem]
    flatrate: list[FlatrateItem]
    buy: list[BuyItem]

class Lb(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]

class Lc(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]

class Li(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]

class Lt(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem]

class Lu(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]

class Lv(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]
    rent: list[RentItem]

class Ly(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]

class Ma(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]

class Mc(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]

class Md(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]

class Me(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]

class Mk(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]

class Ml(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]

class Mt(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]

class Mu(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]

class Mx(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]

class My(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]

class Mz(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]

class Ni(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]
    buy: list[BuyItem]
    rent: list[RentItem]

class Nl(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]
    buy: list[BuyItem]
    rent: list[RentItem]

class No(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem]

class Ad1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    logo_path: str
    provider_id: int
    provider_name: str
    display_priority: int

class Nz(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    buy: list[BuyItem]
    ads: list[Ad1]
    rent: list[RentItem]
    flatrate: list[FlatrateItem]

class Om(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]

class Pa(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]

class Pe(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]
    rent: list[RentItem]

class Pf(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]

class Pg(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]

class Ph(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]

class Pk(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]

class Pl(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]
    buy: list[BuyItem]
    rent: list[RentItem]

class Pt(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem]

class Py(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]

class Qa(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]

class Ro(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]
    buy: list[BuyItem]
    rent: list[RentItem]

class Rs(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]

class Ru(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    ads: list[Ad1]

class Sa(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    rent: list[RentItem]
    flatrate: list[FlatrateItem]
    buy: list[BuyItem]

class Se(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]
    rent: list[RentItem]

class Sg(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]

class Si(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem]

class Sk(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]

class Sm(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]

class Sv(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]

class Tc(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]

class Th(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]
    buy: list[BuyItem]
    rent: list[RentItem]

class Tn(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]

class Tr(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]
    flatrate: list[FlatrateItem]

class Tt(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]

class Tw(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]
    rent: list[RentItem]
    buy: list[BuyItem]

class Tz(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]

class Ua(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]

class Ug(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]

class Us(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    rent: list[RentItem]
    buy: list[BuyItem]

class Uy(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]

class Va(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    flatrate: list[FlatrateItem]

class Ve(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    buy: list[BuyItem]
    flatrate: list[FlatrateItem]
    rent: list[RentItem]

class Za(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]

class Zw(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    link: str
    buy: list[BuyItem]
    rent: list[RentItem]

class Results(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    ad: Ad = Field(..., alias='AD')
    ae: Ae = Field(..., alias='AE')
    ag: Ag = Field(..., alias='AG')
    ao: Ao = Field(..., alias='AO')
    ar: Ar = Field(..., alias='AR')
    at: At = Field(..., alias='AT')
    au: Au = Field(..., alias='AU')
    az: Az = Field(..., alias='AZ')
    ba: Ba = Field(..., alias='BA')
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
    md: Md = Field(..., alias='MD')
    me: Me = Field(..., alias='ME')
    mk: Mk = Field(..., alias='MK')
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
    rs: Rs = Field(..., alias='RS')
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

class MovieWatchProvidersModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: int
    results: Results
