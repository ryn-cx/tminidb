# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import assert_error, download_and_save, parse_json
from tminidb.exceptions import HTTPError

if TYPE_CHECKING:
    from tminidb import Tminidb
    from tminidb.tv_season_details import TvSeasonDetails

SERIES_ID = 1396
SEASON_NUMBER = 1
NAME = f"{SERIES_ID}_{SEASON_NUMBER}"
INVALID_SERIES_ID = 999999999
INVALID_NAME = f"{INVALID_SERIES_ID}_{SEASON_NUMBER}"


@pytest.fixture(scope="session")
def endpoint(client: Tminidb) -> TvSeasonDetails:
    return client.tv_season_details


class TestTvSeasonDetails:
    def test_download(self, endpoint: TvSeasonDetails) -> None:
        download_and_save(
            endpoint,
            NAME,
            lambda: endpoint.download(SERIES_ID, SEASON_NUMBER),
        )

    def test_parse(self, endpoint: TvSeasonDetails) -> None:
        data = parse_json(endpoint, NAME)
        assert data is not None

    def test_invalid_download(self, endpoint: TvSeasonDetails) -> None:
        assert_error(
            endpoint,
            INVALID_NAME,
            lambda: endpoint.download(INVALID_SERIES_ID, SEASON_NUMBER),
            HTTPError,
        )


@pytest.mark.parametrize("language", [None, "fr-FR"])
def test_log_id(endpoint: TvSeasonDetails, language: str | None) -> None:
    kwargs: dict[str, str] = {} if language is None else {"language": language}
    expected = (
        f"TvSeasonDetails series_id={SERIES_ID!r} season_number={SEASON_NUMBER!r}"
    )
    if language is not None:
        expected += f" language={language!r}"
    assert endpoint.get_log_id(SERIES_ID, SEASON_NUMBER, **kwargs) == expected
