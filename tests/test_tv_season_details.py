# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tminidb.exceptions import SeasonNotFoundError

if TYPE_CHECKING:
    from tminidb import TMiniDB

SEASONS = [pytest.param(1396, 1, id="breaking bad season 1")]


# TODO: Validate
@pytest.mark.parametrize(("series_id", "season_number"), SEASONS)
def test_download(client: TMiniDB, series_id: int, season_number: int) -> None:
    season = client.tv_season.details(series_id, season_number)
    assert season.season_number == season_number


# TODO: Validate
def test_download_invalid(client: TMiniDB) -> None:
    with pytest.raises(SeasonNotFoundError):
        client.tv_season.details.download(1396, 999)
