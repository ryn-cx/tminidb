# TODO: Validate
"""Contains the TvSeriesEpisodeGroups class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any

from tminidb.base_api_endpoint import BaseEndpoint
from tminidb.exceptions import InvalidFileError
from tminidb.tv_series_episode_groups.models import TvSeriesEpisodeGroupsModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class TvSeriesEpisodeGroups(BaseEndpoint[TvSeriesEpisodeGroupsModel]):
    """Manage the TV series episode groups file.

    Wraps `GET /tv/{series_id}/episode_groups`:
    https://developer.themoviedb.org/reference/tv-series-episode-groups
    """

    _response_model = TvSeriesEpisodeGroupsModel

    def download(self, series_id: int) -> dict[str, Any]:
        """Downloads the TV series episode groups file."""
        log_id = self.get_log_id(self.download, locals())
        data = self._client.download(
            f"tv/{series_id}/episode_groups",
            {},
            log_id=log_id,
        )
        if data.get("id") != series_id:
            raise InvalidFileError(field="series id", expected=series_id, response=data)
        return data

    def download_and_parse(self, series_id: int) -> TvSeriesEpisodeGroupsModel:
        """Downloads and parses the TV series episode groups file."""
        return self.parse(self.download(series_id))
