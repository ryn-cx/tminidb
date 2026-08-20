# TODO: Validate
"""Contains the TvEpisodeGroupEndpoints class.

Every endpoint the API's docs file under TV Episode Groups is a method here,
reached the way the API reaches it:
`client.tv_episode_groups.details("5acf93e60e0a26346d0000ce")` is
`tv/episode_group/5acf93e60e0a26346d0000ce` and is the whole of it, because the
method both downloads and reads.

[Official Documentation](https://developer.themoviedb.org/reference/tv-episode-group-details)
"""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any

from tminidb.base_endpoint import BaseEndpoint
from tminidb.exceptions import InvalidFileError
from tminidb.tv_episode_groups.models.details import EpisodeGroup

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class TvEpisodeGroupEndpoints(BaseEndpoint):
    """The endpoints the API's docs file under TV Episode Groups.

    [Official Documentation](https://developer.themoviedb.org/reference/tv-episode-group-details)
    """

    # TODO: Validate
    def details(self, tv_episode_group_id: str) -> EpisodeGroup:
        """Get the details of a TV episode group.

        Groups support 7 different types which are enumerated as the following:

        | Type | Name              |
        | :--- | :---------------- |
        | 1    | Original air date |
        | 2    | Absolute          |
        | 3    | DVD               |
        | 4    | Digital           |
        | 5    | Story arc         |
        | 6    | Production        |
        | 7    | TV                |

        [Official Documentation](https://developer.themoviedb.org/reference/tv-episode-group-details)

        Raises:
            InvalidFileError: If the response is for a different group.
        """
        log_id = self.get_log_id(self.details, locals())
        data = self._client.download(
            f"tv/episode_group/{tv_episode_group_id}",
            {},
            log_id=log_id,
        )
        if data.get("id") != tv_episode_group_id:
            raise InvalidFileError(
                field="episode group id",
                expected=tv_episode_group_id,
                response=data,
            )
        return self.load_details(data)

    # TODO: Validate
    def load_details(self, data: dict[str, Any]) -> EpisodeGroup:
        """Read a response the details endpoint answered with."""
        return EpisodeGroup.from_response(data)
