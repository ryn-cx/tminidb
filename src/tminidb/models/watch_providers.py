# TODO: Validate

from __future__ import annotations

from typing import Any, Self

from pydantic import BaseModel, ConfigDict, Field, SkipValidation


# TODO: Validate
class Provider(BaseModel):
    model_config = ConfigDict(frozen=True)

    logo_path: str
    provider_id: int
    provider_name: str
    display_priority: int


# TODO: Validate
class CountryProviders(BaseModel):
    model_config = ConfigDict(frozen=True)

    link: str
    flatrate: tuple[Provider, ...] = ()
    free: tuple[Provider, ...] = ()
    ads: tuple[Provider, ...] = ()
    rent: tuple[Provider, ...] = ()
    buy: tuple[Provider, ...] = ()


# TODO: Validate
class Results(BaseModel):
    model_config = ConfigDict(frozen=True)

    AD: CountryProviders | None = None
    AE: CountryProviders | None = None
    AG: CountryProviders | None = None
    AL: CountryProviders | None = None
    AO: CountryProviders | None = None
    AR: CountryProviders | None = None
    AT: CountryProviders | None = None
    AU: CountryProviders | None = None
    AZ: CountryProviders | None = None
    BA: CountryProviders | None = None
    BB: CountryProviders | None = None
    BE: CountryProviders | None = None
    BF: CountryProviders | None = None
    BG: CountryProviders | None = None
    BH: CountryProviders | None = None
    BM: CountryProviders | None = None
    BO: CountryProviders | None = None
    BR: CountryProviders | None = None
    BS: CountryProviders | None = None
    BY: CountryProviders | None = None
    BZ: CountryProviders | None = None
    CA: CountryProviders | None = None
    CH: CountryProviders | None = None
    CI: CountryProviders | None = None
    CL: CountryProviders | None = None
    CM: CountryProviders | None = None
    CO: CountryProviders | None = None
    CR: CountryProviders | None = None
    CU: CountryProviders | None = None
    CV: CountryProviders | None = None
    CY: CountryProviders | None = None
    CZ: CountryProviders | None = None
    DE: CountryProviders | None = None
    DK: CountryProviders | None = None
    DO: CountryProviders | None = None
    DZ: CountryProviders | None = None
    EC: CountryProviders | None = None
    EE: CountryProviders | None = None
    EG: CountryProviders | None = None
    ES: CountryProviders | None = None
    FI: CountryProviders | None = None
    FJ: CountryProviders | None = None
    FR: CountryProviders | None = None
    GB: CountryProviders | None = None
    GF: CountryProviders | None = None
    GG: CountryProviders | None = None
    GH: CountryProviders | None = None
    GI: CountryProviders | None = None
    GP: CountryProviders | None = None
    GQ: CountryProviders | None = None
    GR: CountryProviders | None = None
    GT: CountryProviders | None = None
    GY: CountryProviders | None = None
    HK: CountryProviders | None = None
    HN: CountryProviders | None = None
    HR: CountryProviders | None = None
    HU: CountryProviders | None = None
    ID: CountryProviders | None = None
    IE: CountryProviders | None = None
    IL: CountryProviders | None = None
    IN: CountryProviders | None = None
    IQ: CountryProviders | None = None
    IS: CountryProviders | None = None
    IT: CountryProviders | None = None
    JM: CountryProviders | None = None
    JO: CountryProviders | None = None
    JP: CountryProviders | None = None
    KE: CountryProviders | None = None
    KR: CountryProviders | None = None
    KW: CountryProviders | None = None
    LB: CountryProviders | None = None
    LC: CountryProviders | None = None
    LI: CountryProviders | None = None
    LT: CountryProviders | None = None
    LU: CountryProviders | None = None
    LV: CountryProviders | None = None
    LY: CountryProviders | None = None
    MA: CountryProviders | None = None
    MC: CountryProviders | None = None
    MD: CountryProviders | None = None
    ME: CountryProviders | None = None
    MG: CountryProviders | None = None
    MK: CountryProviders | None = None
    ML: CountryProviders | None = None
    MT: CountryProviders | None = None
    MU: CountryProviders | None = None
    MX: CountryProviders | None = None
    MY: CountryProviders | None = None
    MZ: CountryProviders | None = None
    NE: CountryProviders | None = None
    NG: CountryProviders | None = None
    NI: CountryProviders | None = None
    NL: CountryProviders | None = None
    NO: CountryProviders | None = None
    NZ: CountryProviders | None = None
    OM: CountryProviders | None = None
    PA: CountryProviders | None = None
    PE: CountryProviders | None = None
    PF: CountryProviders | None = None
    PG: CountryProviders | None = None
    PH: CountryProviders | None = None
    PK: CountryProviders | None = None
    PL: CountryProviders | None = None
    PS: CountryProviders | None = None
    PT: CountryProviders | None = None
    PY: CountryProviders | None = None
    QA: CountryProviders | None = None
    RO: CountryProviders | None = None
    RS: CountryProviders | None = None
    RU: CountryProviders | None = None
    SA: CountryProviders | None = None
    SC: CountryProviders | None = None
    SE: CountryProviders | None = None
    SG: CountryProviders | None = None
    SI: CountryProviders | None = None
    SK: CountryProviders | None = None
    SM: CountryProviders | None = None
    SN: CountryProviders | None = None
    SV: CountryProviders | None = None
    TC: CountryProviders | None = None
    TD: CountryProviders | None = None
    TH: CountryProviders | None = None
    TN: CountryProviders | None = None
    TR: CountryProviders | None = None
    TT: CountryProviders | None = None
    TW: CountryProviders | None = None
    TZ: CountryProviders | None = None
    UA: CountryProviders | None = None
    UG: CountryProviders | None = None
    US: CountryProviders | None = None
    UY: CountryProviders | None = None
    VA: CountryProviders | None = None
    VE: CountryProviders | None = None
    XK: CountryProviders | None = None
    YE: CountryProviders | None = None
    ZA: CountryProviders | None = None
    ZM: CountryProviders | None = None
    ZW: CountryProviders | None = None


# TODO: Validate
class WatchProviders(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: int
    results: Results
    raw: SkipValidation[dict[str, Any]] = Field(repr=False)

    # TODO: Validate
    @classmethod
    def from_response(cls, data: dict[str, Any]) -> Self:
        return cls.model_validate({**data, "raw": data})
