# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import assert_error, download_and_save, parse_json_to_model
from tminidb.exceptions import HTTPError

if TYPE_CHECKING:
    from tminidb import TMiniDB
    from tminidb.tv_watch_providers import TvWatchProviders

SERIES_ID = 1396
INVALID_SERIES_ID = 999999999


@pytest.fixture(scope="session")
def endpoint(client: TMiniDB) -> TvWatchProviders:
    return client.tv_watch_providers


class TestTvWatchProviders:
    def test_download(self, endpoint: TvWatchProviders) -> None:
        download_and_save(
            endpoint,
            str(SERIES_ID),
            lambda: endpoint.download(SERIES_ID),
        )

    def test_parse(self, endpoint: TvWatchProviders) -> None:
        data = parse_json_to_model(endpoint, str(SERIES_ID))
        assert data is not None

    def test_invalid_download(self, endpoint: TvWatchProviders) -> None:
        assert_error(
            endpoint,
            str(INVALID_SERIES_ID),
            lambda: endpoint.download(INVALID_SERIES_ID),
            HTTPError,
        )
