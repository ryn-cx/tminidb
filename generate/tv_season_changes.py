# TODO: Validate
"""Rebuilds TvSeasonChangesModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically, get_credential
from good_ass_pydantic_integrator import generate_model

from generate.constants import ACCESS_TOKEN_CREDENTIAL, FILES_PATH, TMINIDB_PATH
from generate.utils import download_if_missing
from tminidb import TMiniDB

CHANGE_LOGS = [
    ("364732", 364732),
    ("unknown_999999999", 999999999),
]
"""The name each change log is recorded under and the season id it is for."""


# TODO: Validate
def generate_tv_season_changes(client: TMiniDB) -> None:
    """Rebuild TvSeasonChangesModel."""
    for name, season_id in CHANGE_LOGS:
        download_if_missing(
            FILES_PATH,
            "TvSeasonChangesModel",
            name,
            lambda season_id=season_id: client.tv_season_changes.download(season_id),
        )
    generate_model(FILES_PATH, TMINIDB_PATH, "TvSeasonChangesModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_tv_season_changes(
        TMiniDB(get_credential(ACCESS_TOKEN_CREDENTIAL), build_client_automatically()),
    )
