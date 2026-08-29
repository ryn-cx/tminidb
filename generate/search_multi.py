# TODO: Validate
"""Rebuilds SearchMultiModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically, get_credential

from generate.constants import ACCESS_TOKEN_CREDENTIAL, FILES_PATH, TMINIDB_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model
from tminidb import TMiniDB

QUERIES = load_ids("SearchMultiModel")
"""The queries the model is built from. Nothing matches the last one.

Astro Boy matches series that have no announced air date, which the API gives
an empty first_air_date.
"""


# TODO: Validate
def generate_search_multi(client: TMiniDB) -> None:
    """Rebuild SearchMultiModel."""
    for query in QUERIES:
        download_if_missing(
            FILES_PATH,
            "SearchMultiModel",
            query,
            lambda query=query: client.search.multi.download(query),
        )

    rebuild_model(FILES_PATH, TMINIDB_PATH, "SearchMultiModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_search_multi(
        TMiniDB(get_credential(ACCESS_TOKEN_CREDENTIAL), build_client_automatically()),
    )
