# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import RecordedEndpoint
from tminidb.exceptions import SeriesNotFoundError
from tminidb.tv_series.images.models import TvSeriesImagesModel

if TYPE_CHECKING:
    from tminidb import TMiniDB

SERIES_IDS = [
    pytest.param(1396, id="breaking bad"),
    pytest.param(37854, id="one piece"),
]


# TODO: Validate
class TvSeriesImagesTest(RecordedEndpoint):
    MODEL = TvSeriesImagesModel


# TODO: Validate
@pytest.mark.parametrize("series_id", SERIES_IDS)
def test_download(client: TMiniDB, series_id: int) -> None:
    TvSeriesImagesTest.download_test(
        series_id,
        lambda: client.tv_series.images.download(series_id),
    )


# TODO: Validate
@pytest.mark.parametrize("series_id", SERIES_IDS)
def test_parse(client: TMiniDB, series_id: int) -> None:
    images = client.tv_series.images.load(
        TvSeriesImagesTest.recorded_content(series_id),
    )
    assert images.id == series_id


# TODO: Validate
@pytest.mark.parametrize(
    "series_id",
    [pytest.param(999999999, id="series that does not exist")],
)
def test_download_invalid(client: TMiniDB, series_id: int) -> None:
    TvSeriesImagesTest.error_test(
        series_id,
        lambda: client.tv_series.images.download(series_id),
        SeriesNotFoundError,
    )
