# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import record_test, recorded_content
from tminidb.exceptions import HTTPError
from tminidb.tv_seasons.details import TvSeasonDetails
from tminidb.tv_seasons.details.models import Episode, TvSeason

if TYPE_CHECKING:
    from tminidb import TMiniDB


# TODO: Validate
class TestSeason:
    SERIES_ID = 1396
    SEASON_NUMBER = 1
    NAME = "1396_1"
    SEASON_ID = 3572
    AIR_DATE = "2008-01-20"

    # TODO: Validate
    def test_download(self, client: TMiniDB) -> None:
        record_test(
            TvSeasonDetails,
            self.NAME,
            lambda: (
                client.tv_seasons.details(
                    self.SERIES_ID,
                    self.SEASON_NUMBER,
                ).raw
            ),
        )

    # TODO: Validate
    def test_parse(self) -> None:
        # The whole of what the response is read into, in one comparison. The
        # season's own identity is written out; the episode rows are read back
        # from the response, since their summaries and runtimes are edited on
        # TMDB long after the season finished airing.
        data = recorded_content(TvSeasonDetails, self.NAME)

        assert TvSeason.from_response(data) == TvSeason(
            object_id=data["_id"],
            air_date=self.AIR_DATE,
            episodes=tuple(Episode(**episode) for episode in data["episodes"]),
            name="Season 1",
            overview=data["overview"],
            id=self.SEASON_ID,
            poster_path=data["poster_path"],
            season_number=self.SEASON_NUMBER,
            vote_average=data["vote_average"],
            raw=data,
        )


# TODO: Validate
class TestUnknownSeries:
    SERIES_ID = 999999999
    SEASON_NUMBER = 1

    # TODO: Validate
    def test_download(self, client: TMiniDB) -> None:
        # A season of a series that does not exist is refused rather than
        # answered with an empty season, so there is no response to record.
        with pytest.raises(HTTPError) as error:
            client.tv_seasons.details(self.SERIES_ID, self.SEASON_NUMBER)

        assert error.value.status_code == 404  # noqa: PLR2004
        assert error.value.response["success"] is False


# TODO: Validate
class TestUnknownSeason:
    SERIES_ID = 1396
    SEASON_NUMBER = 99

    # TODO: Validate
    def test_download(self, client: TMiniDB) -> None:
        # A season number a real series does not have is refused the same way
        # an unknown series is, so a bad number cannot be told from a bad
        # series by the answer alone.
        with pytest.raises(HTTPError) as error:
            client.tv_seasons.details(self.SERIES_ID, self.SEASON_NUMBER)

        assert error.value.status_code == 404  # noqa: PLR2004
