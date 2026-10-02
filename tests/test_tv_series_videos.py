# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tminidb.exceptions import SeriesNotFoundError

if TYPE_CHECKING:
    from tminidb import TMiniDB

IDS = [
    pytest.param(2316, id="the office"),
    pytest.param(1396, id="breaking bad"),
]


# TODO: Validate
@pytest.mark.parametrize("series_id", IDS)
def test_download(client: TMiniDB, series_id: int) -> None:
    videos = client.tv_series.videos(series_id)
    assert videos.id == series_id
    assert videos.results


# TODO: Validate
def test_download_invalid(client: TMiniDB) -> None:
    with pytest.raises(SeriesNotFoundError):
        client.tv_series.videos.download(999999999)
