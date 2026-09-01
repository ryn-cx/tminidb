# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import RecordedEndpoint
from tminidb.exceptions import MovieNotFoundError
from tminidb.movie.translations.models import MovieTranslationsModel

if TYPE_CHECKING:
    from tminidb import TMiniDB

MOVIE_IDS = [
    pytest.param(603, id="the matrix"),
]


# TODO: Validate
class MovieTranslationsTest(RecordedEndpoint):
    MODEL = MovieTranslationsModel


# TODO: Validate
@pytest.mark.parametrize("movie_id", MOVIE_IDS)
def test_download(client: TMiniDB, movie_id: int) -> None:
    MovieTranslationsTest.download_test(
        movie_id,
        lambda: client.movie.translations.download(movie_id),
    )


# TODO: Validate
@pytest.mark.parametrize("movie_id", MOVIE_IDS)
def test_parse(client: TMiniDB, movie_id: int) -> None:
    translations = client.movie.translations.load(
        MovieTranslationsTest.recorded_content(movie_id),
    )
    assert translations.id == movie_id
    assert translations.translations


# TODO: Validate
@pytest.mark.parametrize(
    "movie_id",
    [pytest.param(999999999, id="movie that does not exist")],
)
def test_download_invalid(client: TMiniDB, movie_id: int) -> None:
    MovieTranslationsTest.error_test(
        movie_id,
        lambda: client.movie.translations.download(movie_id),
        MovieNotFoundError,
    )
