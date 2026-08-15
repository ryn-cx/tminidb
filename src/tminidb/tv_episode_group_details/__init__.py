# TODO: Validate
"""Contains the TvEpisodeGroupDetails class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any

from tminidb.base_api_endpoint import BaseEndpoint
from tminidb.exceptions import InvalidFileError
from tminidb.tv_episode_group_details.models import TvEpisodeGroupDetailsModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class TvEpisodeGroupDetails(BaseEndpoint[TvEpisodeGroupDetailsModel]):
    """Manage the TV episode group details file.

    Wraps `GET /tv/episode_group/{tv_episode_group_id}`:
    https://developer.themoviedb.org/reference/tv-episode-group-details
    """

    _response_model = TvEpisodeGroupDetailsModel

    def download(self, tv_episode_group_id: str) -> dict[str, Any]:
        """Downloads the TV episode group details file."""
        log_id = self.get_log_id(self.download, locals())
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
        return data

    def download_and_parse(
        self,
        tv_episode_group_id: str,
    ) -> TvEpisodeGroupDetailsModel:
        """Downloads and parses the TV episode group details file."""
        return self.parse(self.download(tv_episode_group_id))
