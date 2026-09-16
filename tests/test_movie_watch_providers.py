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
    providers = client.movie.watch_providers(movie_id)
    assert providers.id == movie_id


# TODO: Validate
def test_download_invalid(client: TMiniDB) -> None:
    with pytest.raises(MovieNotFoundError):
        client.movie.watch_providers.download(999999999)
