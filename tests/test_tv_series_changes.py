# TODO: Validate
from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from tminidb import TMiniDB

WINDOWS = [
    pytest.param(108978, date(2026, 8, 18), id="a series that was edited"),
    pytest.param(2147483647, None, id="the highest series id, which no series has"),
]
"""One window the API answers in a single request."""

RANGES = [
    pytest.param(
        108978,
        date(2026, 7, 22),
        date(2026, 8, 18),
        id="four weeks of a series that was edited",
    ),
    pytest.param(
        108978,
        date(2026, 1, 1),
        date(2026, 1, 1),
        id="a day the series was not edited on",
    ),
]
"""A range walked 14 days at a time and merged into one file."""


# TODO: Validate
@pytest.mark.parametrize(("series_id", "start_date"), WINDOWS)
def test_download(client: TMiniDB, series_id: int, start_date: date | None) -> None:
    change_log = client.tv_series.changes(series_id, start_date=start_date)
    assert change_log.changes is not None


# TODO: Validate
@pytest.mark.parametrize(("series_id", "start_date", "end_date"), RANGES)
def test_download_merged(
    client: TMiniDB,
    series_id: int,
    start_date: date,
    end_date: date,
) -> None:
    merged = client.tv_series.changes.download_merged(series_id, start_date, end_date)
    assert client.tv_series.changes.load(merged).changes is not None
