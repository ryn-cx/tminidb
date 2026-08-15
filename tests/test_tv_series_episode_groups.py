# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import assert_error, download_and_save, parse_json_to_model
from tminidb.exceptions import HTTPError

if TYPE_CHECKING:
    from tminidb import TMiniDB
    from tminidb.tv_series_episode_groups import TvSeriesEpisodeGroups

SERIES_ID = 37854
NAME = str(SERIES_ID)
INVALID_SERIES_ID = 999999999
INVALID_NAME = str(INVALID_SERIES_ID)


@pytest.fixture(scope="session")
def endpoint(client: TMiniDB) -> TvSeriesEpisodeGroups:
    return client.tv_series_episode_groups


class TestTvSeriesEpisodeGroups:
    def test_download(self, endpoint: TvSeriesEpisodeGroups) -> None:
        download_and_save(
            endpoint,
            NAME,
            lambda: endpoint.download(SERIES_ID),
        )

    def test_parse(self, endpoint: TvSeriesEpisodeGroups) -> None:
        data = parse_json_to_model(endpoint, NAME)
        assert data is not None

    def test_invalid_download(self, endpoint: TvSeriesEpisodeGroups) -> None:
        assert_error(
            endpoint,
            INVALID_NAME,
            lambda: endpoint.download(INVALID_SERIES_ID),
            HTTPError,
        )
