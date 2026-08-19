# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

from tests.utils import record_test, recorded_content
from tminidb.search.movie import SearchMovie
from tminidb.search.movie.models import MovieResult, MovieSearchResults

if TYPE_CHECKING:
    from tminidb import TMiniDB


# TODO: Validate
class TestMatches:
    QUERY = "The Matrix"
    FIRST_ID = 603
    FIRST_TITLE = "The Matrix"
    FIRST_RELEASE_DATE = "1999-03-31"

    # TODO: Validate
    def test_download(self, client: TMiniDB) -> None:
        record_test(
            SearchMovie,
            self.QUERY,
            lambda: client.search.movie(self.QUERY).raw,
        )

    # TODO: Validate
    def test_parse(self) -> None:
        # The whole of what the response is read into, written out rather than
        # picked at, so anything that changes about it is a failure rather than
        # something no assertion happened to look at. A page holds twenty
        # results and which ones they are moves as the API reranks, so the rows
        # are read back from the response and only the first, which is the
        # exact title that was searched for, is written out.
        data = recorded_content(SearchMovie, self.QUERY)

        assert MovieSearchResults.from_response(data) == MovieSearchResults(
            page=data["page"],
            total_pages=data["total_pages"],
            total_results=data["total_results"],
            results=(
                MovieResult(
                    adult=False,
                    backdrop_path=data["results"][0]["backdrop_path"],
                    genre_ids=(28, 878),
                    id=self.FIRST_ID,
                    original_language="en",
                    original_title=self.FIRST_TITLE,
                    overview=data["results"][0]["overview"],
                    popularity=data["results"][0]["popularity"],
                    poster_path=data["results"][0]["poster_path"],
                    release_date=self.FIRST_RELEASE_DATE,
                    title=self.FIRST_TITLE,
                    video=False,
                    vote_average=data["results"][0]["vote_average"],
                    vote_count=data["results"][0]["vote_count"],
                ),
                *(MovieResult(**item) for item in data["results"][1:]),
            ),
            raw=data,
        )


# TODO: Validate
class TestNoMatches:
    QUERY = "1234567890qwertyuiopasdfghjklzxcvbnm"

    # TODO: Validate
    def test_download(self, client: TMiniDB) -> None:
        record_test(
            SearchMovie,
            self.QUERY,
            lambda: client.search.movie(self.QUERY).raw,
        )

    # TODO: Validate
    def test_parse(self) -> None:
        # A search nothing matches is a page rather than an error, so an empty
        # result says only that nothing matched.
        data = recorded_content(SearchMovie, self.QUERY)

        assert MovieSearchResults.from_response(data) == MovieSearchResults(
            page=1,
            # A page count of one rather than zero: the API answers an empty
            # search with one empty page rather than with no pages at all.
            total_pages=1,
            total_results=0,
            results=(),
            raw=data,
        )
