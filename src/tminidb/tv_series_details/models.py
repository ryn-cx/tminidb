from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import ConfigDict
from datetime import date

class CreatedByItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: int
    credit_id: str
    name: str
    original_name: str
    gender: int
    profile_path: str | None

class Genre(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: int
    name: str

class LastEpisodeToAir(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: int
    name: str
    overview: str
    vote_average: float
    vote_count: int
    air_date: date
    episode_number: int
    episode_type: str
    production_code: str
    runtime: int | None
    season_number: int
    show_id: int
    still_path: str | None

class NextEpisodeToAir(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: int
    name: str
    overview: str
    vote_average: float
    vote_count: int
    air_date: date
    episode_number: int
    episode_type: str
    production_code: str
    runtime: int | None
    season_number: int
    show_id: int
    still_path: str | None

class Network(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: int
    logo_path: str
    name: str
    origin_country: str

class ProductionCompany(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: int
    logo_path: str | None
    name: str
    origin_country: str

class ProductionCountry(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    iso_3166_1: str
    name: str

class Season(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    air_date: date | None
    episode_count: int
    id: int
    name: str
    overview: str
    poster_path: str | None
    season_number: int
    vote_average: float

class SpokenLanguage(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    english_name: str
    iso_639_1: str
    name: str

class TvSeriesDetailsModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    adult: bool
    backdrop_path: str
    created_by: list[CreatedByItem]
    episode_run_time: list[int]
    first_air_date: date
    genres: list[Genre]
    homepage: str
    id: int
    in_production: bool
    languages: list[str]
    last_air_date: date
    last_episode_to_air: LastEpisodeToAir
    name: str
    next_episode_to_air: NextEpisodeToAir | None
    networks: list[Network]
    number_of_episodes: int
    number_of_seasons: int
    origin_country: list[str]
    original_language: str
    original_name: str
    overview: str
    popularity: float
    poster_path: str
    production_companies: list[ProductionCompany]
    production_countries: list[ProductionCountry]
    seasons: list[Season]
    softcore: bool
    spoken_languages: list[SpokenLanguage]
    status: str
    tagline: str
    type: str
    vote_average: float
    vote_count: int
