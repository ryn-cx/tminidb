# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import record_test, recorded_content
from tminidb.exceptions import HTTPError
from tminidb.tv_episodes.details import TvEpisodeDetails
from tminidb.tv_episodes.details.models import CrewMember, GuestStar, Details

if TYPE_CHECKING:
    from tminidb import TMiniDB


# TODO: Validate
class TestEpisode:
    SERIES_ID = 1396
    SEASON_NUMBER = 1
    EPISODE_NUMBER = 1
    NAME = "1396_1_1"
    EPISODE_ID = 62085
    TITLE = "Pilot"
    AIR_DATE = "2008-01-20"

    # TODO: Validate
    def test_download(self, client: TMiniDB) -> None:
        record_test(
            TvEpisodeDetails,
            self.NAME,
            lambda: (
                client.tv_episodes.details(
                    self.SERIES_ID,
                    self.SEASON_NUMBER,
                    self.EPISODE_NUMBER,
                ).raw
            ),
        )

    # TODO: Validate
    def test_parse(self) -> None:
        # The whole of what the response is read into, written out rather than
        # picked at, so anything that changes about it is a failure rather than
        # something no assertion happened to look at.
        data = recorded_content(TvEpisodeDetails, self.NAME)

        assert Details.from_response(data) == Details(
            air_date=self.AIR_DATE,
            # Who is credited on an episode is added to as people go through
            # it, so the two lists of people are read back from the response.
            crew=tuple(CrewMember(**member) for member in data["crew"]),
            episode_number=self.EPISODE_NUMBER,
            episode_type="standard",
            guest_stars=tuple(GuestStar(**star) for star in data["guest_stars"]),
            name=self.TITLE,
            # Runtimes and summaries are re-edited on TMDB, so pinning them
            # would fail for a reason that is nothing to do with the reading.
            overview=data["overview"],
            id=self.EPISODE_ID,
            production_code=data["production_code"],
            runtime=data["runtime"],
            season_number=self.SEASON_NUMBER,
            still_path=data["still_path"],
            vote_average=data["vote_average"],
            vote_count=data["vote_count"],
            raw=data,
        )


# TODO: Validate
class TestUnknownEpisode:
    SERIES_ID = 1396
    SEASON_NUMBER = 1
    EPISODE_NUMBER = 99

    # TODO: Validate
    def test_download(self, client: TMiniDB) -> None:
        # An episode number a real season does not have is refused rather than
        # answered with an empty episode, so there is no response to record.
        with pytest.raises(HTTPError) as error:
            client.tv_episodes.details(
                self.SERIES_ID,
                self.SEASON_NUMBER,
                self.EPISODE_NUMBER,
            )

        assert error.value.status_code == 404  # noqa: PLR2004
        assert error.value.response["success"] is False


# TODO: Validate
class TestUnknownSeries:
    SERIES_ID = 999999999
    SEASON_NUMBER = 1
    EPISODE_NUMBER = 1

    # TODO: Validate
    def test_download(self, client: TMiniDB) -> None:
        with pytest.raises(HTTPError) as error:
            client.tv_episodes.details(
                self.SERIES_ID,
                self.SEASON_NUMBER,
                self.EPISODE_NUMBER,
            )

        assert error.value.status_code == 404  # noqa: PLR2004
