# TODO: Validate
"""Contains the SearchMulti class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any

from tminidb.base_api_endpoint import BaseEndpoint
from tminidb.exceptions import InvalidFileError
from tminidb.search_multi.models import SearchMultiModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class SearchMulti(BaseEndpoint[SearchMultiModel]):
    """SearchMulti endpoint.

    Wraps `GET /search/multi`:
    https://developer.themoviedb.org/reference/search-multi
    """

    _response_model = SearchMultiModel

    def download(
        self,
        query: str,
        *,
        include_adult: bool = False,
        language: str | None = None,
        page: int = 1,
    ) -> dict[str, Any]:
        """Downloads a SearchMulti file.

        Args:
            query: Text to search for.
            include_adult: Whether to include adult content. Defaults to `False`.
            language: `ISO 639-1`-`ISO 3166-1` language for the results. Defaults to
                `en-US`.
            page: Which page of results to fetch. Defaults to `1`.
        """
        log_id = self.get_log_id(self.download, locals())
        language = language or self._client.language
        data = self._client.download(
            "search/multi",
            {
                "query": query,
                "include_adult": include_adult,
                "language": language,
                "page": page,
            },
            log_id=log_id,
        )
        # Nothing but the page echoes the query, so that and the results
        # are what get checked.
        if data.get("page") != page or data.get("results") is None:
            raise InvalidFileError(field="search page", expected=page)
        return data

    def download_and_parse(
        self,
        query: str,
        *,
        include_adult: bool = False,
        language: str | None = None,
        page: int = 1,
    ) -> SearchMultiModel:
        """Downloads and parses a SearchMulti file.

        Args:
            query: Text to search for.
            include_adult: Whether to include adult content. Defaults to `False`.
            language: `ISO 639-1`-`ISO 3166-1` language for the results. Defaults to
                `en-US`.
            page: Which page of results to fetch. Defaults to `1`.
        """
        return self.parse(
            self.download(
                query,
                include_adult=include_adult,
                language=language,
                page=page,
            ),
        )
