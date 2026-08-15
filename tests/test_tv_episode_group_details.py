# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import assert_error, download_and_save, parse_json_to_model
from tminidb.exceptions import HTTPError

if TYPE_CHECKING:
    from tminidb import TMiniDB
    from tminidb.tv_episode_group_details import TvEpisodeGroupDetails

EPISODE_GROUP_IDS = (
    # `DVD / PVOD` for Breaking Bad, which has no network.
    "69f50757054263b7bc87e32a",
    # `Aired Order` for Game of Thrones, which does have a network, so the two
    # together cover both shapes the field takes.
    "5e9077d2e640d600151f32bd",
)
INVALID_EPISODE_GROUP_ID = "000000000000000000000000"


@pytest.fixture(scope="session")
def endpoint(client: TMiniDB) -> TvEpisodeGroupDetails:
    return client.tv_episode_group_details


@pytest.fixture(params=EPISODE_GROUP_IDS)
def episode_group_id(request: pytest.FixtureRequest) -> str:
    return request.param


class TestTvEpisodeGroupDetails:
    def test_download(
        self,
        endpoint: TvEpisodeGroupDetails,
        episode_group_id: str,
    ) -> None:
        download_and_save(
            endpoint,
            episode_group_id,
            lambda: endpoint.download(episode_group_id),
        )

    def test_parse(
        self,
        endpoint: TvEpisodeGroupDetails,
        episode_group_id: str,
    ) -> None:
        data = parse_json_to_model(endpoint, episode_group_id)
        assert data is not None

    def test_invalid_download(self, endpoint: TvEpisodeGroupDetails) -> None:
        assert_error(
            endpoint,
            INVALID_EPISODE_GROUP_ID,
            lambda: endpoint.download(INVALID_EPISODE_GROUP_ID),
            HTTPError,
        )
