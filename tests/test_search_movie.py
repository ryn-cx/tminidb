# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import download_and_save, parse_json_to_model

if TYPE_CHECKING:
    from tminidb import TMiniDB
    from tminidb.search_movie import SearchMovie

QUERY = "The Matrix"


@pytest.fixture(scope="session")
def endpoint(client: TMiniDB) -> SearchMovie:
    return client.search_movie


class TestSearchMovie:
    def test_download(self, endpoint: SearchMovie) -> None:
        download_and_save(endpoint, QUERY, lambda: endpoint.download(QUERY))

    def test_parse(self, endpoint: SearchMovie) -> None:
        data = parse_json_to_model(endpoint, QUERY)
        assert data is not None
