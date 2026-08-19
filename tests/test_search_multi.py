# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

from tests.utils import record_test, recorded_content
from tminidb.search.multi import SearchMulti
from tminidb.search.multi.models import MultiResult, MultiSearchResults

if TYPE_CHECKING:
    from tminidb import TMiniDB


# TODO: Validate
class TestMovieMatch:
    # A query that matches exactly one thing, and that thing a movie, so the
    # whole page can be written out and the `title` branch of the reading is
    # the one that runs.
    QUERY = "Accidental Partners"
    MOVIE_ID = 1632181

    # TODO: Validate
    def test_download(self, client: TMiniDB) -> None:
        record_test(
            SearchMulti,
            self.QUERY,
            lambda: client.search.multi(self.QUERY).raw,
        )

    # TODO: Validate
    def test_parse(self) -> None:
        data = recorded_content(SearchMulti, self.QUERY)

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
class TestTvMatch:
    # A series and a movie sharing a name, so both branches of the reading run
    # inside one page and a `name` cannot quietly be read where a `title` was
    # meant.
    QUERY = "Teach You a Lesson"
    SERIES_ID = 276161
    MOVIE_ID = 896977

    # TODO: Validate
    def test_download(self, client: TMiniDB) -> None:
        record_test(
            SearchMulti,
            self.QUERY,
            lambda: client.search.multi(self.QUERY).raw,
        )

    # TODO: Validate
    def test_parse(self) -> None:
        data = recorded_content(SearchMulti, self.QUERY)

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
class TestPersonMatch:
    # A person, which is the third kind of thing this endpoint answers with and
    # the one that carries neither a date nor a title.
    QUERY = "Anoushka"
    PERSON_ID = 5256874

    # TODO: Validate
    def test_download(self, client: TMiniDB) -> None:
        record_test(
            SearchMulti,
            self.QUERY,
            lambda: client.search.multi(self.QUERY).raw,
        )

    # TODO: Validate
    def test_parse(self) -> None:
        data = recorded_content(SearchMulti, self.QUERY)

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
class TestNoMatches:
    QUERY = "1234567890qwertyuiopasdfghjklzxcvbnm"

    # TODO: Validate
    def test_download(self, client: TMiniDB) -> None:
        record_test(
            SearchMulti,
            self.QUERY,
            lambda: client.search.multi(self.QUERY).raw,
        )

    # TODO: Validate
    def test_parse(self) -> None:
        # A search nothing matches is a page rather than an error, so an empty
        # result says only that nothing matched.
        data = recorded_content(SearchMulti, self.QUERY)

        assert MultiSearchResults.from_response(data) == MultiSearchResults(
            page=1,
            # A page count of one rather than zero: the API answers an empty
            # search with one empty page rather than with no pages at all.
            total_pages=1,
            total_results=0,
            results=(),
            raw=data,
        )
