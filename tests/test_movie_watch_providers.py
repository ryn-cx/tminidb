# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING, Any

import pytest

from tests.utils import record_test, recorded_content
from tminidb.exceptions import HTTPError
from tminidb.movies.watch_providers import MovieWatchProviders
from tminidb.movies.watch_providers.models import (
    CountryProviders,
    MovieProviders,
    Provider,
    Results,
)

if TYPE_CHECKING:
    from tminidb import TMiniDB


# TODO: Validate
def _expected_results(data: dict[str, Any]) -> Results:
    """Every country in the response, read back into the field it belongs in.

    A country is a field of its own rather than a row, so the codes the
    response was filed under are what say which fields should be filled in, and
    every field not named here is left as None.
    """
    return Results(
        **{
            code: CountryProviders(
                link=entry["link"],
                **{
                    kind: tuple(Provider(**offer) for offer in offers)
                    for kind, offers in entry.items()
                    if kind != "link"
                },
            )
            for code, entry in data["results"].items()
        },
    )


# TODO: Validate
class TestMovie:
    MOVIE_ID = 603

    # TODO: Validate
    def test_download(self, client: TMiniDB) -> None:
        record_test(
            MovieWatchProviders,
            str(self.MOVIE_ID),
            lambda: client.movies.watch_providers(self.MOVIE_ID).raw,
        )

    # TODO: Validate
    def test_parse(self) -> None:
        # The whole of what the response is read into, in one comparison. A
        # popular movie is on offer in a hundred-odd countries and which
        # service carries it where changes week to week, so the rows are read
        # back from the response: what is being checked is that every country
        # is there, under the code it was filed under, with every way of paying
        # for it kept apart and none of them dropped.
        data = recorded_content(MovieWatchProviders, str(self.MOVIE_ID))

        assert MovieProviders.from_response(data) == MovieProviders(
            id=self.MOVIE_ID,
            results=_expected_results(data),
            raw=data,
        )


# TODO: Validate
class TestUnknownMovie:
    MOVIE_ID = 999999999

    # TODO: Validate
    def test_download(self, client: TMiniDB) -> None:
        # An id that belongs to no movie is refused rather than answered with
        # an empty list of countries, so there is no response to record.
        with pytest.raises(HTTPError) as error:
            client.movies.watch_providers(self.MOVIE_ID)

        assert error.value.status_code == 404  # noqa: PLR2004
        assert error.value.response["success"] is False
