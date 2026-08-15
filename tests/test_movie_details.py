# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import assert_error, download_and_save, parse_json_to_model
from tminidb.exceptions import HTTPError

if TYPE_CHECKING:
    from tminidb import TMiniDB
    from tminidb.movie_details import MovieDetails

MOVIE_IDS = (
    603,
    # A sparse entry: no release date, imdb id, backdrop or genres, so it covers
    # the fields a fully filled in movie never shows as null or empty.
    1466882,
)
INVALID_MOVIE_ID = 999999999


@pytest.fixture(scope="session")
def endpoint(client: TMiniDB) -> MovieDetails:
    return client.movie_details


@pytest.fixture(params=MOVIE_IDS)
def movie_id(request: pytest.FixtureRequest) -> int:
    return request.param


class TestMovieDetails:
    def test_download(self, endpoint: MovieDetails, movie_id: int) -> None:
        download_and_save(
            endpoint,
            str(movie_id),
            lambda: endpoint.download(movie_id),
        )

    def test_parse(self, endpoint: MovieDetails, movie_id: int) -> None:
        data = parse_json_to_model(endpoint, str(movie_id))
        assert data is not None

    def test_invalid_download(self, endpoint: MovieDetails) -> None:
        assert_error(
            endpoint,
            str(INVALID_MOVIE_ID),
            lambda: endpoint.download(INVALID_MOVIE_ID),
            HTTPError,
        )
