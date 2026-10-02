# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tminidb.exceptions import SeriesNotFoundError

if TYPE_CHECKING:
    from tminidb import TMiniDB

SERIES_IDS = [
    pytest.param(2316, "tt0386676", id="the office"),
    pytest.param(1396, "tt0903747", id="breaking bad"),
]


# TODO: Validate
@pytest.mark.parametrize(("series_id", "imdb_id"), SERIES_IDS)
def test_download(client: TMiniDB, series_id: int, imdb_id: str) -> None:
    external_ids = client.tv_series.external_ids(series_id)
    assert external_ids.id == series_id
    assert external_ids.imdb_id == imdb_id


# TODO: Validate
def test_download_invalid(client: TMiniDB) -> None:
    with pytest.raises(SeriesNotFoundError):
        client.tv_series.external_ids.download(999999999)
