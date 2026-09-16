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
    pytest.param(135886, id="the latino list volume 2"),
]


# TODO: Validate
@pytest.mark.parametrize("movie_id", MOVIE_IDS)
def test_download(client: TMiniDB, movie_id: int) -> None:
    recommendations = client.movie.recommendations(movie_id)
    assert recommendations.page == 1
    assert recommendations.results


# TODO: Validate
def test_download_page(client: TMiniDB) -> None:
    assert client.movie.recommendations(603, page=SECOND_PAGE).page == SECOND_PAGE


# TODO: Validate
def test_download_invalid(client: TMiniDB) -> None:
    with pytest.raises(MovieNotFoundError):
        client.movie.recommendations.download(999999999)
