# TODO: Validate
"""Every endpoint the API's docs file under Movies."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, Any

import pytest

from tests.utils import RecordedEndpoint
from tminidb.exceptions import HTTPError
from tminidb.movies import MovieEndpoints
from tminidb.movies.models.details import (
    Collection,
    Genre,
    Movie,
    ProductionCompany,
    ProductionCountry,
    SpokenLanguage,
)
from tminidb.movies.models.watch_providers import (
    CountryProviders,
    MovieProviders,
    Provider,
    Results,
)

if TYPE_CHECKING:
    from tminidb import TMiniDB


# TODO: Validate
class MovieTest(RecordedEndpoint):
    ENDPOINT = MovieEndpoints


# TODO: Validate
class TestChanges:
    """Test `movies.changes`."""

    MOVIE_ID = 969681
    """Most popular movie at the time of writing this test
    https://www.themoviedb.org/movie/969681-spider-man-brand-new-day"""

    # TODO: Validate
    class TestResponseWithChanges(MovieTest):
        # TODO: Validate
        def test_download(self, client: TMiniDB) -> None:
            self.record_test(
                TestChanges.MOVIE_ID,
                lambda: (
                    client.movies.changes(
                        TestChanges.MOVIE_ID,
                        start_date=date(2026, 8, 18),
                    ).raw
                ),
            )

        # TODO: Validate
        def test_parse(self, client: TMiniDB) -> None:
            self.parse_test(TestChanges.MOVIE_ID, client.movies.load_changes)

    # TODO: Validate
    class TestMergedResponseWithChanges(MovieTest):
        # TODO: Validate
        def test_download(self, client: TMiniDB) -> None:
            self.record_test(
                TestChanges.MOVIE_ID,
                lambda: (
                    client.movies.changes(
                        TestChanges.MOVIE_ID,
                        start_date=date(2026, 7, 22),
                        end_date=date(2026, 8, 18),
                    ).raw
                ),
            )

        # TODO: Validate
        def test_parse(self, client: TMiniDB) -> None:
            self.parse_test(TestChanges.MOVIE_ID, client.movies.load_changes)

    # TODO: Validate
    class TestResponseWithoutChanges(MovieTest):
        # TODO: Validate
        def test_download(self, client: TMiniDB) -> None:
            self.record_test(
                TestChanges.MOVIE_ID,
                lambda: (
                    client.movies.changes(
                        TestChanges.MOVIE_ID,
                        start_date=date(2026, 1, 1),
                        end_date=date(2026, 1, 1),
                    ).raw
                ),
            )

        # TODO: Validate
        def test_parse(self, client: TMiniDB) -> None:
            self.parse_test(TestChanges.MOVIE_ID, client.movies.load_changes)

    class TestInvalidMovieID:
        """Values between -2147483648 and 0 return a 404 error."""

        MOVIE_ID = 0

        def test_download(self, client: TMiniDB) -> None:
            with pytest.raises(HTTPError) as error:
                client.movies.changes(self.MOVIE_ID)

            assert error.value.status_code == 404  # noqa: PLR2004
            assert error.value.response.json()["success"] is False

    # TODO: Validate
    class TestUnusedMovieID(MovieTest):
        MOVIE_ID = 2147483647

        # TODO: Validate
        def test_download(self, client: TMiniDB) -> None:
            self.record_test(
                self.MOVIE_ID,
                lambda: client.movies.changes(self.MOVIE_ID).raw,
            )

        # TODO: Validate
        def test_parse(self, client: TMiniDB) -> None:
            self.parse_test(self.MOVIE_ID, client.movies.load_changes)


# TODO: Validate
class TestDetails:
    """Test `movies.details`."""

    # TODO: Validate
    class TestMovie(MovieTest):
        MOVIE_ID = 603
        TITLE = "The Matrix"
        RELEASE_DATE = "1999-03-31"
        RUNTIME = 136
        IMDB_ID = "tt0133093"

        # TODO: Validate
        def test_download(self, client: TMiniDB) -> None:
            self.record_test(
                self.MOVIE_ID,
                lambda: client.movies.details(self.MOVIE_ID).raw,
            )

        # TODO: Validate
        def test_parse(self, client: TMiniDB) -> None:
            # The whole of what the response is read into, written out rather than
            # picked at, so anything that changes about it is a failure rather than
            # something no assertion happened to look at. `raw` being the response
            # it was read from is what says it still gives back what it was given.
            data = self.recorded_content(self.MOVIE_ID)

            assert client.movies.load_details(data) == Movie(
                adult=False,
                backdrop_path=data["backdrop_path"],
                belongs_to_collection=Collection(**data["belongs_to_collection"]),
                budget=63000000,
                genres=tuple(Genre(**genre) for genre in data["genres"]),
                homepage=data["homepage"],
                id=self.MOVIE_ID,
                imdb_id=self.IMDB_ID,
                origin_country=("US",),
                original_language="en",
                original_title=self.TITLE,
                # Summaries are rewritten often enough that pinning one would fail
                # for a reason that is nothing to do with the reading.
                overview=data["overview"],
                # Artwork, ratings and how much TMDB is being asked about a movie
                # all move on their own, so they are read back rather than pinned.
                popularity=data["popularity"],
                poster_path=data["poster_path"],
                production_companies=tuple(
                    ProductionCompany(**company)
                    for company in data["production_companies"]
                ),
                production_countries=tuple(
                    ProductionCountry(**country)
                    for country in data["production_countries"]
                ),
                release_date=self.RELEASE_DATE,
                revenue=data["revenue"],
                runtime=self.RUNTIME,
                spoken_languages=tuple(
                    SpokenLanguage(**language) for language in data["spoken_languages"]
                ),
                status="Released",
                tagline=data["tagline"],
                title=self.TITLE,
                video=False,
                vote_average=data["vote_average"],
                vote_count=data["vote_count"],
                raw=data,
            )

    # TODO: Validate
    class TestSparseMovie(MovieTest):
        # A movie with almost nothing filled in: no release date, no IMDb id and no
        # runtime, which is where the fields a well known movie never shows as
        # empty get covered.
        MOVIE_ID = 1466882

        # TODO: Validate
        def test_download(self, client: TMiniDB) -> None:
            self.record_test(
                self.MOVIE_ID,
                lambda: client.movies.details(self.MOVIE_ID).raw,
            )

        # TODO: Validate
        def test_parse(self, client: TMiniDB) -> None:
            data = self.recorded_content(self.MOVIE_ID)

            assert client.movies.load_details(data) == Movie(
                adult=data["adult"],
                backdrop_path=None,
                belongs_to_collection=None,
                budget=0,
                genres=(),
                homepage="",
                id=self.MOVIE_ID,
                imdb_id=None,
                origin_country=tuple(data["origin_country"]),
                original_language=data["original_language"],
                original_title=data["original_title"],
                overview=data["overview"],
                popularity=data["popularity"],
                poster_path=data["poster_path"],
                production_companies=(),
                production_countries=(),
                release_date="",
                revenue=0,
                runtime=data["runtime"],
                spoken_languages=tuple(
                    SpokenLanguage(**language) for language in data["spoken_languages"]
                ),
                status=data["status"],
                tagline="",
                title=data["title"],
                video=data["video"],
                vote_average=data["vote_average"],
                vote_count=data["vote_count"],
                raw=data,
            )

    # TODO: Validate
    class TestUnknownMovie:
        MOVIE_ID = 999999999

        # TODO: Validate
        def test_download(self, client: TMiniDB) -> None:
            # An id that belongs to no movie is refused rather than answered with
            # an empty movie, so there is no response to record.
            with pytest.raises(HTTPError) as error:
                client.movies.details(self.MOVIE_ID)

            assert error.value.status_code == 404  # noqa: PLR2004
            assert error.value.response.json()["success"] is False


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
class TestWatchProviders:
    """Test `movies.watch_providers`."""

    # TODO: Validate
    class TestMovie(MovieTest):
        MOVIE_ID = 603

        # TODO: Validate
        def test_download(self, client: TMiniDB) -> None:
            self.record_test(
                self.MOVIE_ID,
                lambda: client.movies.watch_providers(self.MOVIE_ID).raw,
            )

        # TODO: Validate
        def test_parse(self, client: TMiniDB) -> None:
            # The whole of what the response is read into, in one comparison. A
            # popular movie is on offer in a hundred-odd countries and which
            # service carries it where changes week to week, so the rows are read
            # back from the response: what is being checked is that every country
            # is there, under the code it was filed under, with every way of paying
            # for it kept apart and none of them dropped.
            data = self.recorded_content(self.MOVIE_ID)

            assert client.movies.load_watch_providers(data) == MovieProviders(
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
            assert error.value.response.json()["success"] is False
