from __future__ import annotations

import logging

from get_around import build_client_automatically, get_credential
from good_ass_pydantic_integrator.recordings import (
    RecordingId,
    download_missing,
    load_ids,
    rebuild_model,
)

from generate.constants import ACCESS_TOKEN_CREDENTIAL, GENERATOR_PATHS
from tminidb import TMiniDB

MODEL_NAME = "TvSeriesRecommendationsModel"


# TODO: Validate
class TvSeriesRecommendationsId(RecordingId[TMiniDB]):
    series_id: int

    # TODO: Validate
    def download(self, client: TMiniDB) -> str:
        return client.tv_series.recommendations.download(self.series_id)


SERIES_IDS = load_ids(GENERATOR_PATHS, MODEL_NAME, TvSeriesRecommendationsId)


# TODO: Validate
def generate_tv_series_recommendations(client: TMiniDB) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, SERIES_IDS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, TvSeriesRecommendationsId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_tv_series_recommendations(
        TMiniDB(get_credential(ACCESS_TOKEN_CREDENTIAL), build_client_automatically()),
    )
