# TODO: Validate
"""Every endpoint the API's docs file under TV Series."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, ClassVar

import pytest

from tests.utils import RecordedEndpoint
from tminidb.exceptions import HTTPError
from tminidb.tv_series import TvSeriesEndpoints

if TYPE_CHECKING:
    from tminidb import TMiniDB


INVALID_SERIES_IDS = [pytest.param(0), pytest.param(999999999)]
"""Ids no series is ever going to have.

Zero stands for everything from -2147483648 up to it, which is refused the same
way, and the other is a number in range that no series has been given.
"""


# TODO: Validate
class BaseTVSeriesTest(RecordedEndpoint):
    ENDPOINT = TvSeriesEndpoints


# TODO: Validate
class TestChanges:
    """Test `tv_series.changes`."""

    # TODO: Validate
    class BaseChangesTest(BaseTVSeriesTest):
        SERIES_ID = 108978
        """Most popular TV series at the time of writing this test
        https://www.themoviedb.org/tv/108978-reacher"""

        def test_parse(self, client: TMiniDB) -> None:
            self.parse_test(self.SERIES_ID, client.tv_series.load_changes)

    class TestResponseWithChanges(BaseChangesTest):
        def test_download(self, client: TMiniDB) -> None:
            self.record_test(
                self.SERIES_ID,
                lambda: (
                    client.tv_series.changes(
                        self.SERIES_ID,
                        start_date=date(2026, 8, 18),
                    ).raw
                ),
            )

    class TestMergedResponseWithChanges(BaseChangesTest):
        def test_download(self, client: TMiniDB) -> None:
            self.record_test(
                self.SERIES_ID,
                lambda: (
                    client.tv_series.changes(
                        self.SERIES_ID,
                        start_date=date(2026, 7, 22),
                        end_date=date(2026, 8, 18),
                    ).raw
                ),
            )

    class TestResponseWithoutChanges(BaseChangesTest):
        def test_download(self, client: TMiniDB) -> None:
            self.record_test(
                self.SERIES_ID,
                lambda: (
                    client.tv_series.changes(
                        self.SERIES_ID,
                        start_date=date(2026, 1, 1),
                        end_date=date(2026, 1, 1),
                    ).raw
                ),
            )

    class TestInvalidSeriesID:
        SERIES_ID = 0
        """Values between -2147483648 and 0 return a 404 error."""

        def test_download(self, client: TMiniDB) -> None:
            with pytest.raises(HTTPError) as error:
                client.tv_series.changes(self.SERIES_ID)

            assert error.value.status_code == 404  # noqa: PLR2004
            assert error.value.response.json()["success"] is False

    class TestUnusedSeriesID(BaseChangesTest):
        SERIES_ID = 2147483647
        """Maximum possible series ID."""

        def test_download(self, client: TMiniDB) -> None:
            self.record_test(
                self.SERIES_ID,
                lambda: client.tv_series.changes(self.SERIES_ID).raw,
            )


class TestDetails:
    """Test `tv_series.details`."""

    class BaseDetailsTest(BaseTVSeriesTest):
        SERIES_ID: ClassVar[int]

        def test_download(self, client: TMiniDB) -> None:
            self.record_test(
                self.SERIES_ID,
                lambda: client.tv_series.details(self.SERIES_ID).raw,
            )

        def test_parse(self, client: TMiniDB) -> None:
            self.parse_test(self.SERIES_ID, client.tv_series.load_details)

    class TestFinishedSeries(BaseDetailsTest):
        SERIES_ID = 1

    @pytest.mark.parametrize("series_id", INVALID_SERIES_IDS)
    def test_invalid(self, client: TMiniDB, series_id: int) -> None:
        with pytest.raises(HTTPError) as error:
            client.tv_series.details(series_id)

        assert error.value.status_code == 404  # noqa: PLR2004


# TODO: Validate
class TestEpisodeGroups:
    """Test `tv_series.episode_groups`."""

    # TODO: Validate
    class TestSeries(BaseTVSeriesTest):
        SERIES_ID = 1416
        """Most popular TV series at the time of writing this test with episode groups.
        https://www.themoviedb.org/tv/1416-grey-s-anatomy?language=en-US"""

        def test_download(self, client: TMiniDB) -> None:
            self.record_test(
                self.SERIES_ID,
                lambda: client.tv_series.episode_groups(self.SERIES_ID).raw,
            )

        def test_parse(self, client: TMiniDB) -> None:
            self.parse_test(self.SERIES_ID, client.tv_series.load_episode_groups)


    # TODO: Validate
    class TestInvalidSeriesID:
        # An id no series has is refused rather than answered with an empty list
        # of groupings, so there is no response to record.

        # TODO: Validate
        @pytest.mark.parametrize("series_id", INVALID_SERIES_IDS)
        def test_invalid(self, client: TMiniDB, series_id: int) -> None:
            with pytest.raises(HTTPError) as error:
                client.tv_series.episode_groups(series_id)

            assert error.value.status_code == 404  # noqa: PLR2004
            assert error.value.response.json()["success"] is False


# TODO: Validate
class TestWatchProviders:
    """Test `tv_series.watch_providers`."""

    # TODO: Validate
    class TestSeries(BaseTVSeriesTest):
        SERIES_ID = 1396

        # TODO: Validate
        def test_download(self, client: TMiniDB) -> None:
            self.record_test(
                self.SERIES_ID,
                lambda: client.tv_series.watch_providers(self.SERIES_ID).raw,
            )

        # TODO: Validate
        def test_parse(self, client: TMiniDB) -> None:
            self.parse_test(self.SERIES_ID, client.tv_series.load_watch_providers)

    # TODO: Validate
    class TestInvalidSeriesID:
        # An id no series has is refused rather than answered with an empty list
        # of countries, so there is no response to record.

        # TODO: Validate
        @pytest.mark.parametrize("series_id", INVALID_SERIES_IDS)
        def test_invalid(self, client: TMiniDB, series_id: int) -> None:
            with pytest.raises(HTTPError) as error:
                client.tv_series.watch_providers(series_id)

            assert error.value.status_code == 404  # noqa: PLR2004
            assert error.value.response.json()["success"] is False
