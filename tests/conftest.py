# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from get_around import get_credential

from tests.current_test import CURRENT_TEST
from tminidb import TMiniDB

if TYPE_CHECKING:
    from collections.abc import Iterator

# The comparisons a test makes live in `tests.utils`, which is not a test file
# and so is not rewritten to report what differed unless it is asked for.
pytest.register_assert_rewrite("tests.utils")

ACCESS_TOKEN_CREDENTIAL = "TMDB_ACCESS_TOKEN"  # noqa: S105


# TODO: Validate
@pytest.fixture(scope="session")
def client() -> TMiniDB:
    return TMiniDB(get_credential(ACCESS_TOKEN_CREDENTIAL))


# TODO: Validate
@pytest.fixture(autouse=True)
def _current_test(request: pytest.FixtureRequest) -> Iterator[None]:
    """Names the folder the recordings of the running test are kept in."""
    node = request.cls.__name__ if request.cls else request.node.name
    token = CURRENT_TEST.set(node)
    try:
        yield
    finally:
        CURRENT_TEST.reset(token)
