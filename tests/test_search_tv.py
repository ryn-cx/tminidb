# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import RecordedEndpoint
from tminidb.search.tv.models import SearchTvModel

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
class SearchTvTest(RecordedEndpoint):
    MODEL = SearchTvModel


# TODO: Validate
@pytest.mark.parametrize("query", QUERIES)
def test_download(client: TMiniDB, query: str) -> None:
    SearchTvTest.download_test(query, lambda: client.search.tv.download(query))


# TODO: Validate
@pytest.mark.parametrize("query", QUERIES)
def test_parse(client: TMiniDB, query: str) -> None:
    results = client.search.tv.load(SearchTvTest.recorded_content(query))
    assert results.page == 1


# TODO: Validate
def test_parse_no_matches(client: TMiniDB) -> None:
    results = client.search.tv.load(SearchTvTest.recorded_content(NO_MATCHES_QUERY))
    assert results.total_results == 0
    assert results.results == []
