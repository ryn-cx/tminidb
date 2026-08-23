# TODO: Validate
"""Rebuilds TvEpisodeGroupModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically, get_credential
from good_ass_pydantic_integrator import generate_model

from generate.constants import ACCESS_TOKEN_CREDENTIAL, FILES_PATH, TMINIDB_PATH
from generate.utils import download_if_missing
from tminidb import TMiniDB

EPISODE_GROUP_IDS = [
    "5e9077d2e640d600151f32bd",
    "69f50757054263b7bc87e32a",
]
"""The episode groups the model is built from."""


# TODO: Validate
def generate_tv_episode_group(client: TMiniDB) -> None:
    """Rebuild TvEpisodeGroupModel."""
    for episode_group_id in EPISODE_GROUP_IDS:
        download_if_missing(
            FILES_PATH,
            "TvEpisodeGroupModel",
            episode_group_id,
            lambda episode_group_id=episode_group_id: client.tv_episode_group.download(
                episode_group_id,
            ),
        )

    generate_model(FILES_PATH, TMINIDB_PATH, "TvEpisodeGroupModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_tv_episode_group(
        TMiniDB(get_credential(ACCESS_TOKEN_CREDENTIAL), build_client_automatically()),
    )
