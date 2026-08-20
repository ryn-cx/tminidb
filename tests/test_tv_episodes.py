# TODO: Validate
"""Every endpoint the API's docs file under TV Episodes."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING

import pytest

from tests.utils import RecordedEndpoint
from tminidb.exceptions import HTTPError
from tminidb.tv_episodes import TvEpisodeEndpoints
from tminidb.tv_episodes.models.changes import Change, Item, TvEpisodeChangeLog
from tminidb.tv_episodes.models.details import CrewMember, Details, GuestStar
from tminidb.tv_episodes.models.translations import Data, Translation, Translations

if TYPE_CHECKING:
    from tminidb import TMiniDB

# The window is asked for by name rather than left to default to the last 24
# hours, so re-recording a fixture years from now asks for the same days and
# gets the same answer instead of whatever happened yesterday.
START_DATE = date(2026, 8, 10)
END_DATE = date(2026, 8, 18)


# TODO: Validate
class TvEpisodeTest(RecordedEndpoint):
    ENDPOINT = TvEpisodeEndpoints


# TODO: Validate
class TestChanges:
    """Test `tv_episodes.changes`."""

    # TODO: Validate
    class TestEditedRecently(TvEpisodeTest):
        # A episode that had been edited inside the window.
        EPISODE_ID = 7434652
        NAME = "7434652"

        # TODO: Validate
        def test_download(self, client: TMiniDB) -> None:
            self.record_test(
                self.NAME,
                lambda: (
                    client.tv_episodes.changes(
                        self.EPISODE_ID,
                        start_date=START_DATE,
                        end_date=END_DATE,
                    ).raw
                ),
            )

        # TODO: Validate
        def test_parse(self, client: TMiniDB) -> None:
            # The whole of what the response is read into, in one comparison. Which
            # fields were edited and how many times is whatever the editors did
            # that fortnight, so the rows are read back from the response: what is
            # checked is that every group and every edit inside it is carried over,
            # in order, and that an edit keeps the id, action and time that make it
            # readable.
            data = self.recorded_content(self.NAME)

            assert client.tv_episodes.load_changes(data) == TvEpisodeChangeLog(
                changes=tuple(
                    Change(
                        key=group["key"],
                        items=tuple(Item(**item) for item in group["items"]),
                    )
                    for group in data["changes"]
                ),
                raw=data,
            )
            assert client.tv_episodes.load_changes(data).changes

    # TODO: Validate
    class TestUnknownEpisode(TvEpisodeTest):
        # An id that belongs to no episode. It is answered with an empty list
        # rather than with an error, which is the same answer a episode nobody
        # touched gives, so an empty log says nothing about whether the id was good.
        EPISODE_ID = 999999999
        NAME = "unknown_999999999"

        # TODO: Validate
        def test_download(self, client: TMiniDB) -> None:
            self.record_test(
                self.NAME,
                lambda: (
                    client.tv_episodes.changes(
                        self.EPISODE_ID,
                        start_date=START_DATE,
                        end_date=END_DATE,
                    ).raw
                ),
            )

        # TODO: Validate
        def test_parse(self, client: TMiniDB) -> None:
            self.parse_test(self.NAME, client.tv_episodes.load_changes)


# TODO: Validate
class TestDetails:
    """Test `tv_episodes.details`."""

    # TODO: Validate
    class TestEpisode(TvEpisodeTest):
        SERIES_ID = 1396
        SEASON_NUMBER = 1
        EPISODE_NUMBER = 1
        NAME = "1396_1_1"
        EPISODE_ID = 62085
        TITLE = "Pilot"
        AIR_DATE = "2008-01-20"

        # TODO: Validate
        def test_download(self, client: TMiniDB) -> None:
            self.record_test(
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
        def test_parse(self, client: TMiniDB) -> None:
            # The whole of what the response is read into, written out rather than
            # picked at, so anything that changes about it is a failure rather than
            # something no assertion happened to look at.
            data = self.recorded_content(self.NAME)

            assert client.tv_episodes.load_details(data) == Details(
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
            assert error.value.response.json()["success"] is False

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


# TODO: Validate
class TestTranslations:
    """Test `tv_episodes.translations`."""

    # TODO: Validate
    class TestEpisode(TvEpisodeTest):
        SERIES_ID = 1396
        SEASON_NUMBER = 1
        EPISODE_NUMBER = 1
        NAME = "1396_1_1"
        EPISODE_ID = 62085

        # TODO: Validate
        def test_download(self, client: TMiniDB) -> None:
            self.record_test(
                self.NAME,
                lambda: (
                    client.tv_episodes.translations(
                        self.SERIES_ID,
                        self.SEASON_NUMBER,
                        self.EPISODE_NUMBER,
                    ).raw
                ),
            )

        # TODO: Validate
        def test_parse(self, client: TMiniDB) -> None:
            # The whole of what the response is read into, in one comparison. Which
            # languages an episode has been written in grows as people add them, so
            # the rows are read back from the response: what is checked is that
            # each one keeps the language and country it is filed under and the
            # title and summary in the nested `data` object.
            data = self.recorded_content(self.NAME)

            assert client.tv_episodes.load_translations(data) == Translations(
                id=self.EPISODE_ID,
                translations=tuple(
                    Translation(
                        iso_3166_1=item["iso_3166_1"],
                        iso_639_1=item["iso_639_1"],
                        name=item["name"],
                        english_name=item["english_name"],
                        data=Data(**item["data"]),
                    )
                    for item in data["translations"]
                ),
                raw=data,
            )

    # TODO: Validate
    class TestUnknownEpisode:
        SERIES_ID = 999999999
        SEASON_NUMBER = 1
        EPISODE_NUMBER = 1

        # TODO: Validate
        def test_download(self, client: TMiniDB) -> None:
            # An episode that does not exist is refused rather than answered with
            # an empty list of translations, so there is no response to record.
            with pytest.raises(HTTPError) as error:
                client.tv_episodes.translations(
                    self.SERIES_ID,
                    self.SEASON_NUMBER,
                    self.EPISODE_NUMBER,
                )

            assert error.value.status_code == 404  # noqa: PLR2004
            assert error.value.response.json()["success"] is False
