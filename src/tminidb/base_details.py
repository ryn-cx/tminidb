# TODO: Validate
"""Contains the BaseDetails class."""

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
class BaseDetails[T: BaseModel](BaseEndpoint):
    """Base class for an endpoint that answers with the details of one thing.

    Every detail endpoint takes the same two parameters and differs only in the
    path it is under and the model it is read with.

    Source: https://developer.themoviedb.org/reference/movie-details
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
        append_to_response: str | None,
        language: str | None,
        log_id: str,
    ) -> str:
        return self._client.download(
            endpoint,
            params={
                "append_to_response": append_to_response,
                "language": language or self._client.language,
            },
            log_id=log_id,
        )

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> T:
        """Read a downloaded details file into its model."""
        return type(self).LOAD(data, log_id or self.default_log_id)
