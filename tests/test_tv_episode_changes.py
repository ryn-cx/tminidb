# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import RecordedEndpoint
from tminidb.tv_episode.changes.models import TvEpisodeChangesModel

if TYPE_CHECKING:
    from datetime import date

    from tminidb import TMiniDB

CHANGE_LOGS = [
    pytest.param("7434652", 7434652, None, None, id="episode edited recently"),
    pytest.param(
        "unknown_999999999",
        999999999,
        None,
        None,
        id="episode id no episode has",
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
class TvEpisodeChangesTest(RecordedEndpoint):
    MODEL = TvEpisodeChangesModel


# TODO: Validate
def download_change_log(
    client: TMiniDB,
    episode_id: int,
    start_date: date | None,
    end_date: date | None,
) -> str:
    """Download the change log the way the range asked for needs it downloaded."""
    if start_date is not None and end_date is not None:
        return client.tv_episode.changes.download_merged(
            episode_id,
            start_date,
            end_date,
        )
    return client.tv_episode.changes.download(episode_id, start_date=start_date)


# TODO: Validate
@pytest.mark.parametrize(
    ("name", "episode_id", "start_date", "end_date"),
    CHANGE_LOGS,
)
def test_download(
    client: TMiniDB,
    name: str,
    episode_id: int,
    start_date: date | None,
    end_date: date | None,
) -> None:
    TvEpisodeChangesTest.download_test(
        name,
        lambda: download_change_log(client, episode_id, start_date, end_date),
    )


# TODO: Validate
@pytest.mark.parametrize("name", RECORDED_NAMES)
def test_parse(client: TMiniDB, name: str) -> None:
    change_log = client.tv_episode.changes.load(
        TvEpisodeChangesTest.recorded_content(name),
    )
    assert change_log.changes is not None
