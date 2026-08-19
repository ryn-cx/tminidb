# TODO: Validate
from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING

from tests.utils import record_test, recorded_content
from tminidb.tv_seasons.changes import TvSeasonChanges
from tminidb.tv_seasons.changes.models import Item, Change, TvSeasonChangeLog

if TYPE_CHECKING:
    from tminidb import TMiniDB

# The window is asked for by name rather than left to default to the last 24
# hours, so re-recording a fixture years from now asks for the same days and
# gets the same answer instead of whatever happened yesterday.
START_DATE = date(2026, 8, 10)
END_DATE = date(2026, 8, 18)


# TODO: Validate
class TestEditedRecently:
    # A season that had been edited inside the window.
    SEASON_ID = 364732
    NAME = "364732"

    # TODO: Validate
    def test_download(self, client: TMiniDB) -> None:
        record_test(
            TvSeasonChanges,
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
        data = recorded_content(TvSeasonChanges, self.NAME)

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
class TestUnknownSeason:
    # An id that belongs to no season. It is answered with an empty list
    # rather than with an error, which is the same answer a season nobody
    # touched gives, so an empty log says nothing about whether the id was good.
    SEASON_ID = 999999999
    NAME = "unknown_999999999"

    # TODO: Validate
    def test_download(self, client: TMiniDB) -> None:
        record_test(
            TvSeasonChanges,
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
        data = recorded_content(TvSeasonChanges, self.NAME)

        assert TvSeasonChangeLog.from_response(data) == TvSeasonChangeLog(
            changes=(),
            raw=data,
        )
