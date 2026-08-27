# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import RecordedEndpoint
from tminidb.exceptions import MovieNotFoundError
from tminidb.movie.details.models import MovieDetailsModel

if TYPE_CHECKING:
    from tminidb import TMiniDB

MOVIE_IDS = [
    pytest.param(603, id="the matrix"),
    pytest.param(1466882, id="movie with almost nothing filled in"),
]


# TODO: Validate
class MovieDetailsTest(RecordedEndpoint):
    MODEL = MovieDetailsModel


# TODO: Validate
@pytest.mark.parametrize("movie_id", MOVIE_IDS)
def test_download(client: TMiniDB, movie_id: int) -> None:
    MovieDetailsTest.download_test(
        movie_id,
        lambda: client.movie.details.download(movie_id),
    )


# TODO: Validate
@pytest.mark.parametrize("movie_id", MOVIE_IDS)
def test_parse(client: TMiniDB, movie_id: int) -> None:
    movie = client.movie.details.load(MovieDetailsTest.recorded_content(movie_id))
    assert movie.id == movie_id


# TODO: Validate
@pytest.mark.parametrize(
    "movie_id",
    [pytest.param(999999999, id="movie that does not exist")],
)
def test_download_invalid(client: TMiniDB, movie_id: int) -> None:
    MovieDetailsTest.error_test(
        movie_id,
        lambda: client.movie.details.download(movie_id),
        MovieNotFoundError,
    )
