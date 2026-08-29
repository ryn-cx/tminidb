# TODO: Validate
"""Rebuilds TvEpisodeDetailsModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically, get_credential

from generate.constants import ACCESS_TOKEN_CREDENTIAL, FILES_PATH, TMINIDB_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model
from tminidb import TMiniDB

EPISODES = load_ids("TvEpisodeDetailsModel")
"""The series id, season number and episode number of each recorded episode."""


# TODO: Validate
def generate_tv_episode_details(client: TMiniDB) -> None:
    """Rebuild TvEpisodeDetailsModel."""
    for series_id, season_number, episode_number in EPISODES:
        download_if_missing(
            FILES_PATH,
            "TvEpisodeDetailsModel",
            f"{series_id}_{season_number}_{episode_number}",
            lambda episode=(series_id, season_number, episode_number): (
                client.tv_episode.details.download(*episode)
            ),
        )

    rebuild_model(
        FILES_PATH,
        TMINIDB_PATH,
        "TvEpisodeDetailsModel",
        name_of=lambda episode: f"{episode[0]}_{episode[1]}_{episode[2]}",
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_tv_episode_details(
        TMiniDB(get_credential(ACCESS_TOKEN_CREDENTIAL), build_client_automatically()),
    )
