# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tminidb.exceptions import SeriesNotFoundError

if TYPE_CHECKING:
    from tminidb import TMiniDB

SERIES_IDS = [
    pytest.param(1416, id="grey's anatomy"),
    pytest.param(37854, id="one piece"),
]


# TODO: Validate
@pytest.mark.parametrize("series_id", SERIES_IDS)
def test_download(client: TMiniDB, series_id: int) -> None:
    episode_groups = client.tv_series.episode_groups(series_id)
    assert episode_groups.id == series_id


# TODO: Validate
def test_download_invalid(client: TMiniDB) -> None:
    with pytest.raises(SeriesNotFoundError):
        client.tv_series.episode_groups.download(999999999)
