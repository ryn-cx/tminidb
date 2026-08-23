# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import RecordedEndpoint
from tminidb.exceptions import SeriesNotFoundError
from tminidb.watch_providers.tv_series.models import TvSeriesWatchProvidersModel

if TYPE_CHECKING:
    from tminidb import TMiniDB

SERIES_IDS = [
    pytest.param(1396, id="breaking bad"),
]


# TODO: Validate
class TvSeriesWatchProvidersTest(RecordedEndpoint):
    MODEL = TvSeriesWatchProvidersModel


# TODO: Validate
@pytest.mark.parametrize("series_id", SERIES_IDS)
def test_download(client: TMiniDB, series_id: int) -> None:
    TvSeriesWatchProvidersTest.download_test(
        series_id,
        lambda: client.tv_series_watch_providers.download(series_id),
    )


# TODO: Validate
@pytest.mark.parametrize("series_id", SERIES_IDS)
def test_parse(client: TMiniDB, series_id: int) -> None:
    providers = client.tv_series_watch_providers.load(
        TvSeriesWatchProvidersTest.recorded_content(series_id),
    )
    assert providers.id == series_id


# TODO: Validate
@pytest.mark.parametrize(
    "series_id",
    [pytest.param(999999999, id="series that does not exist")],
)
def test_download_invalid(client: TMiniDB, series_id: int) -> None:
    TvSeriesWatchProvidersTest.error_test(
        series_id,
        lambda: client.tv_series_watch_providers.download(series_id),
        SeriesNotFoundError,
    )
