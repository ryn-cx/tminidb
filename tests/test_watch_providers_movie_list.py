# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from tminidb import TMiniDB

WATCH_REGIONS = [
    pytest.param("US", id="united states"),
    pytest.param("JP", id="japan"),
]


# TODO: Validate
@pytest.mark.parametrize("watch_region", WATCH_REGIONS)
def test_download(client: TMiniDB, watch_region: str) -> None:
    providers = client.watch_providers.movie_list(watch_region=watch_region)
    assert providers.results


# TODO: Validate
def test_download_without_region(client: TMiniDB) -> None:
    assert client.watch_providers.movie_list().results
