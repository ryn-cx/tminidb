# TODO: Validate
import pytest

from tminidb import TMiniDB


@pytest.fixture(scope="session")
def client() -> TMiniDB:
    return TMiniDB()
