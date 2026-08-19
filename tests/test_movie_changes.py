from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING

import pytest

from tests.utils import parse_test, record_test, recorded_content
from tminidb.exceptions import HTTPError
from tminidb.movies.changes import MovieChanges
from tminidb.movies.changes.models import MovieChangeLog

if TYPE_CHECKING:
    from tminidb import TMiniDB

# Most popular movie at the time of writing this test
# https://www.themoviedb.org/movie/969681-spider-man-brand-new-day
MOVIE_ID = 969681


# TODO: Validate
class TestResponseWithChanges:
    def test_download(self, client: TMiniDB) -> None:
        record_test(
            MovieChanges,
            str(MOVIE_ID),
            lambda: (
                client.movies.changes(
                    MOVIE_ID,
                    start_date=date(2026, 8, 18),
                ).raw
            ),
        )

    def test_parse(self) -> None:
        parse_test(MovieChanges, str(MOVIE_ID), MovieChangeLog)


class TestMergedResponseWithChanges:
    def test_download(self, client: TMiniDB) -> None:
        record_test(
            MovieChanges,
            str(MOVIE_ID),
            lambda: (
                client.movies.changes(
                    MOVIE_ID,
                    start_date=date(2026, 7, 22),
                    end_date=date(2026, 8, 18),
                ).raw
            ),
        )

    def test_parse(self) -> None:
        parse_test(MovieChanges, str(MOVIE_ID), MovieChangeLog)


class TestResponseWithoutChanges:
    def test_download(self, client: TMiniDB) -> None:
        record_test(
            MovieChanges,
            str(MOVIE_ID),
            lambda: (
                client.movies.changes(
                    MOVIE_ID,
                    start_date=date(2026, 1, 1),
                    end_date=date(2026, 1, 1),
                ).raw
            ),
        )

    def test_parse(self) -> None:
        data = recorded_content(MovieChanges, str(MOVIE_ID))

        assert MovieChangeLog.from_response(data) == MovieChangeLog(
            changes=(),
            raw=data,
        )


class TestInvalidMovieID:
    """Values between -2147483648 and 0 return a 404 error."""
    MOVIE_ID = 0

    def test_download(self, client: TMiniDB) -> None:
        with pytest.raises(HTTPError) as error:
            client.movies.changes(self.MOVIE_ID)

        assert error.value.status_code == 404  # noqa: PLR2004
        assert error.value.response["success"] is False


class TestUnusedMovieID:
    MOVIE_ID = 2147483647

    def test_download(self, client: TMiniDB) -> None:
        record_test(
            MovieChanges,
            str(self.MOVIE_ID),
            lambda: client.movies.changes(self.MOVIE_ID).raw,
        )

    def test_parse(self) -> None:
        data = recorded_content(MovieChanges, str(self.MOVIE_ID))

        assert MovieChangeLog.from_response(data) == MovieChangeLog(
            changes=(),
            raw=data,
        )
