# TODO: Validate
"""Every endpoint the API's docs file under Search."""

from __future__ import annotations

from typing import TYPE_CHECKING

from tests.utils import RecordedEndpoint
from tminidb.search import SearchEndpoints
from tminidb.search.models.movie import MovieResult, MovieSearchResults
from tminidb.search.models.multi import MultiResult, MultiSearchResults
from tminidb.search.models.tv import TvResult, TvSearchResults

if TYPE_CHECKING:
    from tminidb import TMiniDB


# TODO: Validate
class SearchTest(RecordedEndpoint):
    ENDPOINT = SearchEndpoints


# TODO: Validate
class TestMovie:
    """Test `search.movie`."""

    # TODO: Validate
    class TestMatches(SearchTest):
        QUERY = "The Matrix"
        FIRST_ID = 603
        FIRST_TITLE = "The Matrix"
        FIRST_RELEASE_DATE = "1999-03-31"

        # TODO: Validate
        def test_download(self, client: TMiniDB) -> None:
            self.record_test(
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
            data = self.recorded_content(self.QUERY)

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
    class TestNoMatches(SearchTest):
        QUERY = "1234567890qwertyuiopasdfghjklzxcvbnm"

        # TODO: Validate
        def test_download(self, client: TMiniDB) -> None:
            self.record_test(
                self.QUERY,
                lambda: client.search.movie(self.QUERY).raw,
            )

        # TODO: Validate
        def test_parse(self) -> None:
            # A search nothing matches is a page rather than an error, so an empty
            # result says only that nothing matched.
            data = self.recorded_content(self.QUERY)

            assert MovieSearchResults.from_response(data) == MovieSearchResults(
                page=1,
                # A page count of one rather than zero: the API answers an empty
                # search with one empty page rather than with no pages at all.
                total_pages=1,
                total_results=0,
                results=(),
                raw=data,
            )


# TODO: Validate
class TestMulti:
    """Test `search.multi`."""

    # TODO: Validate
    class TestMovieMatch(SearchTest):
        # A query that matches exactly one thing, and that thing a movie, so the
        # whole page can be written out and the `title` branch of the reading is
        # the one that runs.
        QUERY = "Accidental Partners"
        MOVIE_ID = 1632181

        # TODO: Validate
        def test_download(self, client: TMiniDB) -> None:
            self.record_test(
                self.QUERY,
                lambda: client.search.multi(self.QUERY).raw,
            )

        # TODO: Validate
        def test_parse(self) -> None:
            data = self.recorded_content(self.QUERY)

            results = MultiSearchResults.from_response(data)

            assert results == MultiSearchResults(
                page=1,
                total_pages=1,
                total_results=1,
                results=(MultiResult(**data["results"][0]),),
                raw=data,
            )
            # A movie fills in `title` and leaves `name` out, and the reading keeps
            # the two apart rather than answering with whichever it found.
            assert results.results[0].id == self.MOVIE_ID
            assert results.results[0].media_type == "movie"
            assert results.results[0].title == self.QUERY
            assert results.results[0].name == ""

    # TODO: Validate
    class TestTvMatch(SearchTest):
        # A series and a movie sharing a name, so both branches of the reading run
        # inside one page and a `name` cannot quietly be read where a `title` was
        # meant.
        QUERY = "Teach You a Lesson"
        SERIES_ID = 276161
        MOVIE_ID = 896977

        # TODO: Validate
        def test_download(self, client: TMiniDB) -> None:
            self.record_test(
                self.QUERY,
                lambda: client.search.multi(self.QUERY).raw,
            )

        # TODO: Validate
        def test_parse(self) -> None:
            data = self.recorded_content(self.QUERY)

            results = MultiSearchResults.from_response(data)

            assert results == MultiSearchResults(
                page=1,
                total_pages=1,
                total_results=2,
                results=tuple(MultiResult(**item) for item in data["results"]),
                raw=data,
            )
            # The series is named and the movie is titled, and neither is read into
            # the other's field.
            series, movie = results.results
            assert (series.id, series.media_type) == (self.SERIES_ID, "tv")
            assert (series.name, series.title) == (self.QUERY, "")
            assert (movie.id, movie.media_type) == (self.MOVIE_ID, "movie")
            assert (movie.title, movie.name) == (self.QUERY, "")

    # TODO: Validate
    class TestPersonMatch(SearchTest):
        # A person, which is the third kind of thing this endpoint answers with and
        # the one that carries neither a date nor a title.
        QUERY = "Anoushka"
        PERSON_ID = 5256874

        # TODO: Validate
        def test_download(self, client: TMiniDB) -> None:
            self.record_test(
                self.QUERY,
                lambda: client.search.multi(self.QUERY).raw,
            )

        # TODO: Validate
        def test_parse(self) -> None:
            data = self.recorded_content(self.QUERY)

            results = MultiSearchResults.from_response(data)

            assert results == MultiSearchResults(
                page=data["page"],
                total_pages=data["total_pages"],
                total_results=data["total_results"],
                # A common first name matches dozens of people and the ranking
                # moves, so the rows are read back from the response and only the
                # top match is written out.
                results=tuple(MultiResult(**item) for item in data["results"]),
                raw=data,
            )
            # A person is named and carries neither a title nor a date, so the
            # fields the other two kinds fill in are empty here.
            person = results.results[0]
            assert (person.id, person.media_type) == (self.PERSON_ID, "person")
            assert (person.name, person.title) == (self.QUERY, "")
            assert (person.release_date, person.first_air_date) == ("", "")

    # TODO: Validate
    class TestNoMatches(SearchTest):
        QUERY = "1234567890qwertyuiopasdfghjklzxcvbnm"

        # TODO: Validate
        def test_download(self, client: TMiniDB) -> None:
            self.record_test(
                self.QUERY,
                lambda: client.search.multi(self.QUERY).raw,
            )

        # TODO: Validate
        def test_parse(self) -> None:
            # A search nothing matches is a page rather than an error, so an empty
            # result says only that nothing matched.
            data = self.recorded_content(self.QUERY)

            assert MultiSearchResults.from_response(data) == MultiSearchResults(
                page=1,
                # A page count of one rather than zero: the API answers an empty
                # search with one empty page rather than with no pages at all.
                total_pages=1,
                total_results=0,
                results=(),
                raw=data,
            )


# TODO: Validate
class TestTv:
    """Test `search.tv`."""

    # TODO: Validate
    class TestMatches(SearchTest):
        QUERY = "Breaking Bad"
        FIRST_ID = 1396
        FIRST_NAME = "Breaking Bad"
        FIRST_AIR_DATE = "2008-01-20"

        # TODO: Validate
        def test_download(self, client: TMiniDB) -> None:
            self.record_test(self.QUERY, lambda: client.search.tv(self.QUERY).raw)

        # TODO: Validate
        def test_parse(self) -> None:
            # The whole of what the response is read into, written out rather than
            # picked at. Which of the twenty rows come back moves as the API
            # reranks, so they are read from the response and only the first, which
            # is the exact name that was searched for, is written out.
            data = self.recorded_content(self.QUERY)

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
    class TestNoMatches(SearchTest):
        QUERY = "1234567890qwertyuiopasdfghjklzxcvbnm"

        # TODO: Validate
        def test_download(self, client: TMiniDB) -> None:
            self.record_test(self.QUERY, lambda: client.search.tv(self.QUERY).raw)

        # TODO: Validate
        def test_parse(self) -> None:
            # A search nothing matches is a page rather than an error, so an empty
            # result says only that nothing matched.
            data = self.recorded_content(self.QUERY)

            assert TvSearchResults.from_response(data) == TvSearchResults(
                page=1,
                # A page count of one rather than zero: the API answers an empty
                # search with one empty page rather than with no pages at all.
                total_pages=1,
                total_results=0,
                results=(),
                raw=data,
            )
