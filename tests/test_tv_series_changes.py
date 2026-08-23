# TODO: Validate
from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING

import pytest

from tests.utils import RecordedEndpoint
from tminidb.changes.tv_series.models import TvSeriesChangesModel

if TYPE_CHECKING:
    from tminidb import TMiniDB

CHANGE_LOGS = [
    pytest.param(
        "108978_with_changes",
        108978,
        date(2026, 8, 18),
        None,
        id="one window of a series that was edited",
    ),
    pytest.param(
        "108978_merged",
        108978,
        date(2026, 7, 22),
        date(2026, 8, 18),
        id="four weeks of a series that was edited",
    ),
    pytest.param(
        "108978_without_changes",
        108978,
        date(2026, 1, 1),
        date(2026, 1, 1),
        id="a day the series was not edited on",
    ),
    pytest.param(
        "2147483647",
        2147483647,
        None,
        None,
        id="the highest series id, which no series has",
    ),
]
"""What is recorded for this endpoint: the name, the id, and the range asked for.

A range with no end is one window the API answers in a single request; a range
with both ends is walked 14 days at a time and merged into one file.
"""


RECORDED_NAMES = [
    pytest.param(change_log.values[0], id=change_log.id) for change_log in CHANGE_LOGS
]
"""Just the name of each recording, for the tests that only read one back."""


# TODO: Validate
class TvSeriesChangesTest(RecordedEndpoint):
    MODEL = TvSeriesChangesModel


# TODO: Validate
def download_change_log(
    client: TMiniDB,
    series_id: int,
    start_date: date | None,
    end_date: date | None,
) -> str:
    """Download the change log the way the range asked for needs it downloaded."""
    if start_date is not None and end_date is not None:
        return client.tv_series_changes.download_merged(series_id, start_date, end_date)
    return client.tv_series_changes.download(series_id, start_date=start_date)


# TODO: Validate
@pytest.mark.parametrize(
    ("name", "series_id", "start_date", "end_date"),
    CHANGE_LOGS,
)
def test_download(
    client: TMiniDB,
    name: str,
    series_id: int,
    start_date: date | None,
    end_date: date | None,
) -> None:
    TvSeriesChangesTest.download_test(
        name,
        lambda: download_change_log(client, series_id, start_date, end_date),
    )


# TODO: Validate
@pytest.mark.parametrize("name", RECORDED_NAMES)
def test_parse(client: TMiniDB, name: str) -> None:
    change_log = client.tv_series_changes.load(
        TvSeriesChangesTest.recorded_content(name),
    )
    assert change_log.changes is not None
