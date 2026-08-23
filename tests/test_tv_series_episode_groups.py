# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import RecordedEndpoint
from tminidb.exceptions import SeriesNotFoundError
from tminidb.tv_series_episode_groups.models import TvSeriesEpisodeGroupsModel

if TYPE_CHECKING:
    from tminidb import TMiniDB

SERIES_IDS = [
    pytest.param(1416, id="grey's anatomy"),
    pytest.param(37854, id="one piece"),
]


# TODO: Validate
class TvSeriesEpisodeGroupsTest(RecordedEndpoint):
    MODEL = TvSeriesEpisodeGroupsModel


# TODO: Validate
@pytest.mark.parametrize("series_id", SERIES_IDS)
def test_download(client: TMiniDB, series_id: int) -> None:
    TvSeriesEpisodeGroupsTest.download_test(
        series_id,
        lambda: client.tv_series_episode_groups.download(series_id),
    )


# TODO: Validate
@pytest.mark.parametrize("series_id", SERIES_IDS)
def test_parse(client: TMiniDB, series_id: int) -> None:
    episode_groups = client.tv_series_episode_groups.load(
        TvSeriesEpisodeGroupsTest.recorded_content(series_id),
    )
    assert episode_groups.id == series_id


# TODO: Validate
@pytest.mark.parametrize(
    "series_id",
    [pytest.param(999999999, id="series that does not exist")],
)
def test_download_invalid(client: TMiniDB, series_id: int) -> None:
    TvSeriesEpisodeGroupsTest.error_test(
        series_id,
        lambda: client.tv_series_episode_groups.download(series_id),
        SeriesNotFoundError,
    )
