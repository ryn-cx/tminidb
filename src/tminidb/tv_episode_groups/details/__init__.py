# TODO: Validate
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
"""

from __future__ import annotations

from logging import NullHandler, getLogger

from tminidb.base_endpoint import BaseEndpoint, records_call
from tminidb.exceptions import InvalidFileError
from tminidb.tv_episode_groups.details.models import EpisodeGroup

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class TvEpisodeGroupDetails(BaseEndpoint):
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
    """

    # TODO: Validate
    @records_call
    def __call__(self, tv_episode_group_id: str) -> EpisodeGroup:
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
        log_id = self.log_id()
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
        return EpisodeGroup.from_response(data)
