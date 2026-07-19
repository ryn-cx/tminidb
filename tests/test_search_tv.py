# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import download_and_save, parse_json

if TYPE_CHECKING:
    from tminidb import Tminidb
    from tminidb.search_tv import SearchTv

QUERY = "Breaking Bad"


@pytest.fixture(scope="session")
def endpoint(client: Tminidb) -> SearchTv:
    return client.search_tv


class TestSearchTv:
    def test_download(self, endpoint: SearchTv) -> None:
        download_and_save(endpoint, QUERY, lambda: endpoint.download(QUERY))

    def test_parse(self, endpoint: SearchTv) -> None:
        data = parse_json(endpoint, QUERY)
        assert data is not None


@pytest.mark.parametrize("page", [1, 2])
def test_log_id(endpoint: SearchTv, page: int) -> None:
    expected = f"SearchTv query={QUERY!r}"
    if page != 1:
        expected += f" page={page!r}"
    assert endpoint.get_log_id(QUERY, page=page) == expected
