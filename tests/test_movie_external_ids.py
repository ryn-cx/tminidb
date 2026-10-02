# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tminidb.exceptions import MovieNotFoundError

if TYPE_CHECKING:
    from tminidb import TMiniDB

MOVIE_IDS = [
    pytest.param(603, "tt0133093", id="the matrix"),
    pytest.param(278, "tt0111161", id="the shawshank redemption"),
]


# TODO: Validate
@pytest.mark.parametrize(("movie_id", "imdb_id"), MOVIE_IDS)
def test_download(client: TMiniDB, movie_id: int, imdb_id: str) -> None:
    external_ids = client.movie.external_ids(movie_id)
    assert external_ids.id == movie_id
    assert external_ids.imdb_id == imdb_id


# TODO: Validate
def test_download_invalid(client: TMiniDB) -> None:
    with pytest.raises(MovieNotFoundError):
        client.movie.external_ids.download(999999999)
