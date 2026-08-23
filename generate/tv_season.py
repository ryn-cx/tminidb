# TODO: Validate
"""Rebuilds TvSeasonModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically, get_credential
from good_ass_pydantic_integrator import generate_model

from generate.constants import ACCESS_TOKEN_CREDENTIAL, FILES_PATH, TMINIDB_PATH
from generate.utils import download_if_missing
from tminidb import TMiniDB

SEASONS = [(1396, 1)]
"""The series id and season number of each season the model is built from."""


# TODO: Validate
def generate_tv_season(client: TMiniDB) -> None:
    """Rebuild TvSeasonModel."""
    for series_id, season_number in SEASONS:
        download_if_missing(
            FILES_PATH,
            "TvSeasonModel",
            f"{series_id}_{season_number}",
            lambda series_id=series_id, season_number=season_number: (
                client.tv_season.download(series_id, season_number)
            ),
        )
    generate_model(FILES_PATH, TMINIDB_PATH, "TvSeasonModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_tv_season(
        TMiniDB(get_credential(ACCESS_TOKEN_CREDENTIAL), build_client_automatically()),
    )
