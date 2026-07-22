# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import download_and_save, parse_json_to_model

if TYPE_CHECKING:
    from tminidb import TMiniDB
    from tminidb.search_tv import SearchTv

QUERY = "Breaking Bad"


@pytest.fixture(scope="session")
def endpoint(client: TMiniDB) -> SearchTv:
    return client.search_tv


class TestSearchTv:
    def test_download(self, endpoint: SearchTv) -> None:
        download_and_save(endpoint, QUERY, lambda: endpoint.download(QUERY))

    def test_parse(self, endpoint: SearchTv) -> None:
        data = parse_json_to_model(endpoint, QUERY)
        assert data is not None
