"""Contains the BaseSearchMulti and SearchMulti classes."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any

from good_ass_pydantic_integrator import GAPIBaseModel

from tminidb.base_api_endpoint import BaseEndpoint
from tminidb.constants import DEFAULT_LANGUAGE
from tminidb.search_multi.models import SearchMultiModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class BaseSearchMulti[T: GAPIBaseModel](BaseEndpoint[T]):
    """Shared logic for the SearchMulti endpoint.

    Wraps `GET /search/multi`:
    https://developer.themoviedb.org/reference/search-multi
    """

    def get_log_id(
        self,
        query: str,
        *,
        include_adult: bool = False,
        language: str,
        page: int = 1,
    ) -> str:
        """Returns a log id for a SearchMulti download.

        Args:
            query: Text to search for.
            include_adult: Whether to include adult content. Defaults to `False`.
            language: `ISO 639-1`-`ISO 3166-1` language for the results. Defaults to
                `en-US`.
            page: Which page of results to fetch. Defaults to `1`.
        """
        return self.append_non_default_args(
            f"{self.__class__.__name__} {query=}",
            include_adult=(include_adult, False),
            language=(language, DEFAULT_LANGUAGE),
            page=(page, 1),
        )

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
        language = language or self._client.language
        return self._client.download(
            "search/multi",
            {
                "query": query,
                "include_adult": include_adult,
                "language": language,
                "page": page,
            },
            log_id=self.get_log_id(
                query,
                include_adult=include_adult,
                language=language,
                page=page,
            ),
        )

    def download_and_parse(
        self,
        query: str,
        *,
        include_adult: bool = False,
        language: str | None = None,
        page: int = 1,
    ) -> T:
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


class SearchMulti(BaseSearchMulti[SearchMultiModel]):
    """SearchMulti endpoint.

    Wraps `GET /search/multi`:
    https://developer.themoviedb.org/reference/search-multi
    """

    _response_model = SearchMultiModel
