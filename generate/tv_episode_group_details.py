# TODO: Validate
"""Rebuilds TvEpisodeGroupDetailsModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically, get_credential

from generate.constants import ACCESS_TOKEN_CREDENTIAL, FILES_PATH, TMINIDB_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model
from tminidb import TMiniDB

EPISODE_GROUP_IDS = load_ids("TvEpisodeGroupDetailsModel")
"""The episode groups the model is built from."""


# TODO: Validate
def generate_tv_episode_group_details(client: TMiniDB) -> None:
    """Rebuild TvEpisodeGroupDetailsModel."""
    for episode_group_id in EPISODE_GROUP_IDS:
        download_if_missing(
            FILES_PATH,
            "TvEpisodeGroupDetailsModel",
            episode_group_id,
            lambda episode_group_id=episode_group_id: (
                client.tv_episode_group.details.download(
                    episode_group_id,
                )
            ),
        )

    rebuild_model(FILES_PATH, TMINIDB_PATH, "TvEpisodeGroupDetailsModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_tv_episode_group_details(
        TMiniDB(get_credential(ACCESS_TOKEN_CREDENTIAL), build_client_automatically()),
    )
