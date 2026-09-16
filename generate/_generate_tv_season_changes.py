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

MODEL_NAME = "TvSeasonChangesModel"


# TODO: Validate
class TvSeasonChangesId(RecordingId[TMiniDB]):
    name: str
    season_id: int

    # TODO: Validate
    def recording_name(self) -> str:
        return self.name

    # TODO: Validate
    def download(self, client: TMiniDB) -> str:
        return client.tv_season.changes.download(self.season_id)


CHANGE_LOGS = load_ids(GENERATOR_PATHS, MODEL_NAME, TvSeasonChangesId)


# TODO: Validate
def generate_tv_season_changes(client: TMiniDB) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, CHANGE_LOGS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, TvSeasonChangesId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_tv_season_changes(
        TMiniDB(get_credential(ACCESS_TOKEN_CREDENTIAL), build_client_automatically()),
    )
