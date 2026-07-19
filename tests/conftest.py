# TODO: Validate
import pytest

from tminidb import Tminidb


@pytest.fixture(scope="session")
def client() -> Tminidb:
    return Tminidb()
