# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import record_test, recorded_content
from tminidb.exceptions import HTTPError
from tminidb.movies.details import MovieDetails
from tminidb.movies.details.models import (
    Collection,
    Genre,
    Movie,
    ProductionCompany,
    ProductionCountry,
    SpokenLanguage,
)

if TYPE_CHECKING:
    from tminidb import TMiniDB


# TODO: Validate
class TestMovie:
    MOVIE_ID = 603
    TITLE = "The Matrix"
    RELEASE_DATE = "1999-03-31"
    RUNTIME = 136
    IMDB_ID = "tt0133093"

    # TODO: Validate
    def test_download(self, client: TMiniDB) -> None:
        record_test(
            MovieDetails,
            str(self.MOVIE_ID),
            lambda: client.movies.details(self.MOVIE_ID).raw,
        )

    # TODO: Validate
    def test_parse(self) -> None:
        # The whole of what the response is read into, written out rather than
        # picked at, so anything that changes about it is a failure rather than
        # something no assertion happened to look at. `raw` being the response
        # it was read from is what says it still gives back what it was given.
        data = recorded_content(MovieDetails, str(self.MOVIE_ID))

        assert Movie.from_response(data) == Movie(
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
                ProductionCompany(**company) for company in data["production_companies"]
            ),
            production_countries=tuple(
                ProductionCountry(**country) for country in data["production_countries"]
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
class TestSparseMovie:
    # A movie with almost nothing filled in: no release date, no IMDb id and no
    # runtime, which is where the fields a well known movie never shows as
    # empty get covered.
    MOVIE_ID = 1466882

    # TODO: Validate
    def test_download(self, client: TMiniDB) -> None:
        record_test(
            MovieDetails,
            str(self.MOVIE_ID),
            lambda: client.movies.details(self.MOVIE_ID).raw,
        )

    # TODO: Validate
    def test_parse(self) -> None:
        data = recorded_content(MovieDetails, str(self.MOVIE_ID))

        assert Movie.from_response(data) == Movie(
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
        assert error.value.response["success"] is False
