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

MODEL_NAME = "MovieChangesModel"


# TODO: Validate
class MovieChangesId(RecordingId[TMiniDB]):
    name: str
    movie_id: int
    start_date: date | None = None
    end_date: date | None = None

    # TODO: Validate
    def recording_name(self) -> str:
        return self.name

    # TODO: Validate
    def download(self, client: TMiniDB) -> str:
        if self.start_date is not None and self.end_date is not None:
            return client.movie.changes.download_merged(
                self.movie_id,
                self.start_date,
                self.end_date,
            )
        return client.movie.changes.download(
            self.movie_id,
            start_date=self.start_date,
        )


CHANGE_LOGS = load_ids(GENERATOR_PATHS, MODEL_NAME, MovieChangesId)


# TODO: Validate
def generate_movie_changes(client: TMiniDB) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, CHANGE_LOGS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, MovieChangesId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_movie_changes(
        TMiniDB(get_credential(ACCESS_TOKEN_CREDENTIAL), build_client_automatically()),
    )
