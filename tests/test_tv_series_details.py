# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import assert_error, download_and_save, parse_json_to_model
from tminidb.exceptions import HTTPError

if TYPE_CHECKING:
    from tminidb import TMiniDB
    from tminidb.tv_series_details import TvSeriesDetails

SERIES_ID = 1396
INVALID_SERIES_ID = 999999999


@pytest.fixture(scope="session")
def endpoint(client: TMiniDB) -> TvSeriesDetails:
    return client.tv_series_details


class TestTvSeriesDetails:
    def test_download(self, endpoint: TvSeriesDetails) -> None:
        download_and_save(
            endpoint,
            str(SERIES_ID),
            lambda: endpoint.download(SERIES_ID),
        )

    def test_parse(self, endpoint: TvSeriesDetails) -> None:
        data = parse_json_to_model(endpoint, str(SERIES_ID))
        assert data is not None

    def test_invalid_download(self, endpoint: TvSeriesDetails) -> None:
        assert_error(
            endpoint,
            str(INVALID_SERIES_ID),
            lambda: endpoint.download(INVALID_SERIES_ID),
            HTTPError,
        )


@pytest.mark.parametrize("language", [None, "fr-FR"])
def test_log_id(endpoint: TvSeriesDetails, language: str | None) -> None:
    kwargs: dict[str, str] = {} if language is None else {"language": language}
    expected = f"TvSeriesDetails series_id={SERIES_ID!r}"
    if language is not None:
        expected += f" language={language!r}"
    assert endpoint.get_log_id(SERIES_ID, **kwargs) == expected
