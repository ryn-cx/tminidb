from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING

import pytest

from tests.utils import parse_test, record_test, recorded_content
from tminidb.exceptions import HTTPError
from tminidb.tv_series.changes import TvSeriesChanges
from tminidb.tv_series.changes.models import TvSeriesChangeLog

if TYPE_CHECKING:
    from tminidb import TMiniDB

# Most popular TV series at the time of writing this test
# https://www.themoviedb.org/tv/108978-reacher
SERIES_ID = 108978


class TestResponseWithChanges:
    def test_download(self, client: TMiniDB) -> None:
        record_test(
            TvSeriesChanges,
            str(SERIES_ID),
            lambda: (
                client.tv_series.changes(
                    SERIES_ID,
                    start_date=date(2026, 8, 18),
                ).raw
            ),
        )

    def test_parse(self) -> None:
        parse_test(TvSeriesChanges, str(SERIES_ID), TvSeriesChangeLog)


class TestMergedResponseWithChanges:
    def test_download(self, client: TMiniDB) -> None:
        record_test(
            TvSeriesChanges,
            str(SERIES_ID),
            lambda: (
                client.tv_series.changes(
                    SERIES_ID,
                    start_date=date(2026, 7, 22),
                    end_date=date(2026, 8, 18),
                ).raw
            ),
        )

    def test_parse(self) -> None:
        parse_test(TvSeriesChanges, str(SERIES_ID), TvSeriesChangeLog)


class TestResponseWithoutChanges:
    def test_download(self, client: TMiniDB) -> None:
        record_test(
            TvSeriesChanges,
            str(SERIES_ID),
            lambda: (
                client.tv_series.changes(
                    SERIES_ID,
                    start_date=date(2026, 1, 1),
                    end_date=date(2026, 1, 1),
                ).raw
            ),
        )

    def test_parse(self) -> None:
        data = recorded_content(TvSeriesChanges, str(SERIES_ID))

        assert TvSeriesChangeLog.from_response(data) == TvSeriesChangeLog(
            changes=(),
            raw=data,
        )


class TestInvalidSeriesID:
    """Values between -2147483648 and 0 return a 404 error."""
    SERIES_ID = 0

    def test_download(self, client: TMiniDB) -> None:
        with pytest.raises(HTTPError) as error:
            client.tv_series.changes(self.SERIES_ID)

        assert error.value.status_code == 404  # noqa: PLR2004
        assert error.value.response["success"] is False


class TestUnusedSeriesID:
    SERIES_ID = 2147483647

    # TODO: Validate
    def test_download(self, client: TMiniDB) -> None:
        record_test(
            TvSeriesChanges,
            str(self.SERIES_ID),
            lambda: client.tv_series.changes(self.SERIES_ID).raw,
        )

    # TODO: Validate
    def test_parse(self) -> None:
        data = recorded_content(TvSeriesChanges, str(self.SERIES_ID))

        assert TvSeriesChangeLog.from_response(data) == TvSeriesChangeLog(
            changes=(),
            raw=data,
        )
