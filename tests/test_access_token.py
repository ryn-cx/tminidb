# TODO: Validate
"""What happens to a client whose access token TMDB will not accept.

The token is read in `download`, which every endpoint goes through, so one
endpoint standing in for all of them is enough: what is being checked is the
token rather than the thing asked about.

A refusal is not a response, so there is nothing to record here.
"""

from __future__ import annotations

import pytest

from tminidb import TMiniDB
from tminidb.exceptions import HTTPError

MOVIE_ID = 603
"""The Matrix, which is only here to give the request something to ask about."""

INVALID_KEY = 7
"""What TMDB files an unusable token under, in its own numbering rather than HTTP's."""


# TODO: Validate
class TestInvalidAccessToken:
    """A token TMDB does not know is refused rather than answered."""

    ACCESS_TOKEN = "not-a-real-token"  # noqa: S105 - A token it refuses is the point.

    # TODO: Validate
    def test_download(self) -> None:
        client = TMiniDB(self.ACCESS_TOKEN)

        with pytest.raises(HTTPError) as error:
            client.movies.details(MOVIE_ID)

        assert error.value.status_code == 401  # noqa: PLR2004 - The code is the point.
        body = error.value.response.json()
        assert body["success"] is False
        # TMDB answers with a numbering of its own alongside the status code,
        # and it is the one that says which of the 401s this is.
        assert body["status_code"] == INVALID_KEY


# TODO: Validate
class TestMissingAccessToken:
    """A client given no token is refused before anything is asked of the API.

    Nothing is downloaded here, so unlike the rest of these tests it says the
    same thing whether or not there is a network to reach TMDB over.
    """

    # TODO: Validate
    @pytest.mark.parametrize("access_token", ["", " ", "\t\n"])
    def test_build(self, access_token: str) -> None:
        with pytest.raises(ValueError, match="access token"):
            TMiniDB(access_token)
