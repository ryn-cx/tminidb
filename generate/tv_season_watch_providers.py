# TODO: Validate
"""Rebuilds TvSeasonWatchProvidersModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically, get_credential

from generate.constants import ACCESS_TOKEN_CREDENTIAL, FILES_PATH, TMINIDB_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model
from tminidb import TMiniDB

SEASONS = load_ids("TvSeasonWatchProvidersModel")
"""The series id and season number of each season the model is built from."""


# TODO: Validate
def generate_tv_season_watch_providers(client: TMiniDB) -> None:
    """Rebuild TvSeasonWatchProvidersModel."""
    for series_id, season_number in SEASONS:
        download_if_missing(
            FILES_PATH,
            "TvSeasonWatchProvidersModel",
            f"{series_id}_{season_number}",
            lambda series_id=series_id, season_number=season_number: (
                client.tv_season.watch_providers.download(series_id, season_number)
            ),
        )
    rebuild_model(
        FILES_PATH,
        TMINIDB_PATH,
        "TvSeasonWatchProvidersModel",
        name_of=lambda season: f"{season[0]}_{season[1]}",
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_tv_season_watch_providers(
        TMiniDB(get_credential(ACCESS_TOKEN_CREDENTIAL), build_client_automatically()),
    )
