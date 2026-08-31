# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import RecordedEndpoint
from tminidb.exceptions import SeasonNotFoundError
from tminidb.tv_season.watch_providers.models import TvSeasonWatchProvidersModel

if TYPE_CHECKING:
    from tminidb import TMiniDB

SEASONS = [pytest.param(1396, 1, id="breaking bad season 1")]


# TODO: Validate
class TvSeasonWatchProvidersTest(RecordedEndpoint):
    MODEL = TvSeasonWatchProvidersModel


# TODO: Validate
@pytest.mark.parametrize(("series_id", "season_number"), SEASONS)
def test_download(client: TMiniDB, series_id: int, season_number: int) -> None:
    TvSeasonWatchProvidersTest.download_test(
        f"{series_id}_{season_number}",
        lambda: client.tv_season.watch_providers.download(series_id, season_number),
    )


# TODO: Validate
@pytest.mark.parametrize(("series_id", "season_number"), SEASONS)
def test_parse(client: TMiniDB, series_id: int, season_number: int) -> None:
    providers = client.tv_season.watch_providers.load(
        TvSeasonWatchProvidersTest.recorded_content(f"{series_id}_{season_number}"),
    )
    # The file carries the season's own id, so the series id is not in it to check.
    assert providers.id
    assert providers.results


# TODO: Validate
@pytest.mark.parametrize(
    ("series_id", "season_number"),
    [pytest.param(1396, 999, id="season the series does not have")],
)
def test_download_invalid(client: TMiniDB, series_id: int, season_number: int) -> None:
    TvSeasonWatchProvidersTest.error_test(
        f"{series_id}_{season_number}",
        lambda: client.tv_season.watch_providers.download(series_id, season_number),
        SeasonNotFoundError,
    )
