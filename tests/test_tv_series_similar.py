# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tminidb.exceptions import SeriesNotFoundError

if TYPE_CHECKING:
    from tminidb import TMiniDB

SECOND_PAGE = 2

SERIES_IDS = [
    pytest.param(1396, id="breaking bad"),
    pytest.param(1790, id="family feud"),
]


# TODO: Validate
@pytest.mark.parametrize("series_id", SERIES_IDS)
def test_download(client: TMiniDB, series_id: int) -> None:
    similar = client.tv_series.similar(series_id)
    assert similar.page == 1
    assert similar.results


# TODO: Validate
def test_download_page(client: TMiniDB) -> None:
    assert client.tv_series.similar(1396, page=SECOND_PAGE).page == SECOND_PAGE


# TODO: Validate
def test_download_invalid(client: TMiniDB) -> None:
    with pytest.raises(SeriesNotFoundError):
        client.tv_series.similar.download(999999999)
