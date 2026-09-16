# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tminidb.exceptions import EpisodeNotFoundError

if TYPE_CHECKING:
    from tminidb import TMiniDB

EPISODES = [pytest.param(1396, 1, 1, id="breaking bad season 1 episode 1")]


# TODO: Validate
@pytest.mark.parametrize(("series_id", "season_number", "episode_number"), EPISODES)
def test_download(
    client: TMiniDB,
    series_id: int,
    season_number: int,
    episode_number: int,
) -> None:
    translations = client.tv_episode.translations(
        series_id,
        season_number,
        episode_number,
    )
    assert translations.translations


# TODO: Validate
def test_download_invalid(client: TMiniDB) -> None:
    with pytest.raises(EpisodeNotFoundError):
        client.tv_episode.translations.download(1396, 1, 999)
