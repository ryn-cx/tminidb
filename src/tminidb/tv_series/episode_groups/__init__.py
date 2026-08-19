# TODO: Validate
"""Get the episode groups that have been added to a TV show.

With a group ID you can call the get TV episode group details method.

[Official Documentation](https://developer.themoviedb.org/reference/tv-series-episode-groups)
"""

from __future__ import annotations

from logging import NullHandler, getLogger

from tminidb.base_endpoint import BaseEndpoint, records_call
from tminidb.exceptions import InvalidFileError
from tminidb.tv_series.episode_groups.models import EpisodeGroups

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class TvSeriesEpisodeGroups(BaseEndpoint):
    """Get the episode groups that have been added to a TV show.

    With a group ID you can call the get TV episode group details method.

    [Official Documentation](https://developer.themoviedb.org/reference/tv-series-episode-groups)
    """

    # TODO: Validate
    @records_call
    def __call__(self, series_id: int) -> EpisodeGroups:
        """Get the episode groups that have been added to a TV show.

        With a group ID you can call the get TV episode group details method.

        [Official Documentation](https://developer.themoviedb.org/reference/tv-series-episode-groups)

        Raises:
            InvalidFileError: If the response is for a different series.
        """
        log_id = self.log_id()
        data = self._client.download(
            f"tv/{series_id}/episode_groups",
            {},
            log_id=log_id,
        )
        if data.get("id") != series_id:
            raise InvalidFileError(field="series id", expected=series_id, response=data)
        return EpisodeGroups.from_response(data)
