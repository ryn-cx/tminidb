# TODO: Validate
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
from tminidb.find.by_id import (
    ExternalSource,  # noqa: TC001 - Pydantic reads it at runtime.
)

MODEL_NAME = "FindByIdModel"


# TODO: Validate
class FindByIdId(RecordingId[TMiniDB]):
    external_id: str
    external_source: ExternalSource

    # TODO: Validate
    def recording_name(self) -> str:
        return f"{self.external_source}_{self.external_id}"

    # TODO: Validate
    def download(self, client: TMiniDB) -> str:
        return client.find.by_id.download(self.external_id, self.external_source)


FIND_IDS = load_ids(GENERATOR_PATHS, MODEL_NAME, FindByIdId)


# TODO: Validate
def generate_find_by_id(client: TMiniDB) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, FIND_IDS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, FindByIdId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_find_by_id(
        TMiniDB(get_credential(ACCESS_TOKEN_CREDENTIAL), build_client_automatically()),
    )
