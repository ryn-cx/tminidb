# TODO: Validate
"""Rebuilds SearchMovieModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically, get_credential

from generate.constants import ACCESS_TOKEN_CREDENTIAL, FILES_PATH, TMINIDB_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model
from tminidb import TMiniDB

QUERIES = load_ids("SearchMovieModel")
"""The queries the model is built from. Nothing matches the last one."""


# TODO: Validate
def generate_search_movie(client: TMiniDB) -> None:
    """Rebuild SearchMovieModel."""
    for query in QUERIES:
        download_if_missing(
            FILES_PATH,
            "SearchMovieModel",
            query,
            lambda query=query: client.search.movie.download(query),
        )

    rebuild_model(FILES_PATH, TMINIDB_PATH, "SearchMovieModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_search_movie(
        TMiniDB(get_credential(ACCESS_TOKEN_CREDENTIAL), build_client_automatically()),
    )
