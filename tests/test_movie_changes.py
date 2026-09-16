# TODO: Validate
from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from tminidb import TMiniDB

WINDOWS = [
    pytest.param(969681, date(2026, 8, 18), id="a movie that was edited"),
    pytest.param(2147483647, None, id="the highest movie id, which no movie has"),
]
"""One window the API answers in a single request."""

RANGES = [
    pytest.param(
        969681,
        date(2026, 7, 22),
        date(2026, 8, 18),
        id="four weeks of a movie that was edited",
    ),
    pytest.param(
        969681,
        date(2026, 1, 1),
        date(2026, 1, 1),
        id="a day the movie was not edited on",
    ),
]
"""A range walked 14 days at a time and merged into one file."""


# TODO: Validate
@pytest.mark.parametrize(("movie_id", "start_date"), WINDOWS)
def test_download(client: TMiniDB, movie_id: int, start_date: date | None) -> None:
    change_log = client.movie.changes(movie_id, start_date=start_date)
    assert change_log.changes is not None


# TODO: Validate
@pytest.mark.parametrize(("movie_id", "start_date", "end_date"), RANGES)
def test_download_merged(
    client: TMiniDB,
    movie_id: int,
    start_date: date,
    end_date: date,
) -> None:
    merged = client.movie.changes.download_merged(movie_id, start_date, end_date)
    assert client.movie.changes.load(merged).changes is not None
