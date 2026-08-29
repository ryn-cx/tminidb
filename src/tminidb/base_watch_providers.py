# TODO: Validate
"""Contains the BaseWatchProviders class."""

from __future__ import annotations

import json
from logging import NullHandler, getLogger
from typing import TYPE_CHECKING

from pydantic import BaseModel

from tminidb.base_api_endpoint import BaseEndpoint
from tminidb.exceptions import InvalidFileError

if TYPE_CHECKING:
    from collections.abc import Callable

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class BaseWatchProviders[T: BaseModel](BaseEndpoint):
    """Base class for an endpoint that answers with streaming providers.

    Powered by TMDB's partnership with JustWatch. Using this data requires
    attributing JustWatch as its source.

    Source: https://developer.themoviedb.org/reference/movie-watch-providers
    """

    MODEL: type[T]
    """The model this endpoint reads its responses with."""

    LOAD: Callable[[str | bytes | object, str], T]
    """The `model_validate_json` its model's module generates."""

    # TODO: Validate
    def _download(self, endpoint: str, *, log_id: str) -> str:
        return self._client.download(endpoint, params={}, log_id=log_id)

    # TODO: Validate
    @staticmethod
    def _validate_download(response: str, field: str, expected: int) -> str:
        if json.loads(response).get("id") != expected:
            raise InvalidFileError(field=field, expected=expected, response=response)
        return response

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> T:
        """Read a downloaded watch providers file into its model."""
        return type(self).LOAD(data, log_id or self.default_log_id)
