# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tminidb.exceptions import MovieNotFoundError

if TYPE_CHECKING:
    from tminidb import TMiniDB

MOVIE_IDS = [
    pytest.param(603, id="the matrix"),
]


# TODO: Validate
@pytest.mark.parametrize("movie_id", MOVIE_IDS)
def test_download(client: TMiniDB, movie_id: int) -> None:
    translations = client.movie.translations(movie_id)
    assert translations.id == movie_id
    assert translations.translations


# TODO: Validate
def test_download_invalid(client: TMiniDB) -> None:
    with pytest.raises(MovieNotFoundError):
        client.movie.translations.download(999999999)
