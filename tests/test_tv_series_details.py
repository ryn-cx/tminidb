# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import assert_error, download_and_save, parse_json_to_model
from tminidb.exceptions import HTTPError

if TYPE_CHECKING:
    from tminidb import TMiniDB
    from tminidb.tv_series_details import TvSeriesDetails

SERIES_IDS = [
    1396,
    # No creators, a logo-less production company and a specials season.
    53787,
]
INVALID_SERIES_ID = 999999999


@pytest.fixture(scope="session")
def endpoint(client: TMiniDB) -> TvSeriesDetails:
    return client.tv_series_details


@pytest.fixture(params=SERIES_IDS, ids=str)
def series_id(request: pytest.FixtureRequest) -> int:
    return request.param


class TestTvSeriesDetails:
    def test_download(self, endpoint: TvSeriesDetails, series_id: int) -> None:
        download_and_save(
            endpoint,
            str(series_id),
            lambda: endpoint.download(series_id),
        )

    def test_parse(self, endpoint: TvSeriesDetails, series_id: int) -> None:
        data = parse_json_to_model(endpoint, str(series_id))
        assert data is not None

    def test_invalid_download(self, endpoint: TvSeriesDetails) -> None:
        assert_error(
            endpoint,
            str(INVALID_SERIES_ID),
            lambda: endpoint.download(INVALID_SERIES_ID),
            HTTPError,
        )
