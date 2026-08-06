# TODO: Validate
"""Contains the TvWatchProviders class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any

from tminidb.base_api_endpoint import BaseEndpoint
from tminidb.exceptions import InvalidFileError
from tminidb.tv_watch_providers.models import TvWatchProvidersModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class TvWatchProviders(BaseEndpoint[TvWatchProvidersModel]):
    """Manage the TV watch providers file.

    Wraps `GET /tv/{series_id}/watch/providers`:
    https://developer.themoviedb.org/reference/tv-series-watch-providers
    """

    _response_model = TvWatchProvidersModel

    def download(self, series_id: int) -> dict[str, Any]:
        """Downloads the TV watch providers file."""
        log_id = self.get_log_id(self.download, locals())
        data = self._client.download(
            f"tv/{series_id}/watch/providers",
            {},
            log_id=log_id,
        )
        if data.get("id") != series_id:
            raise InvalidFileError(field="series id", expected=series_id)
        return data

    def download_and_parse(self, series_id: int) -> TvWatchProvidersModel:
        """Downloads and parses the TV watch providers file."""
        return self.parse(self.download(series_id))
