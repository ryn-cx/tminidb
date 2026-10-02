# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from tminidb import TMiniDB
    from tminidb.find.by_id import ExternalSource

MOVIE_ID = 278
SERIES_ID = 2316

FOUND = [
    pytest.param(
        "tt0111161",
        "imdb_id",
        "movie_results",
        MOVIE_ID,
        id="movie by imdb id",
    ),
    pytest.param(
        "tt0386676",
        "imdb_id",
        "tv_results",
        SERIES_ID,
        id="series by imdb id",
    ),
    pytest.param("73244", "tvdb_id", "tv_results", SERIES_ID, id="series by tvdb id"),
]


# TODO: Validate
@pytest.mark.parametrize(
    ("external_id", "external_source", "results", "tmdb_id"),
    FOUND,
)
def test_download(
    client: TMiniDB,
    external_id: str,
    external_source: ExternalSource,
    results: str,
    tmdb_id: int,
) -> None:
    found = client.find.by_id(external_id, external_source)
    assert [result.id for result in getattr(found, results)] == [tmdb_id]


# TODO: Validate
def test_download_unknown_id(client: TMiniDB) -> None:
    found = client.find.by_id("tt0000000", "imdb_id")
    assert not found.movie_results
    assert not found.tv_results
