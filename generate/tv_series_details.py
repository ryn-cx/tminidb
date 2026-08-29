# TODO: Validate
"""Rebuilds TvSeriesDetailsModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically, get_credential

from generate.constants import ACCESS_TOKEN_CREDENTIAL, FILES_PATH, TMINIDB_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model
from tminidb import TMiniDB

SERIES_IDS = load_ids("TvSeriesDetailsModel")
"""The series the model is built from."""


# TODO: Validate
def generate_tv_series_details(client: TMiniDB) -> None:
    """Rebuild TvSeriesDetailsModel."""
    for series_id in SERIES_IDS:
        download_if_missing(
            FILES_PATH,
            "TvSeriesDetailsModel",
            series_id,
            lambda series_id=series_id: client.tv_series.details.download(series_id),
        )

    rebuild_model(FILES_PATH, TMINIDB_PATH, "TvSeriesDetailsModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_tv_series_details(
        TMiniDB(get_credential(ACCESS_TOKEN_CREDENTIAL), build_client_automatically()),
    )
