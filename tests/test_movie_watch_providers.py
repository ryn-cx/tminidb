# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import assert_error, download_and_save, parse_json_to_model
from tminidb.exceptions import HTTPError

if TYPE_CHECKING:
    from tminidb import TMiniDB
    from tminidb.movie_watch_providers import MovieWatchProviders

MOVIE_ID = 603
INVALID_MOVIE_ID = 999999999


@pytest.fixture(scope="session")
def endpoint(client: TMiniDB) -> MovieWatchProviders:
    return client.movie_watch_providers


class TestMovieWatchProviders:
    def test_download(self, endpoint: MovieWatchProviders) -> None:
        download_and_save(
            endpoint,
            str(MOVIE_ID),
            lambda: endpoint.download(MOVIE_ID),
        )

    def test_parse(self, endpoint: MovieWatchProviders) -> None:
        data = parse_json_to_model(endpoint, str(MOVIE_ID))
        assert data is not None

    def test_invalid_download(self, endpoint: MovieWatchProviders) -> None:
        assert_error(
            endpoint,
            str(INVALID_MOVIE_ID),
            lambda: endpoint.download(INVALID_MOVIE_ID),
            HTTPError,
        )


def test_log_id(endpoint: MovieWatchProviders) -> None:
    assert (
        endpoint.get_log_id(MOVIE_ID)
        == f"MovieWatchProviders movie_id={MOVIE_ID!r}"
    )
