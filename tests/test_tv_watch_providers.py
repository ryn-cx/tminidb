# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING, Any

import pytest

from tests.utils import record_test, recorded_content
from tminidb.exceptions import HTTPError
from tminidb.tv_series.watch_providers import TvWatchProviders
from tminidb.tv_series.watch_providers.models import (
    CountryProviders,
    Provider,
    Results,
    TvProviders,
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
class TestSeries:
    SERIES_ID = 1396

    # TODO: Validate
    def test_download(self, client: TMiniDB) -> None:
        record_test(
            TvWatchProviders,
            str(self.SERIES_ID),
            lambda: client.tv_series.watch_providers(self.SERIES_ID).raw,
        )

    # TODO: Validate
    def test_parse(self) -> None:
        # The whole of what the response is read into, in one comparison. Which
        # service carries a series where changes week to week, so the rows are
        # read back from the response: what is checked is that every country is
        # there, under the code it was filed under, with every way of paying
        # for it kept apart and none of them dropped.
        data = recorded_content(TvWatchProviders, str(self.SERIES_ID))

        assert TvProviders.from_response(data) == TvProviders(
            id=self.SERIES_ID,
            results=_expected_results(data),
            raw=data,
        )


# TODO: Validate
class TestUnknownSeries:
    SERIES_ID = 999999999

    # TODO: Validate
    def test_download(self, client: TMiniDB) -> None:
        # An id that belongs to no series is refused rather than answered with
        # an empty list of countries, so there is no response to record.
        with pytest.raises(HTTPError) as error:
            client.tv_series.watch_providers(self.SERIES_ID)

        assert error.value.status_code == 404  # noqa: PLR2004
        assert error.value.response["success"] is False
