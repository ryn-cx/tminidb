# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import RecordedEndpoint
from tminidb.exceptions import EpisodeGroupNotFoundError
from tminidb.tv_episode_group.models import TvEpisodeGroupModel

if TYPE_CHECKING:
    from tminidb import TMiniDB

EPISODE_GROUP_IDS = [
    pytest.param("5e9077d2e640d600151f32bd", id="group with a network"),
    pytest.param("69f50757054263b7bc87e32a", id="group without a network"),
]


# TODO: Validate
class TvEpisodeGroupTest(RecordedEndpoint):
    MODEL = TvEpisodeGroupModel


# TODO: Validate
@pytest.mark.parametrize("episode_group_id", EPISODE_GROUP_IDS)
def test_download(client: TMiniDB, episode_group_id: str) -> None:
    TvEpisodeGroupTest.download_test(
        episode_group_id,
        lambda: client.tv_episode_group.download(episode_group_id),
    )


# TODO: Validate
@pytest.mark.parametrize("episode_group_id", EPISODE_GROUP_IDS)
def test_parse(client: TMiniDB, episode_group_id: str) -> None:
    episode_group = client.tv_episode_group.load(
        TvEpisodeGroupTest.recorded_content(episode_group_id),
    )
    assert episode_group.id == episode_group_id


# TODO: Validate
@pytest.mark.parametrize(
    "episode_group_id",
    [pytest.param("000000000000000000000000", id="episode group that does not exist")],
)
def test_download_invalid(client: TMiniDB, episode_group_id: str) -> None:
    TvEpisodeGroupTest.error_test(
        episode_group_id,
        lambda: client.tv_episode_group.download(episode_group_id),
        EpisodeGroupNotFoundError,
    )
