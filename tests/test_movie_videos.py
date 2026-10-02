# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tminidb.exceptions import MovieNotFoundError

if TYPE_CHECKING:
    from tminidb import TMiniDB

IDS = [
    pytest.param(603, id="the matrix"),
    pytest.param(278, id="the shawshank redemption"),
]


# TODO: Validate
@pytest.mark.parametrize("movie_id", IDS)
def test_download(client: TMiniDB, movie_id: int) -> None:
    videos = client.movie.videos(movie_id)
    assert videos.id == movie_id
    assert videos.results


# TODO: Validate
def test_download_invalid(client: TMiniDB) -> None:
    with pytest.raises(MovieNotFoundError):
        client.movie.videos.download(999999999)
