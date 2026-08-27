# TODO: Validate
"""Rebuilds TvEpisodeTranslationsModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically, get_credential
from good_ass_pydantic_integrator import generate_model

from generate.constants import ACCESS_TOKEN_CREDENTIAL, FILES_PATH, TMINIDB_PATH
from generate.utils import download_if_missing
from tminidb import TMiniDB

EPISODES = [(1396, 1, 1)]
"""The series id, season number and episode number of each recorded episode."""


# TODO: Validate
def generate_tv_episode_translations(client: TMiniDB) -> None:
    """Rebuild TvEpisodeTranslationsModel."""
    for series_id, season_number, episode_number in EPISODES:
        download_if_missing(
            FILES_PATH,
            "TvEpisodeTranslationsModel",
            f"{series_id}_{season_number}_{episode_number}",
            lambda episode=(series_id, season_number, episode_number): (
                client.tv_episode.translations.download(*episode)
            ),
        )

    generate_model(FILES_PATH, TMINIDB_PATH, "TvEpisodeTranslationsModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_tv_episode_translations(
        TMiniDB(get_credential(ACCESS_TOKEN_CREDENTIAL), build_client_automatically()),
    )
