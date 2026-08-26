# TODO: Validate
"""Rebuilds SearchTvModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically, get_credential
from good_ass_pydantic_integrator import generate_model

from generate.constants import ACCESS_TOKEN_CREDENTIAL, FILES_PATH, TMINIDB_PATH
from generate.utils import download_if_missing
from tminidb import TMiniDB

QUERIES = ["Breaking Bad", "Astro Boy", "1234567890qwertyuiopasdfghjklzxcvbnm"]
"""The queries the model is built from. Nothing matches the last one.

Astro Boy matches series that have no announced air date, which the API gives
an empty first_air_date.
"""


# TODO: Validate
def generate_search_tv(client: TMiniDB) -> None:
    """Rebuild SearchTvModel."""
    for query in QUERIES:
        download_if_missing(
            FILES_PATH,
            "SearchTvModel",
            query,
            lambda query=query: client.search_tv.download(query),
        )

    generate_model(FILES_PATH, TMINIDB_PATH, "SearchTvModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_search_tv(
        TMiniDB(get_credential(ACCESS_TOKEN_CREDENTIAL), build_client_automatically()),
    )
