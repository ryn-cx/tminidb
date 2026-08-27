# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import RecordedEndpoint
from tminidb.exceptions import SeasonNotFoundError
from tminidb.tv_season.details.models import TvSeasonDetailsModel

if TYPE_CHECKING:
    from tminidb import TMiniDB

SEASONS = [pytest.param(1396, 1, id="breaking bad season 1")]


# TODO: Validate
class TvSeasonDetailsTest(RecordedEndpoint):
    MODEL = TvSeasonDetailsModel


# TODO: Validate
@pytest.mark.parametrize(("series_id", "season_number"), SEASONS)
def test_download(client: TMiniDB, series_id: int, season_number: int) -> None:
    TvSeasonDetailsTest.download_test(
        f"{series_id}_{season_number}",
        lambda: client.tv_season.details.download(series_id, season_number),
    )


# TODO: Validate
@pytest.mark.parametrize(("series_id", "season_number"), SEASONS)
def test_parse(client: TMiniDB, series_id: int, season_number: int) -> None:
    season = client.tv_season.details.load(
        TvSeasonDetailsTest.recorded_content(f"{series_id}_{season_number}"),
    )
    assert season.season_number == season_number


# TODO: Validate
@pytest.mark.parametrize(
    ("series_id", "season_number"),
    [pytest.param(1396, 999, id="season the series does not have")],
)
def test_download_invalid(client: TMiniDB, series_id: int, season_number: int) -> None:
    TvSeasonDetailsTest.error_test(
        f"{series_id}_{season_number}",
        lambda: client.tv_season.details.download(series_id, season_number),
        SeasonNotFoundError,
    )
