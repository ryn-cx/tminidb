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

MODEL_NAME = "ChangesTvListModel"


# TODO: Validate
class ChangesTvListId(RecordingId[TMiniDB]):
    day: date
    page: int = 1

    # TODO: Validate
    def download(self, client: TMiniDB) -> str:
        return client.changes.tv_list.download(
            start_date=self.day,
            end_date=self.day,
            page=self.page,
        )


PAGES = load_ids(GENERATOR_PATHS, MODEL_NAME, ChangesTvListId)


# TODO: Validate
def generate_changes_tv_list(client: TMiniDB) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, PAGES, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, ChangesTvListId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_changes_tv_list(
        TMiniDB(get_credential(ACCESS_TOKEN_CREDENTIAL), build_client_automatically()),
    )
