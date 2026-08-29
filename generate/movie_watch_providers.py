# TODO: Validate
"""Rebuilds MovieWatchProvidersModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically, get_credential

from generate.constants import ACCESS_TOKEN_CREDENTIAL, FILES_PATH, TMINIDB_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model
from tminidb import TMiniDB

MOVIE_IDS = load_ids("MovieWatchProvidersModel")
"""The movies the model is built from."""


# TODO: Validate
def generate_movie_watch_providers(client: TMiniDB) -> None:
    """Rebuild MovieWatchProvidersModel."""
    for movie_id in MOVIE_IDS:
        download_if_missing(
            FILES_PATH,
            "MovieWatchProvidersModel",
            movie_id,
            lambda movie_id=movie_id: client.movie.watch_providers.download(movie_id),
        )

    rebuild_model(FILES_PATH, TMINIDB_PATH, "MovieWatchProvidersModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_movie_watch_providers(
        TMiniDB(get_credential(ACCESS_TOKEN_CREDENTIAL), build_client_automatically()),
    )
