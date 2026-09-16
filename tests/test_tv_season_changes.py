# TODO: Validate
from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from tminidb import TMiniDB

WINDOWS = [
    pytest.param(364732, None, id="season edited recently"),
    pytest.param(999999999, None, id="season id no season has"),
]
"""One window the API answers in a single request."""

RANGES = [
    pytest.param(
        364732,
        date(2026, 7, 22),
        date(2026, 8, 18),
        id="four weeks of a season",
    ),
]
"""A range walked 14 days at a time and merged into one file."""


# TODO: Validate
@pytest.mark.parametrize(("season_id", "start_date"), WINDOWS)
def test_download(client: TMiniDB, season_id: int, start_date: date | None) -> None:
    change_log = client.tv_season.changes(season_id, start_date=start_date)
    assert change_log.changes is not None


# TODO: Validate
@pytest.mark.parametrize(("season_id", "start_date", "end_date"), RANGES)
def test_download_merged(
    client: TMiniDB,
    season_id: int,
    start_date: date,
    end_date: date,
) -> None:
    merged = client.tv_season.changes.download_merged(season_id, start_date, end_date)
    assert client.tv_season.changes.load(merged).changes is not None
