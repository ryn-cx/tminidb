# TODO: Validate
"""Rebuilds MovieChangesModel."""

from __future__ import annotations

import logging
from datetime import date

from get_around import build_client_automatically, get_credential
from good_ass_pydantic_integrator import generate_model

from generate.constants import ACCESS_TOKEN_CREDENTIAL, FILES_PATH, TMINIDB_PATH
from generate.utils import download_if_missing
from tminidb import TMiniDB

CHANGE_LOGS = [
    ("969681_with_changes", 969681, date(2026, 8, 18), None),
    ("969681_merged", 969681, date(2026, 7, 22), date(2026, 8, 18)),
    ("969681_without_changes", 969681, date(2026, 1, 1), date(2026, 1, 1)),
    ("2147483647", 2147483647, None, None),
]
"""The name each change log is recorded under, the movie id, and the range asked for.

A range with no end is one window the API answers in a single request; a range
with both ends is walked 14 days at a time and merged into one file.
"""


# TODO: Validate
def download_change_log(
    client: TMiniDB,
    movie_id: int,
    start_date: date | None,
    end_date: date | None,
) -> str:
    """Download the change log the way the range asked for needs it downloaded."""
    if start_date is not None and end_date is not None:
        return client.movie_changes.download_merged(movie_id, start_date, end_date)
    return client.movie_changes.download(movie_id, start_date=start_date)


# TODO: Validate
def generate_movie_changes(client: TMiniDB) -> None:
    """Rebuild MovieChangesModel."""
    for name, movie_id, start_date, end_date in CHANGE_LOGS:
        download_if_missing(
            FILES_PATH,
            "MovieChangesModel",
            name,
            lambda movie_id=movie_id, start_date=start_date, end_date=end_date: (
                download_change_log(client, movie_id, start_date, end_date)
            ),
        )
    generate_model(FILES_PATH, TMINIDB_PATH, "MovieChangesModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_movie_changes(
        TMiniDB(get_credential(ACCESS_TOKEN_CREDENTIAL), build_client_automatically()),
    )
