# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tminidb.exceptions import MovieNotFoundError

if TYPE_CHECKING:
    from tminidb import TMiniDB

SECOND_PAGE = 2

MOVIE_IDS = [
    pytest.param(603, id="the matrix"),
    pytest.param(2119, id="days of thunder"),
]


# TODO: Validate
@pytest.mark.parametrize("movie_id", MOVIE_IDS)
def test_download(client: TMiniDB, movie_id: int) -> None:
    similar = client.movie.similar(movie_id)
    assert similar.page == 1
    assert similar.results


# TODO: Validate
def test_download_page(client: TMiniDB) -> None:
    assert client.movie.similar(603, page=SECOND_PAGE).page == SECOND_PAGE


# TODO: Validate
def test_download_invalid(client: TMiniDB) -> None:
    with pytest.raises(MovieNotFoundError):
        client.movie.similar.download(999999999)
