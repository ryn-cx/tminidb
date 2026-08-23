# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import RecordedEndpoint
from tminidb.details.movie.models import MovieModel
from tminidb.exceptions import MovieNotFoundError

if TYPE_CHECKING:
    from tminidb import TMiniDB

MOVIE_IDS = [
    pytest.param(603, id="the matrix"),
    pytest.param(1466882, id="movie with almost nothing filled in"),
]


# TODO: Validate
class MovieTest(RecordedEndpoint):
    MODEL = MovieModel


# TODO: Validate
@pytest.mark.parametrize("movie_id", MOVIE_IDS)
def test_download(client: TMiniDB, movie_id: int) -> None:
    MovieTest.download_test(movie_id, lambda: client.movie.download(movie_id))


# TODO: Validate
@pytest.mark.parametrize("movie_id", MOVIE_IDS)
def test_parse(client: TMiniDB, movie_id: int) -> None:
    movie = client.movie.load(MovieTest.recorded_content(movie_id))
    assert movie.id == movie_id


# TODO: Validate
@pytest.mark.parametrize(
    "movie_id",
    [pytest.param(999999999, id="movie that does not exist")],
)
def test_download_invalid(client: TMiniDB, movie_id: int) -> None:
    MovieTest.error_test(
        movie_id,
        lambda: client.movie.download(movie_id),
        MovieNotFoundError,
    )
