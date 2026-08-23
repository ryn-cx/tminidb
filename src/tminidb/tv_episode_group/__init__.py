# TODO: Validate
"""Contains the TvEpisodeGroup class."""

from __future__ import annotations

import json
from logging import NullHandler, getLogger

from tminidb.base_api_endpoint import BaseEndpoint
from tminidb.exceptions import (
    EpisodeGroupNotFoundError,
    InvalidFileError,
    ResourceNotFoundError,
)
from tminidb.tv_episode_group.models import TvEpisodeGroupModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class TvEpisodeGroup(BaseEndpoint):
    """Manage the TV episode group file.

    A group is one of seven types: original air date, absolute, DVD, digital,
    story arc, production or TV.

    Source: https://www.themoviedb.org/tv/episode_group/{episode_group_id}

    Example request:
        - GET /3/tv/episode_group/{episode_group_id} HTTP/2
        - Host: api.themoviedb.org
        - Accept: application/json
        - Authorization: Bearer __REDACTED__
    """

    # TODO: Validate
    def __call__(self, episode_group_id: str) -> TvEpisodeGroupModel:
        """Look the episode group up and return the model it is read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(episode_group_id), log_id)

    # TODO: Validate
    def download(self, episode_group_id: str) -> str:
        """Download the TV episode group file.

        Raises:
            EpisodeGroupNotFoundError: If no episode group is under that id.
        """
        log_id = self.get_log_id(self.download, locals())
        try:
            response = self._client.download(
                f"tv/episode_group/{episode_group_id}",
                params={},
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise EpisodeGroupNotFoundError(
                episode_group_id,
                err.status_code,
                err.response,
            ) from err
        return self._validate_download(response, episode_group_id)

    # TODO: Validate
    @staticmethod
    def _validate_download(response: str, episode_group_id: str) -> str:
        if json.loads(response).get("id") != episode_group_id:
            raise InvalidFileError(
                field="episode group id",
                expected=episode_group_id,
                response=response,
            )
        return response

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> TvEpisodeGroupModel:
        """Read a downloaded TV episode group file into its model."""
        return model_validate_json(data, log_id or type(self).__name__)
