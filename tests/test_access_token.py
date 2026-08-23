# TODO: Validate
"""What happens to a client whose access token TMDB will not accept.

The token is read in `download`, which every endpoint goes through, so one
endpoint stands in for all of them.
"""

from __future__ import annotations

import json

import pytest

from tminidb import TMiniDB
from tminidb.exceptions import HTTPError

MOVIE_ID = 603
"""The Matrix, which only gives the request something to ask about."""

INVALID_KEY = 7
"""What TMDB files an unusable token under, in its own numbering rather than HTTP's."""

UNAUTHORIZED = 401


# TODO: Validate
def test_download_with_invalid_token() -> None:
    """A token TMDB does not know is refused rather than answered."""
    client = TMiniDB("not-a-real-token")

    with pytest.raises(HTTPError) as error:
        client.movie.download(MOVIE_ID)

    assert error.value.status_code == UNAUTHORIZED
    body = json.loads(error.value.response or "")
    assert body["success"] is False
    # TMDB answers with a numbering of its own alongside the status code, and it
    # is the one that says which of the 401s this is.
    assert body["status_code"] == INVALID_KEY


# TODO: Validate
@pytest.mark.parametrize("access_token", ["", " ", "\t\n"])
def test_build_without_token(access_token: str) -> None:
    """A client given no token is refused before anything is asked of the API."""
    with pytest.raises(ValueError, match="access token"):
        TMiniDB(access_token)
