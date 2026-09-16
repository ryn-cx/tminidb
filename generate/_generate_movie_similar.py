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

MODEL_NAME = "MovieSimilarModel"


# TODO: Validate
class MovieSimilarId(RecordingId[TMiniDB]):
    movie_id: int

    # TODO: Validate
    def download(self, client: TMiniDB) -> str:
        return client.movie.similar.download(self.movie_id)


MOVIE_IDS = load_ids(GENERATOR_PATHS, MODEL_NAME, MovieSimilarId)


# TODO: Validate
def generate_movie_similar(client: TMiniDB) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, MOVIE_IDS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, MovieSimilarId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_movie_similar(
        TMiniDB(get_credential(ACCESS_TOKEN_CREDENTIAL), build_client_automatically()),
    )
