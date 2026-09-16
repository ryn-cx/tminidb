# TODO: Validate
from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from tminidb import TMiniDB

WINDOWS = [
    pytest.param(7434652, None, id="episode edited recently"),
    pytest.param(999999999, None, id="episode id no episode has"),
]
"""One window the API answers in a single request."""

RANGES = [
    pytest.param(
        7434652,
        date(2026, 7, 22),
        date(2026, 8, 18),
        id="four weeks of an episode",
    ),
]
"""A range walked 14 days at a time and merged into one file."""


# TODO: Validate
@pytest.mark.parametrize(("episode_id", "start_date"), WINDOWS)
def test_download(client: TMiniDB, episode_id: int, start_date: date | None) -> None:
    change_log = client.tv_episode.changes(episode_id, start_date=start_date)
    assert change_log.changes is not None


# TODO: Validate
@pytest.mark.parametrize(("episode_id", "start_date", "end_date"), RANGES)
def test_download_merged(
    client: TMiniDB,
    episode_id: int,
    start_date: date,
    end_date: date,
) -> None:
    merged = client.tv_episode.changes.download_merged(episode_id, start_date, end_date)
    assert client.tv_episode.changes.load(merged).changes is not None
