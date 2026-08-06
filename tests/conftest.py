# TODO: Validate
import pytest
from get_around import get_credential

from tminidb import TMiniDB

ACCESS_TOKEN_CREDENTIAL = "TMDB_ACCESS_TOKEN"  # noqa: S105


@pytest.fixture(scope="session")
def client() -> TMiniDB:
    return TMiniDB(get_credential(ACCESS_TOKEN_CREDENTIAL))
