# TODO: Validate
"""Every endpoint the API's docs file under TV Seasons."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING

import pytest

from tests.utils import RecordedEndpoint
from tminidb.exceptions import HTTPError
from tminidb.tv_seasons import TvSeasonEndpoints
from tminidb.tv_seasons.models.changes import Change, Item, TvSeasonChangeLog
from tminidb.tv_seasons.models.details import Episode, TvSeason

if TYPE_CHECKING:
    from tminidb import TMiniDB

# The window is asked for by name rather than left to default to the last 24
# hours, so re-recording a fixture years from now asks for the same days and
# gets the same answer instead of whatever happened yesterday.
START_DATE = date(2026, 8, 10)
END_DATE = date(2026, 8, 18)


# TODO: Validate
class TvSeasonTest(RecordedEndpoint):
    ENDPOINT = TvSeasonEndpoints


# TODO: Validate
class TestChanges:
    """Test `tv_seasons.changes`."""

    # TODO: Validate
    class TestEditedRecently(TvSeasonTest):
        # A season that had been edited inside the window.
        SEASON_ID = 364732
        NAME = "364732"

        # TODO: Validate
        def test_download(self, client: TMiniDB) -> None:
            self.record_test(
                self.NAME,
                lambda: (
                    client.tv_seasons.changes(
                        self.SEASON_ID,
                        start_date=START_DATE,
                        end_date=END_DATE,
                    ).raw
                ),
            )

        # TODO: Validate
        def test_parse(self) -> None:
            # The whole of what the response is read into, in one comparison. Which
            # fields were edited and how many times is whatever the editors did
            # that fortnight, so the rows are read back from the response: what is
            # checked is that every group and every edit inside it is carried over,
            # in order, and that an edit keeps the id, action and time that make it
            # readable.
            data = self.recorded_content(self.NAME)

            assert TvSeasonChangeLog.from_response(data) == TvSeasonChangeLog(
                changes=tuple(
                    Change(
                        key=group["key"],
                        items=tuple(Item(**item) for item in group["items"]),
                    )
                    for group in data["changes"]
                ),
                raw=data,
            )
            assert TvSeasonChangeLog.from_response(data).changes

    # TODO: Validate
    class TestUnknownSeason(TvSeasonTest):
        # An id that belongs to no season. It is answered with an empty list
        # rather than with an error, which is the same answer a season nobody
        # touched gives, so an empty log says nothing about whether the id was good.
        SEASON_ID = 999999999
        NAME = "unknown_999999999"

        # TODO: Validate
        def test_download(self, client: TMiniDB) -> None:
            self.record_test(
                self.NAME,
                lambda: (
                    client.tv_seasons.changes(
                        self.SEASON_ID,
                        start_date=START_DATE,
                        end_date=END_DATE,
                    ).raw
                ),
            )

        # TODO: Validate
        def test_parse(self) -> None:
            self.parse_test(self.NAME, TvSeasonChangeLog)


# TODO: Validate
class TestDetails:
    """Test `tv_seasons.details`."""

    # TODO: Validate
    class TestSeason(TvSeasonTest):
        SERIES_ID = 1396
        SEASON_NUMBER = 1
        NAME = "1396_1"
        SEASON_ID = 3572
        AIR_DATE = "2008-01-20"

        # TODO: Validate
        def test_download(self, client: TMiniDB) -> None:
            self.record_test(
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
            data = self.recorded_content(self.NAME)

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
            assert error.value.response.json()["success"] is False

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
