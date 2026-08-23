# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import RecordedEndpoint
from tminidb.exceptions import EpisodeNotFoundError
from tminidb.tv_episode_translations.models import TvEpisodeTranslationsModel

if TYPE_CHECKING:
    from tminidb import TMiniDB

EPISODES = [pytest.param(1396, 1, 1, id="breaking bad season 1 episode 1")]


# TODO: Validate
class TvEpisodeTranslationsTest(RecordedEndpoint):
    MODEL = TvEpisodeTranslationsModel


# TODO: Validate
@pytest.mark.parametrize(("series_id", "season_number", "episode_number"), EPISODES)
def test_download(
    client: TMiniDB,
    series_id: int,
    season_number: int,
    episode_number: int,
) -> None:
    TvEpisodeTranslationsTest.download_test(
        f"{series_id}_{season_number}_{episode_number}",
        lambda: client.tv_episode_translations.download(
            series_id,
            season_number,
            episode_number,
        ),
    )


# TODO: Validate
@pytest.mark.parametrize(("series_id", "season_number", "episode_number"), EPISODES)
def test_parse(
    client: TMiniDB,
    series_id: int,
    season_number: int,
    episode_number: int,
) -> None:
    translations = client.tv_episode_translations.load(
        TvEpisodeTranslationsTest.recorded_content(
            f"{series_id}_{season_number}_{episode_number}",
        ),
    )
    assert translations.translations


# TODO: Validate
@pytest.mark.parametrize(
    ("series_id", "season_number", "episode_number"),
    [pytest.param(1396, 1, 999, id="episode the season does not have")],
)
def test_download_invalid(
    client: TMiniDB,
    series_id: int,
    season_number: int,
    episode_number: int,
) -> None:
    TvEpisodeTranslationsTest.error_test(
        f"{series_id}_{season_number}_{episode_number}",
        lambda: client.tv_episode_translations.download(
            series_id,
            season_number,
            episode_number,
        ),
        EpisodeNotFoundError,
    )
