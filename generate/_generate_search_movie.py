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

MODEL_NAME = "SearchMovieModel"


# TODO: Validate
class SearchMovieId(RecordingId[TMiniDB]):
    query: str

    # TODO: Validate
    def download(self, client: TMiniDB) -> str:
        return client.search.movie.download(self.query)


QUERIES = load_ids(GENERATOR_PATHS, MODEL_NAME, SearchMovieId)


# TODO: Validate
def generate_search_movie(client: TMiniDB) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, QUERIES, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, SearchMovieId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_search_movie(
        TMiniDB(get_credential(ACCESS_TOKEN_CREDENTIAL), build_client_automatically()),
    )
