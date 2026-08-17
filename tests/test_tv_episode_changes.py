# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import download_and_save, parse_json_to_dict, parse_json_to_model

if TYPE_CHECKING:
    from tminidb import TMiniDB
    from tminidb.tv_episode_changes import TvEpisodeChanges

# A TV episode that had been edited when the file was recorded. The window is the
# last 24 hours, so a TV episode that is quiet answers with nothing and would
# record a file with no changes in it to build a model from.
EPISODE_ID = 7434652
NAME = str(EPISODE_ID)
# An id that belongs to no TV episode. It is answered with an empty list rather
# than with an error, which is why there is no recorded error file here.
UNKNOWN_EPISODE_ID = 999999999
UNKNOWN_NAME = f"unknown_{UNKNOWN_EPISODE_ID}"


# TODO: Validate
@pytest.fixture(scope="session")
def endpoint(client: TMiniDB) -> TvEpisodeChanges:
    return client.tv_episode_changes


# TODO: Validate
class TestTvEpisodeChanges:
    # TODO: Validate
    def test_download(self, endpoint: TvEpisodeChanges) -> None:
        download_and_save(endpoint, NAME, lambda: endpoint.download(EPISODE_ID))

    # TODO: Validate
    def test_download_unknown(self, endpoint: TvEpisodeChanges) -> None:
        download_and_save(
            endpoint,
            UNKNOWN_NAME,
            lambda: endpoint.download(UNKNOWN_EPISODE_ID),
        )

    # TODO: Validate
    def test_parse(self, endpoint: TvEpisodeChanges) -> None:
        data = parse_json_to_model(endpoint, NAME)
        assert data.changes

    # TODO: Validate
    def test_parse_groups_are_keyed_and_hold_items(
        self,
        endpoint: TvEpisodeChanges,
    ) -> None:
        data = parse_json_to_model(endpoint, NAME)
        # A change only means anything alongside the field it happened to, so a
        # group without a key would leave its items unreadable.
        assert all(group.key for group in data.changes)
        assert all(group.items for group in data.changes)

    # TODO: Validate
    def test_parse_items_are_dated_edits(self, endpoint: TvEpisodeChanges) -> None:
        items = [
            item
            for group in parse_json_to_model(endpoint, NAME).changes
            for item in group.items
        ]
        assert items
        # Every edit says what it did and when, which is what makes the changes
        # usable as a feed rather than as a snapshot.
        assert all(item.action for item in items)
        assert all(item.time for item in items)

    # TODO: Validate
    def test_parse_unknown_is_empty_rather_than_an_error(
        self,
        endpoint: TvEpisodeChanges,
    ) -> None:
        # An id that names nothing is not rejected, so an empty result says
        # nothing about whether the id was good.
        assert parse_json_to_dict(endpoint, UNKNOWN_NAME) == {"changes": []}
