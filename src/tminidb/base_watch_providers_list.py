# TODO: Validate
"""Contains the BaseWatchProvidersList class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import TYPE_CHECKING

from pydantic import BaseModel

from tminidb.base_api_endpoint import BaseEndpoint

if TYPE_CHECKING:
    from collections.abc import Callable

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class BaseWatchProvidersList[T: BaseModel](BaseEndpoint):
    """Base class for an endpoint that answers with every streaming provider.

    Powered by TMDB's partnership with JustWatch. Using this data requires
    attributing JustWatch as its source.

    Source: https://developer.themoviedb.org/reference/watch-providers-movie-list
    """

    MODEL: type[T]
    """The model this endpoint reads its responses with."""

    LOAD: Callable[[str | bytes | object, str], T]
    """The `model_validate_json` its model's module generates."""

    # TODO: Validate
    def _download(
        self,
        endpoint: str,
        *,
        language: str | None,
        watch_region: str | None,
        log_id: str,
    ) -> str:
        return self._client.download(
            endpoint,
            params={
                "language": language or self._client.language,
                "watch_region": watch_region,
            },
            log_id=log_id,
        )

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> T:
        """Load a watch provider list file into its model."""
        return type(self).LOAD(data, log_id or self.default_log_id)
