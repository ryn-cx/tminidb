from __future__ import annotations

import logging

from get_around import build_client_automatically, get_credential
from good_ass_pydantic_integrator.recordings import (
    RecordingId,
    download_missing,
    load_ids,
    rebuild_model,
)

from generate.constants import ACCESS_TOKEN_CREDENTIAL, GENERATOR_PATHS
from tminidb import TMiniDB

MODEL_NAME = "TvEpisodeGroupDetailsModel"


# TODO: Validate
class TvEpisodeGroupDetailsId(RecordingId[TMiniDB]):
    episode_group_id: str

    # TODO: Validate
    def download(self, client: TMiniDB) -> str:
        return client.tv_episode_group.details.download(self.episode_group_id)


EPISODE_GROUP_IDS = load_ids(GENERATOR_PATHS, MODEL_NAME, TvEpisodeGroupDetailsId)


# TODO: Validate
def generate_tv_episode_group_details(client: TMiniDB) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, EPISODE_GROUP_IDS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, TvEpisodeGroupDetailsId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_tv_episode_group_details(
        TMiniDB(get_credential(ACCESS_TOKEN_CREDENTIAL), build_client_automatically()),
    )
