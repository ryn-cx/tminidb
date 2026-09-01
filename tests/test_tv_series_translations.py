# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import RecordedEndpoint
from tminidb.exceptions import SeriesNotFoundError
from tminidb.tv_series.translations.models import TvSeriesTranslationsModel

if TYPE_CHECKING:
    from tminidb import TMiniDB

SERIES_IDS = [
    pytest.param(1396, id="breaking bad"),
    pytest.param(37854, id="one piece"),
]


# TODO: Validate
class TvSeriesTranslationsTest(RecordedEndpoint):
    MODEL = TvSeriesTranslationsModel


# TODO: Validate
@pytest.mark.parametrize("series_id", SERIES_IDS)
def test_download(client: TMiniDB, series_id: int) -> None:
    TvSeriesTranslationsTest.download_test(
        series_id,
        lambda: client.tv_series.translations.download(series_id),
    )


# TODO: Validate
@pytest.mark.parametrize("series_id", SERIES_IDS)
def test_parse(client: TMiniDB, series_id: int) -> None:
    translations = client.tv_series.translations.load(
        TvSeriesTranslationsTest.recorded_content(series_id),
    )
    assert translations.id == series_id
    assert translations.translations


# TODO: Validate
@pytest.mark.parametrize(
    "series_id",
    [pytest.param(999999999, id="series that does not exist")],
)
def test_download_invalid(client: TMiniDB, series_id: int) -> None:
    TvSeriesTranslationsTest.error_test(
        series_id,
        lambda: client.tv_series.translations.download(series_id),
        SeriesNotFoundError,
    )
