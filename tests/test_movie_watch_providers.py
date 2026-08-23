# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import RecordedEndpoint
from tminidb.exceptions import MovieNotFoundError
from tminidb.watch_providers.movie.models import MovieWatchProvidersModel

if TYPE_CHECKING:
    from tminidb import TMiniDB

MOVIE_IDS = [
    pytest.param(603, id="the matrix"),
]


# TODO: Validate
class MovieWatchProvidersTest(RecordedEndpoint):
    MODEL = MovieWatchProvidersModel


# TODO: Validate
@pytest.mark.parametrize("movie_id", MOVIE_IDS)
def test_download(client: TMiniDB, movie_id: int) -> None:
    MovieWatchProvidersTest.download_test(
        movie_id,
        lambda: client.movie_watch_providers.download(movie_id),
    )


# TODO: Validate
@pytest.mark.parametrize("movie_id", MOVIE_IDS)
def test_parse(client: TMiniDB, movie_id: int) -> None:
    providers = client.movie_watch_providers.load(
        MovieWatchProvidersTest.recorded_content(movie_id),
    )
    assert providers.id == movie_id


# TODO: Validate
@pytest.mark.parametrize(
    "movie_id",
    [pytest.param(999999999, id="movie that does not exist")],
)
def test_download_invalid(client: TMiniDB, movie_id: int) -> None:
    MovieWatchProvidersTest.error_test(
        movie_id,
        lambda: client.movie_watch_providers.download(movie_id),
        MovieNotFoundError,
    )
