# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import assert_error, download_and_save, parse_json_to_model
from tminidb.exceptions import HTTPError

if TYPE_CHECKING:
    from tminidb import TMiniDB
    from tminidb.tv_episode_details import TvEpisodeDetails

SERIES_ID = 1396
SEASON_NUMBER = 1
EPISODE_NUMBER = 1
NAME = f"{SERIES_ID}_{SEASON_NUMBER}_{EPISODE_NUMBER}"
INVALID_SERIES_ID = 999999999
INVALID_NAME = f"{INVALID_SERIES_ID}_{SEASON_NUMBER}_{EPISODE_NUMBER}"


@pytest.fixture(scope="session")
def endpoint(client: TMiniDB) -> TvEpisodeDetails:
    return client.tv_episode_details


class TestTvEpisodeDetails:
    def test_download(self, endpoint: TvEpisodeDetails) -> None:
        download_and_save(
            endpoint,
            NAME,
            lambda: endpoint.download(SERIES_ID, SEASON_NUMBER, EPISODE_NUMBER),
        )

    def test_parse(self, endpoint: TvEpisodeDetails) -> None:
        data = parse_json_to_model(endpoint, NAME)
        assert data is not None

    def test_invalid_download(self, endpoint: TvEpisodeDetails) -> None:
        assert_error(
            endpoint,
            INVALID_NAME,
            lambda: endpoint.download(INVALID_SERIES_ID, SEASON_NUMBER, EPISODE_NUMBER),
            HTTPError,
        )
