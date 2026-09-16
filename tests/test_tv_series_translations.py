# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tminidb.exceptions import SeriesNotFoundError

if TYPE_CHECKING:
    from tminidb import TMiniDB

SERIES_IDS = [
    pytest.param(1396, id="breaking bad"),
    pytest.param(37854, id="one piece"),
]


# TODO: Validate
@pytest.mark.parametrize("series_id", SERIES_IDS)
def test_download(client: TMiniDB, series_id: int) -> None:
    translations = client.tv_series.translations(series_id)
    assert translations.id == series_id
    assert translations.translations


# TODO: Validate
def test_download_invalid(client: TMiniDB) -> None:
    with pytest.raises(SeriesNotFoundError):
        client.tv_series.translations.download(999999999)
