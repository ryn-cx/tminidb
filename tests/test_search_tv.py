# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from tminidb import TMiniDB

NO_MATCHES_QUERY = "1234567890qwertyuiopasdfghjklzxcvbnm"
"""A query nothing matches, which the API answers with one empty page."""

QUERIES = [
    pytest.param("Breaking Bad", id="breaking bad"),
    pytest.param("Astro Boy", id="a series with no announced air date"),
    pytest.param(NO_MATCHES_QUERY, id="query nothing matches"),
]


# TODO: Validate
@pytest.mark.parametrize("query", QUERIES)
def test_download(client: TMiniDB, query: str) -> None:
    assert client.search.tv(query).page == 1


# TODO: Validate
def test_download_no_matches(client: TMiniDB) -> None:
    results = client.search.tv(NO_MATCHES_QUERY)
    assert results.total_results == 0
    assert results.results == []
