# TODO: Validate
"""Contains the BaseSearch class."""

from __future__ import annotations

import json
from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any

from pydantic import BaseModel

from tminidb.base_api_endpoint import BaseEndpoint
from tminidb.exceptions import InvalidFileError

if TYPE_CHECKING:
    from collections.abc import Callable

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class BaseSearch[T: BaseModel](BaseEndpoint):
    """Base class for an endpoint that answers with a page of search results.

    Every search endpoint takes a query, a page and an adult flag, and differs
    in the path it is under, the filters it accepts and the model it is read
    with.

    Source: https://developer.themoviedb.org/reference/search-movie

    Example request:
        - GET /3/search/{type}?
            - query={query}&
            - include_adult=false&
            - language=en-US&
            - page=1
            - HTTP/2
        - Host: api.themoviedb.org
        - Accept: application/json
        - Authorization: Bearer __REDACTED__
    """

    MODEL: type[T]
    """The model this endpoint reads its responses with."""

    LOAD: Callable[[str | bytes | object, str], T]
    """The `model_validate_json` its model's module generates."""

    # TODO: Validate
    def _download(  # noqa: PLR0913 - Each parameter maps to an API parameter.
        self,
        endpoint: str,
        query: str,
        *,
        include_adult: bool,
        language: str | None,
        page: int,
        filters: dict[str, Any],
        log_id: str,
    ) -> str:
        response = self._client.download(
            endpoint,
            params={
                "query": query,
                "include_adult": include_adult,
                "language": language or self._client.language,
                "page": page,
                **filters,
            },
            log_id=log_id,
        )
        return self._validate_download(response, page)

    # TODO: Validate
    @staticmethod
    def _validate_download(response: str, page: int) -> str:
        # Nothing but the page number comes back from what was asked, so that and
        # the results are what say the file is the one that was asked for.
        parsed = json.loads(response)
        if parsed.get("page") != page or parsed.get("results") is None:
            raise InvalidFileError(
                field="search page",
                expected=page,
                response=response,
            )
        return response

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> T:
        """Read a downloaded search file into its model."""
        return type(self).LOAD(data, log_id or type(self).__name__)
