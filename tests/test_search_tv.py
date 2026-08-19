# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

from tests.utils import record_test, recorded_content
from tminidb.search.tv import SearchTv
from tminidb.search.tv.models import TvResult, TvSearchResults

if TYPE_CHECKING:
    from tminidb import TMiniDB


# TODO: Validate
class TestMatches:
    QUERY = "Breaking Bad"
    FIRST_ID = 1396
    FIRST_NAME = "Breaking Bad"
    FIRST_AIR_DATE = "2008-01-20"

    # TODO: Validate
    def test_download(self, client: TMiniDB) -> None:
        record_test(SearchTv, self.QUERY, lambda: client.search.tv(self.QUERY).raw)

    # TODO: Validate
    def test_parse(self) -> None:
        # The whole of what the response is read into, written out rather than
        # picked at. Which of the twenty rows come back moves as the API
        # reranks, so they are read from the response and only the first, which
        # is the exact name that was searched for, is written out.
        data = recorded_content(SearchTv, self.QUERY)

        assert TvSearchResults.from_response(data) == TvSearchResults(
            page=data["page"],
            total_pages=data["total_pages"],
            total_results=data["total_results"],
            results=(
                TvResult(
                    adult=False,
                    backdrop_path=data["results"][0]["backdrop_path"],
                    genre_ids=(18, 80),
                    id=self.FIRST_ID,
                    origin_country=("US",),
                    original_language="en",
                    original_name=self.FIRST_NAME,
                    overview=data["results"][0]["overview"],
                    popularity=data["results"][0]["popularity"],
                    poster_path=data["results"][0]["poster_path"],
                    first_air_date=self.FIRST_AIR_DATE,
                    name=self.FIRST_NAME,
                    vote_average=data["results"][0]["vote_average"],
                    vote_count=data["results"][0]["vote_count"],
                ),
                *(TvResult(**item) for item in data["results"][1:]),
            ),
            raw=data,
        )


# TODO: Validate
class TestNoMatches:
    QUERY = "1234567890qwertyuiopasdfghjklzxcvbnm"

    # TODO: Validate
    def test_download(self, client: TMiniDB) -> None:
        record_test(SearchTv, self.QUERY, lambda: client.search.tv(self.QUERY).raw)

    # TODO: Validate
    def test_parse(self) -> None:
        # A search nothing matches is a page rather than an error, so an empty
        # result says only that nothing matched.
        data = recorded_content(SearchTv, self.QUERY)

        assert TvSearchResults.from_response(data) == TvSearchResults(
            page=1,
            # A page count of one rather than zero: the API answers an empty
            # search with one empty page rather than with no pages at all.
            total_pages=1,
            total_results=0,
            results=(),
            raw=data,
        )
