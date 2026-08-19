# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import record_test, recorded_content
from tminidb.exceptions import HTTPError
from tminidb.tv_episodes.translations import TvEpisodeTranslations
from tminidb.tv_episodes.translations.models import (
    Translations,
    Translation,
    Data,
)

if TYPE_CHECKING:
    from tminidb import TMiniDB


# TODO: Validate
class TestEpisode:
    SERIES_ID = 1396
    SEASON_NUMBER = 1
    EPISODE_NUMBER = 1
    NAME = "1396_1_1"
    EPISODE_ID = 62085

    # TODO: Validate
    def test_download(self, client: TMiniDB) -> None:
        record_test(
            TvEpisodeTranslations,
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
    def test_parse(self) -> None:
        # The whole of what the response is read into, in one comparison. Which
        # languages an episode has been written in grows as people add them, so
        # the rows are read back from the response: what is checked is that
        # each one keeps the language and country it is filed under and the
        # title and summary in the nested `data` object.
        data = recorded_content(TvEpisodeTranslations, self.NAME)

        assert Translations.from_response(data) == Translations(
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
        assert error.value.response["success"] is False
