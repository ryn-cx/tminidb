from __future__ import annotations

from typing import TYPE_CHECKING, NamedTuple

import pytest

from tests.utils import download_and_save, parse_json_to_model

if TYPE_CHECKING:
    from tminidb import Tminidb
    from tminidb.search_multi import SearchMulti
    from tminidb.search_multi.grouped import SearchMultiGrouped


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
def endpoint(client: Tminidb) -> SearchMulti:
    return client.search_multi


@pytest.fixture(scope="session")
def grouped_endpoint(client: Tminidb) -> SearchMultiGrouped:
    return client.search_multi_grouped


@pytest.mark.parametrize("case", TEST_DATA, ids=lambda case: case.query)
def test_download(endpoint: SearchMulti, case: TestData) -> None:
    download_and_save(endpoint, case.query, lambda: endpoint.download(case.query))


@pytest.mark.parametrize("case", TEST_DATA, ids=lambda case: case.query)
def test_parse_raw(endpoint: SearchMulti, case: TestData) -> None:
    model = parse_json_to_model(endpoint, case.query)
    assert case.expected_id in [item.id for item in model.results]


@pytest.mark.parametrize("case", MOVIE_TEST_DATA, ids=lambda case: case.query)
def test_grouped_movie(grouped_endpoint: SearchMultiGrouped, case: TestData) -> None:
    model = parse_json_to_model(grouped_endpoint, case.query)
    assert case.expected_id == model.results.movie[0].id


@pytest.mark.parametrize("case", TV_TEST_DATA, ids=lambda case: case.query)
def test_grouped_tv(grouped_endpoint: SearchMultiGrouped, case: TestData) -> None:
    model = parse_json_to_model(grouped_endpoint, case.query)
    assert case.expected_id == model.results.tv[0].id


@pytest.mark.parametrize("case", PERSON_TEST_DATA, ids=lambda case: case.query)
def test_grouped_person(grouped_endpoint: SearchMultiGrouped, case: TestData) -> None:
    model = parse_json_to_model(grouped_endpoint, case.query)
    # Equality cannot be used because there are multiple people with the same name so
    # the first result is not the expected one.
    assert case.expected_id in [item.id for item in model.results.person]


def test_download_invalid(endpoint: SearchMulti) -> None:
    download_and_save(endpoint, INVALID_QUERY, lambda: endpoint.download(INVALID_QUERY))


def test_parse_invalid(endpoint: SearchMulti) -> None:
    assert parse_json_to_model(endpoint, INVALID_QUERY).results == []


def test_grouped_invalid(grouped_endpoint: SearchMultiGrouped) -> None:
    model = parse_json_to_model(grouped_endpoint, INVALID_QUERY)
    assert not model.results.movie
    assert not model.results.tv
    assert not model.results.person


@pytest.mark.parametrize("page", [1, 2])
def test_log_id(endpoint: SearchMulti, client: Tminidb, page: int) -> None:
    expected = f"SearchMulti query={QUERY!r}"
    if page != 1:
        expected += f" page={page!r}"
    log_id = endpoint.get_log_id(QUERY, language=client.language, page=page)
    assert log_id == expected
