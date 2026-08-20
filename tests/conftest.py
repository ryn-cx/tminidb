# TODO: Validate
from __future__ import annotations

import pytest
from get_around import get_credential

from tminidb import TMiniDB

# The comparisons a test makes live in `tests.utils`, which is not a test file
# and so is not rewritten to report what differed unless it is asked for.
pytest.register_assert_rewrite("tests.utils")

ACCESS_TOKEN_CREDENTIAL = "TMDB_ACCESS_TOKEN"  # noqa: S105


# TODO: Validate
@pytest.fixture(scope="session")
def client() -> TMiniDB:
    return TMiniDB(get_credential(ACCESS_TOKEN_CREDENTIAL))
