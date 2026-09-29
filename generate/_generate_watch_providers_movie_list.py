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

MODEL_NAME = "WatchProvidersMovieListModel"


# TODO: Validate
class WatchProvidersMovieListId(RecordingId[TMiniDB]):
    watch_region: str | None = None

    # TODO: Validate
    def recording_name(self) -> str:
        """Name the recording after its region, or `all` when it has none."""
        return self.watch_region or "all"

    # TODO: Validate
    def download(self, client: TMiniDB) -> str:
        return client.watch_providers.movie_list.download(
            watch_region=self.watch_region,
        )


WATCH_REGIONS = load_ids(GENERATOR_PATHS, MODEL_NAME, WatchProvidersMovieListId)


# TODO: Validate
def generate_watch_providers_movie_list(client: TMiniDB) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, WATCH_REGIONS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, WatchProvidersMovieListId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_watch_providers_movie_list(
        TMiniDB(get_credential(ACCESS_TOKEN_CREDENTIAL), build_client_automatically()),
    )
