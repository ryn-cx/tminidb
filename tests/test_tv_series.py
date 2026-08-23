# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import RecordedEndpoint
from tminidb.details.tv_series.models import TvSeriesModel
from tminidb.exceptions import SeriesNotFoundError

if TYPE_CHECKING:
    from tminidb import TMiniDB

SERIES_IDS = [
    pytest.param(1, id="pilot, the lowest series id there is"),
    pytest.param(1396, id="breaking bad"),
    pytest.param(53787, id="series with specials"),
]


# TODO: Validate
class TvSeriesTest(RecordedEndpoint):
    MODEL = TvSeriesModel


# TODO: Validate
@pytest.mark.parametrize("series_id", SERIES_IDS)
def test_download(client: TMiniDB, series_id: int) -> None:
    TvSeriesTest.download_test(series_id, lambda: client.tv_series.download(series_id))


# TODO: Validate
@pytest.mark.parametrize("series_id", SERIES_IDS)
def test_parse(client: TMiniDB, series_id: int) -> None:
    series = client.tv_series.load(TvSeriesTest.recorded_content(series_id))
    assert series.id == series_id


# TODO: Validate
@pytest.mark.parametrize(
    "series_id",
    [pytest.param(999999999, id="series that does not exist")],
)
def test_download_invalid(client: TMiniDB, series_id: int) -> None:
    TvSeriesTest.error_test(
        series_id,
        lambda: client.tv_series.download(series_id),
        SeriesNotFoundError,
    )
