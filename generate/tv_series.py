# TODO: Validate
"""Rebuilds TvSeriesModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically, get_credential
from good_ass_pydantic_integrator import generate_model

from generate.constants import ACCESS_TOKEN_CREDENTIAL, FILES_PATH, TMINIDB_PATH
from generate.utils import download_if_missing
from tminidb import TMiniDB

SERIES_IDS = [1, 1396, 53787]
"""The series the model is built from."""


# TODO: Validate
def generate_tv_series(client: TMiniDB) -> None:
    """Rebuild TvSeriesModel."""
    for series_id in SERIES_IDS:
        download_if_missing(
            FILES_PATH,
            "TvSeriesModel",
            series_id,
            lambda series_id=series_id: client.tv_series.download(series_id),
        )

    generate_model(FILES_PATH, TMINIDB_PATH, "TvSeriesModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_tv_series(
        TMiniDB(get_credential(ACCESS_TOKEN_CREDENTIAL), build_client_automatically()),
    )
