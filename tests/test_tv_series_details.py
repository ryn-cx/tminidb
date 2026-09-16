# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tminidb.exceptions import SeriesNotFoundError

if TYPE_CHECKING:
    from tminidb import TMiniDB

SERIES_IDS = [
    pytest.param(1, id="pilot, the lowest series id there is"),
    pytest.param(1396, id="breaking bad"),
    pytest.param(53787, id="series with specials"),
]


# TODO: Validate
@pytest.mark.parametrize("series_id", SERIES_IDS)
def test_download(client: TMiniDB, series_id: int) -> None:
    series = client.tv_series.details(series_id)
    assert series.id == series_id


# TODO: Validate
def test_download_invalid(client: TMiniDB) -> None:
    with pytest.raises(SeriesNotFoundError):
        client.tv_series.details.download(999999999)
