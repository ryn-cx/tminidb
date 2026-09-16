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

MODEL_NAME = "TvSeasonDetailsModel"


# TODO: Validate
class TvSeasonDetailsId(RecordingId[TMiniDB]):
    series_id: int
    season_number: int

    # TODO: Validate
    def recording_name(self) -> str:
        return f"{self.series_id}_{self.season_number}"

    # TODO: Validate
    def download(self, client: TMiniDB) -> str:
        return client.tv_season.details.download(self.series_id, self.season_number)


SEASONS = load_ids(GENERATOR_PATHS, MODEL_NAME, TvSeasonDetailsId)


# TODO: Validate
def generate_tv_season_details(client: TMiniDB) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, SEASONS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, TvSeasonDetailsId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_tv_season_details(
        TMiniDB(get_credential(ACCESS_TOKEN_CREDENTIAL), build_client_automatically()),
    )
