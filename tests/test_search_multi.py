# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from tminidb import TMiniDB

NO_MATCHES_QUERY = "1234567890qwertyuiopasdfghjklzxcvbnm"
"""A query nothing matches, which the API answers with one empty page."""

QUERIES = [
    pytest.param("Accidental Partners", id="a movie and nothing else"),
    pytest.param("Teach You a Lesson", id="a series and a movie sharing a name"),
    pytest.param("Anoushka", id="a person"),
    pytest.param("Astro Boy", id="a series with no announced air date"),
    pytest.param(NO_MATCHES_QUERY, id="query nothing matches"),
]


# TODO: Validate
@pytest.mark.parametrize("query", QUERIES)
def test_download(client: TMiniDB, query: str) -> None:
    assert client.search.multi(query).page == 1


# TODO: Validate
def test_download_no_matches(client: TMiniDB) -> None:
    results = client.search.multi(NO_MATCHES_QUERY)
    assert results.total_results == 0
    assert results.results == []
