# TODO: Validate
"""Contains the BaseSimilar class."""

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
class BaseSimilar[T: BaseModel](BaseEndpoint):
    """Base class for an endpoint that answers with a page of similar items.

    Every similar endpoint takes a language and a page, and differs in the path
    it is under and the model it is read with.

    Source: https://developer.themoviedb.org/reference/movie-similar
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
        page: int,
        log_id: str,
    ) -> str:
        response = self._client.download(
            endpoint,
            params={
                "language": language or self._client.language,
                "page": page,
            },
            log_id=log_id,
        )
        return self._validate_download(response, page)

    # TODO: Validate
    @staticmethod
    def _validate_download(response: str, page: int) -> str:
        # The page number is the only part of the request the response repeats.
        parsed = json.loads(response)
        if parsed.get("page") != page or parsed.get("results") is None:
            raise InvalidFileError(
                field="similar page",
                expected=page,
                response=response,
            )
        return response

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> T:
        """Load a similar file into its model."""
        return type(self).LOAD(data, log_id or self.default_log_id)
