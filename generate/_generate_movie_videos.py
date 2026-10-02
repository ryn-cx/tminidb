# TODO: Validate
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

MODEL_NAME = "MovieVideosModel"


# TODO: Validate
class MovieVideosId(RecordingId[TMiniDB]):
    movie_id: int

    # TODO: Validate
    def download(self, client: TMiniDB) -> str:
        return client.movie.videos.download(
            self.movie_id,
            include_video_language="en,null",
        )


IDS = load_ids(GENERATOR_PATHS, MODEL_NAME, MovieVideosId)


# TODO: Validate
def generate_movie_videos(client: TMiniDB) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, IDS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, MovieVideosId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_movie_videos(
        TMiniDB(get_credential(ACCESS_TOKEN_CREDENTIAL), build_client_automatically()),
    )
