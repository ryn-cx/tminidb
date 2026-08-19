# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import record_test, recorded_content
from tminidb.exceptions import HTTPError
from tminidb.tv_series.details import TvSeriesDetails
from tminidb.tv_series.details.models import (
    Creator,
    EpisodeSummary,
    Genre,
    Network,
    ProductionCompany,
    ProductionCountry,
    Season,
    SpokenLanguage,
    TvSeries,
)

if TYPE_CHECKING:
    from tminidb import TMiniDB


# TODO: Validate
class TestFinishedSeries:
    SERIES_ID = 1396
    NAME = "Breaking Bad"
    FIRST_AIR_DATE = "2008-01-20"
    LAST_AIR_DATE = "2013-09-29"
    SEASONS = 5
    EPISODES = 62

    # TODO: Validate
    def test_download(self, client: TMiniDB) -> None:
        record_test(
            TvSeriesDetails,
            str(self.SERIES_ID),
            lambda: client.tv_series.details(self.SERIES_ID).raw,
        )

    # TODO: Validate
    def test_parse(self) -> None:
        # The whole of what the response is read into, in one comparison. The
        # series is finished, so its counts and dates are written out; the
        # season rows are read back from the response, since TMDB adds and
        # renames specials on even a closed show.
        data = recorded_content(TvSeriesDetails, str(self.SERIES_ID))

        assert TvSeries.from_response(data) == TvSeries(
            id=self.SERIES_ID,
            name=self.NAME,
            original_name=self.NAME,
            original_language="en",
            first_air_date=self.FIRST_AIR_DATE,
            last_air_date=self.LAST_AIR_DATE,
            in_production=False,
            status="Ended",
            number_of_seasons=self.SEASONS,
            number_of_episodes=self.EPISODES,
            overview=data["overview"],
            seasons=tuple(Season(**season) for season in data["seasons"]),
            adult=data["adult"],
            backdrop_path=data["backdrop_path"],
            created_by=tuple(Creator(**person) for person in data["created_by"]),
            episode_run_time=tuple(data["episode_run_time"]),
            genres=tuple(Genre(**genre) for genre in data["genres"]),
            homepage=data["homepage"],
            languages=tuple(data["languages"]),
            networks=tuple(Network(**network) for network in data["networks"]),
            origin_country=tuple(data["origin_country"]),
            popularity=data["popularity"],
            poster_path=data["poster_path"],
            production_companies=tuple(
                ProductionCompany(**company) for company in data["production_companies"]
            ),
            production_countries=tuple(
                ProductionCountry(**country) for country in data["production_countries"]
            ),
            spoken_languages=tuple(
                SpokenLanguage(**language) for language in data["spoken_languages"]
            ),
            tagline=data["tagline"],
            type=data["type"],
            vote_average=data["vote_average"],
            vote_count=data["vote_count"],
            last_episode_to_air=EpisodeSummary(**data["last_episode_to_air"]),
            next_episode_to_air=(
                None
                if data["next_episode_to_air"] is None
                else EpisodeSummary(**data["next_episode_to_air"])
            ),
            raw=data,
        )


# TODO: Validate
class TestSeriesWithSpecials:
    # A series whose season list starts at zero, so the specials season, which
    # is the one that breaks any assumption that season numbers start at one,
    # is covered.
    SERIES_ID = 53787

    # TODO: Validate
    def test_download(self, client: TMiniDB) -> None:
        record_test(
            TvSeriesDetails,
            str(self.SERIES_ID),
            lambda: client.tv_series.details(self.SERIES_ID).raw,
        )

    # TODO: Validate
    def test_parse(self) -> None:
        data = recorded_content(TvSeriesDetails, str(self.SERIES_ID))

        assert TvSeries.from_response(data) == TvSeries(
            id=self.SERIES_ID,
            name=data["name"],
            original_name=data["original_name"],
            original_language=data["original_language"],
            first_air_date=data["first_air_date"],
            last_air_date=data["last_air_date"],
            in_production=data["in_production"],
            status=data["status"],
            number_of_seasons=data["number_of_seasons"],
            number_of_episodes=data["number_of_episodes"],
            overview=data["overview"],
            seasons=tuple(Season(**season) for season in data["seasons"]),
            adult=data["adult"],
            backdrop_path=data["backdrop_path"],
            created_by=tuple(Creator(**person) for person in data["created_by"]),
            episode_run_time=tuple(data["episode_run_time"]),
            genres=tuple(Genre(**genre) for genre in data["genres"]),
            homepage=data["homepage"],
            languages=tuple(data["languages"]),
            networks=tuple(Network(**network) for network in data["networks"]),
            origin_country=tuple(data["origin_country"]),
            popularity=data["popularity"],
            poster_path=data["poster_path"],
            production_companies=tuple(
                ProductionCompany(**company) for company in data["production_companies"]
            ),
            production_countries=tuple(
                ProductionCountry(**country) for country in data["production_countries"]
            ),
            spoken_languages=tuple(
                SpokenLanguage(**language) for language in data["spoken_languages"]
            ),
            tagline=data["tagline"],
            type=data["type"],
            vote_average=data["vote_average"],
            vote_count=data["vote_count"],
            last_episode_to_air=EpisodeSummary(**data["last_episode_to_air"]),
            next_episode_to_air=(
                None
                if data["next_episode_to_air"] is None
                else EpisodeSummary(**data["next_episode_to_air"])
            ),
            raw=data,
        )
        assert TvSeries.from_response(data).seasons[0].season_number == 0


# TODO: Validate
class TestUnknownSeries:
    SERIES_ID = 999999999

    # TODO: Validate
    def test_download(self, client: TMiniDB) -> None:
        # An id that belongs to no series is refused rather than answered with
        # an empty series, so there is no response to record.
        with pytest.raises(HTTPError) as error:
            client.tv_series.details(self.SERIES_ID)

        assert error.value.status_code == 404  # noqa: PLR2004
        assert error.value.response["success"] is False
