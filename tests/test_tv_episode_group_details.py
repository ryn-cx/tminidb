# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING, Any

import pytest

from tests.utils import record_test, recorded_content
from tminidb.exceptions import HTTPError
from tminidb.tv_episode_groups.details import TvEpisodeGroupDetails
from tminidb.tv_episode_groups.details.models import (
    EpisodeGroup,
    Group,
    GroupEpisode,
    Network,
)

if TYPE_CHECKING:
    from tminidb import TMiniDB


# TODO: Validate
def _expected(data: dict[str, Any]) -> EpisodeGroup:
    """The whole model, read back out of the response it came from.

    A grouping is a nested thing: seasons holding episodes holding an order of
    their own. Writing a hundred rows out by hand would be unreadable and would
    go stale the first time somebody edits the grouping, so the rows are read
    back and what the comparison checks is that every group and every episode
    inside it is carried over, in order, with the fields that place it.
    """
    return EpisodeGroup(
        description=data["description"],
        episode_count=data["episode_count"],
        group_count=data["group_count"],
        groups=tuple(
            Group(
                id=group["id"],
                name=group["name"],
                order=group["order"],
                episodes=tuple(
                    GroupEpisode(**episode) for episode in group["episodes"]
                ),
                locked=group["locked"],
            )
            for group in data["groups"]
        ),
        id=data["id"],
        name=data["name"],
        network=None if data["network"] is None else Network(**data["network"]),
        type=data["type"],
        raw=data,
    )


# TODO: Validate
class TestGroupWithoutNetwork:
    # `DVD / PVOD` for Breaking Bad, which has no network.
    GROUP_ID = "69f50757054263b7bc87e32a"

    # TODO: Validate
    def test_download(self, client: TMiniDB) -> None:
        record_test(
            TvEpisodeGroupDetails,
            self.GROUP_ID,
            lambda: client.tv_episode_groups.details(self.GROUP_ID).raw,
        )

    # TODO: Validate
    def test_parse(self) -> None:
        data = recorded_content(TvEpisodeGroupDetails, self.GROUP_ID)

        assert EpisodeGroup.from_response(data) == _expected(data)


# TODO: Validate
class TestGroupWithNetwork:
    # `Aired Order` for Game of Thrones, which does have a network, so the two
    # together cover both shapes the field takes.
    GROUP_ID = "5e9077d2e640d600151f32bd"

    # TODO: Validate
    def test_download(self, client: TMiniDB) -> None:
        record_test(
            TvEpisodeGroupDetails,
            self.GROUP_ID,
            lambda: client.tv_episode_groups.details(self.GROUP_ID).raw,
        )

    # TODO: Validate
    def test_parse(self) -> None:
        data = recorded_content(TvEpisodeGroupDetails, self.GROUP_ID)

        assert EpisodeGroup.from_response(data) == _expected(data)


# TODO: Validate
class TestUnknownGroup:
    # Well formed for a group id, which is a hex string rather than a number,
    # but belonging to nothing.
    GROUP_ID = "000000000000000000000000"

    # TODO: Validate
    def test_download(self, client: TMiniDB) -> None:
        with pytest.raises(HTTPError) as error:
            client.tv_episode_groups.details(self.GROUP_ID)

        assert error.value.status_code == 404  # noqa: PLR2004
        assert error.value.response["success"] is False


# TODO: Validate
class TestMalformedGroup:
    # Not shaped like a group id at all.
    GROUP_ID = "not-a-group-id"

    # TODO: Validate
    def test_download(self, client: TMiniDB) -> None:
        # An id that is not shaped like one is refused the same way an unknown
        # one is, so a typo cannot be told from a deleted grouping.
        with pytest.raises(HTTPError) as error:
            client.tv_episode_groups.details(self.GROUP_ID)

        assert error.value.status_code == 404  # noqa: PLR2004
