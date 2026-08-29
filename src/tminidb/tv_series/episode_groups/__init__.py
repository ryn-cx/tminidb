# TODO: Validate
"""Get the episode groups that have been added to a TV show.

Source: https://developer.themoviedb.org/reference/tv-series-episode-groups
"""

from __future__ import annotations

import json
from logging import NullHandler, getLogger

from tminidb.base_api_endpoint import BaseEndpoint
from tminidb.exceptions import (
    InvalidFileError,
    ResourceNotFoundError,
    SeriesNotFoundError,
)
from tminidb.tv_series.episode_groups.models import (
    TvSeriesEpisodeGroupsModel,
    model_validate_json,
)

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class TvSeriesEpisodeGroups(BaseEndpoint):
    """Get the episode groups that have been added to a TV show.

    With a group ID you can call the get TV episode group details method.

    Source: https://developer.themoviedb.org/reference/tv-series-episode-groups
    """

    # TODO: Validate
    def __call__(self, series_id: int) -> TvSeriesEpisodeGroupsModel:
        """Get the episode groups that have been added to a TV show.

        Source: https://developer.themoviedb.org/reference/tv-series-episode-groups
        """
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(series_id), log_id)

    # TODO: Validate
    def download(self, series_id: int) -> str:
        """Download the TV series episode groups file.

        Raises:
            SeriesNotFoundError: If no series is under that id.
        """
        log_id = self.get_log_id(self.download, locals())
        try:
            response = self._client.download(
                f"tv/{series_id}/episode_groups",
                params={},
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise SeriesNotFoundError(series_id, err.status_code, err.response) from err
        return self._validate_download(response, series_id)

    # TODO: Validate
    @staticmethod
    def _validate_download(response: str, series_id: int) -> str:
        if json.loads(response).get("id") != series_id:
            raise InvalidFileError(
                field="series id",
                expected=series_id,
                response=response,
            )
        return response

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> TvSeriesEpisodeGroupsModel:
        """Read a downloaded TV series episode groups file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)
