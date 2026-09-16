# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tminidb.exceptions import EpisodeGroupNotFoundError

if TYPE_CHECKING:
    from tminidb import TMiniDB

EPISODE_GROUP_IDS = [
    pytest.param("5e9077d2e640d600151f32bd", id="group with a network"),
    pytest.param("69f50757054263b7bc87e32a", id="group without a network"),
]


# TODO: Validate
@pytest.mark.parametrize("episode_group_id", EPISODE_GROUP_IDS)
def test_download(client: TMiniDB, episode_group_id: str) -> None:
    episode_group = client.tv_episode_group.details(episode_group_id)
    assert episode_group.id == episode_group_id


# TODO: Validate
def test_download_invalid(client: TMiniDB) -> None:
    with pytest.raises(EpisodeGroupNotFoundError):
        client.tv_episode_group.details.download("000000000000000000000000")
