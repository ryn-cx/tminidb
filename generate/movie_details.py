# TODO: Validate
"""Rebuilds MovieDetailsModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically, get_credential
from good_ass_pydantic_integrator import generate_model

from generate.constants import ACCESS_TOKEN_CREDENTIAL, FILES_PATH, TMINIDB_PATH
from generate.utils import download_if_missing
from tminidb import TMiniDB

MOVIE_IDS = [603, 1466882]
"""The movies the model is built from."""


# TODO: Validate
def generate_movie_details(client: TMiniDB) -> None:
    """Rebuild MovieDetailsModel."""
    for movie_id in MOVIE_IDS:
        download_if_missing(
            FILES_PATH,
            "MovieDetailsModel",
            movie_id,
            lambda movie_id=movie_id: client.movie.details.download(movie_id),
        )

    generate_model(FILES_PATH, TMINIDB_PATH, "MovieDetailsModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_movie_details(
        TMiniDB(get_credential(ACCESS_TOKEN_CREDENTIAL), build_client_automatically()),
    )
