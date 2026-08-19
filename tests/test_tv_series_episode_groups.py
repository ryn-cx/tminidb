# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import record_test, recorded_content
from tminidb.exceptions import HTTPError
from tminidb.tv_series.episode_groups import TvSeriesEpisodeGroups
from tminidb.tv_series.episode_groups.models import EpisodeGroups, EpisodeGroupSummary

if TYPE_CHECKING:
    from tminidb import TMiniDB


# TODO: Validate
class TestSeries:
    # A series people have reordered several ways over, so there is more than
    # one grouping to list.
    SERIES_ID = 37854

    # TODO: Validate
    def test_download(self, client: TMiniDB) -> None:
        record_test(
            TvSeriesEpisodeGroups,
            str(self.SERIES_ID),
            lambda: client.tv_series.episode_groups(self.SERIES_ID).raw,
        )

    # TODO: Validate
    def test_parse(self) -> None:
        # The whole of what the response is read into, in one comparison.
        # Anyone can add a grouping and a long-running show keeps gaining
        # episodes, so the rows are read back from the response rather than
        # pinned to counts that go stale.
        data = recorded_content(TvSeriesEpisodeGroups, str(self.SERIES_ID))

        assert EpisodeGroups.from_response(data) == EpisodeGroups(
            id=self.SERIES_ID,
            results=tuple(EpisodeGroupSummary(**item) for item in data["results"]),
            raw=data,
        )
        assert EpisodeGroups.from_response(data).results


# TODO: Validate
class TestUnknownSeries:
    SERIES_ID = 999999999

    # TODO: Validate
    def test_download(self, client: TMiniDB) -> None:
        # An id that belongs to no series is refused rather than answered with
        # an empty list of groupings, so there is no response to record.
        with pytest.raises(HTTPError) as error:
            client.tv_series.episode_groups(self.SERIES_ID)

        assert error.value.status_code == 404  # noqa: PLR2004
        assert error.value.response["success"] is False
