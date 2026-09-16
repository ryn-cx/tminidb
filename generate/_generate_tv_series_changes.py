from __future__ import annotations

import logging
from datetime import date  # noqa: TC003

from get_around import build_client_automatically, get_credential
from good_ass_pydantic_integrator.recordings import (
    RecordingId,
    download_missing,
    load_ids,
    rebuild_model,
)

from generate.constants import ACCESS_TOKEN_CREDENTIAL, GENERATOR_PATHS
from tminidb import TMiniDB

MODEL_NAME = "TvSeriesChangesModel"


# TODO: Validate
class TvSeriesChangesId(RecordingId[TMiniDB]):
    name: str
    series_id: int
    start_date: date | None = None
    end_date: date | None = None

    # TODO: Validate
    def recording_name(self) -> str:
        return self.name

    # TODO: Validate
    def download(self, client: TMiniDB) -> str:
        if self.start_date is not None and self.end_date is not None:
            return client.tv_series.changes.download_merged(
                self.series_id,
                self.start_date,
                self.end_date,
            )
        return client.tv_series.changes.download(
            self.series_id,
            start_date=self.start_date,
        )


CHANGE_LOGS = load_ids(GENERATOR_PATHS, MODEL_NAME, TvSeriesChangesId)


# TODO: Validate
def generate_tv_series_changes(client: TMiniDB) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, CHANGE_LOGS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, TvSeriesChangesId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_tv_series_changes(
        TMiniDB(get_credential(ACCESS_TOKEN_CREDENTIAL), build_client_automatically()),
    )
