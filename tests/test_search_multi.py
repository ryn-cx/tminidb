# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING, NamedTuple

import pytest

from tests.utils import download_and_save, parse_json_to_model

if TYPE_CHECKING:
    from tminidb import TMiniDB
    from tminidb.search_multi import SearchMulti


class TestData(NamedTuple):
    query: str
    expected_id: int


# Each group should return just that media type.
MOVIE_TEST_DATA = [
    # Returns just a movie
    TestData("Accidental Partners", 1632181),
]
TV_TEST_DATA = [
    # Returns just a tv show
    TestData("Teach You a Lesson", 276161),
]
PERSON_TEST_DATA = [
    # Returns just a person
    TestData("Anoushka", 5256874),
]
TEST_DATA = MOVIE_TEST_DATA + TV_TEST_DATA + PERSON_TEST_DATA

# Returns nothing
INVALID_QUERY = "1234567890qwertyuiopasdfghjklzxcvbnm"

QUERY = MOVIE_TEST_DATA[0].query


@pytest.fixture(scope="session")
def endpoint(client: TMiniDB) -> SearchMulti:
    return client.search_multi


@pytest.mark.parametrize("case", TEST_DATA, ids=lambda case: case.query)
def test_download(endpoint: SearchMulti, case: TestData) -> None:
    download_and_save(endpoint, case.query, lambda: endpoint.download(case.query))


@pytest.mark.parametrize("case", TEST_DATA, ids=lambda case: case.query)
def test_parse_raw(endpoint: SearchMulti, case: TestData) -> None:
    model = parse_json_to_model(endpoint, case.query)
    assert case.expected_id in [item.id for item in model.results]


def test_download_invalid(endpoint: SearchMulti) -> None:
    download_and_save(endpoint, INVALID_QUERY, lambda: endpoint.download(INVALID_QUERY))


def test_parse_invalid(endpoint: SearchMulti) -> None:
    assert parse_json_to_model(endpoint, INVALID_QUERY).results == []
