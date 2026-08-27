# TODO: Validate
from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING

import pytest

from tests.utils import RecordedEndpoint
from tminidb.movie.changes.models import MovieChangesModel

if TYPE_CHECKING:
    from tminidb import TMiniDB

CHANGE_LOGS = [
    pytest.param(
        "969681_with_changes",
        969681,
        date(2026, 8, 18),
        None,
        id="one window of a movie that was edited",
    ),
    pytest.param(
        "969681_merged",
        969681,
        date(2026, 7, 22),
        date(2026, 8, 18),
        id="four weeks of a movie that was edited",
    ),
    pytest.param(
        "969681_without_changes",
        969681,
        date(2026, 1, 1),
        date(2026, 1, 1),
        id="a day the movie was not edited on",
    ),
    pytest.param(
        "2147483647",
        2147483647,
        None,
        None,
        id="the highest movie id, which no movie has",
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
class MovieChangesTest(RecordedEndpoint):
    MODEL = MovieChangesModel


# TODO: Validate
def download_change_log(
    client: TMiniDB,
    movie_id: int,
    start_date: date | None,
    end_date: date | None,
) -> str:
    """Download the change log the way the range asked for needs it downloaded."""
    if start_date is not None and end_date is not None:
        return client.movie.changes.download_merged(movie_id, start_date, end_date)
    return client.movie.changes.download(movie_id, start_date=start_date)


# TODO: Validate
@pytest.mark.parametrize(
    ("name", "movie_id", "start_date", "end_date"),
    CHANGE_LOGS,
)
def test_download(
    client: TMiniDB,
    name: str,
    movie_id: int,
    start_date: date | None,
    end_date: date | None,
) -> None:
    MovieChangesTest.download_test(
        name,
        lambda: download_change_log(client, movie_id, start_date, end_date),
    )


# TODO: Validate
@pytest.mark.parametrize("name", RECORDED_NAMES)
def test_parse(client: TMiniDB, name: str) -> None:
    change_log = client.movie.changes.load(MovieChangesTest.recorded_content(name))
    assert change_log.changes is not None
