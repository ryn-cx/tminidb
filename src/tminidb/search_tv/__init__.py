# TODO: Validate
"""Contains the SearchTv class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any

from tminidb.base_api_endpoint import BaseEndpoint
from tminidb.search_tv.models import SearchTvModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class SearchTv(BaseEndpoint[SearchTvModel]):
    """Manage the search TV file.

    Wraps ``GET /search/tv``:
    https://developer.themoviedb.org/reference/search-tv
    """

    _response_model = SearchTvModel

    def get_log_id(  # noqa: PLR0913
        self,
        query: str,
        *,
        first_air_date_year: int | None = None,
        include_adult: bool = False,
        language: str | None = None,
        page: int = 1,
        year: int | None = None,
    ) -> str:
        """Build the log id for a download."""
        return self.append_non_default_args(
            f"{self.__class__.__name__} {query=}",
            first_air_date_year=(first_air_date_year, None),
            include_adult=(include_adult, False),
            language=(language, None),
            page=(page, 1),
            year=(year, None),
        )

    def download(  # noqa: PLR0913
        self,
        query: str,
        *,
        first_air_date_year: int | None = None,
        include_adult: bool = False,
        language: str | None = None,
        page: int = 1,
        year: int | None = None,
    ) -> dict[str, Any]:
        """Downloads the search TV file."""
        return self._client.download(
            "search/tv",
            {
                "query": query,
                "first_air_date_year": first_air_date_year,
                "include_adult": include_adult,
                "language": language or self._client.language,
                "page": page,
                "year": year,
            },
            log_id=self.get_log_id(
                query,
                first_air_date_year=first_air_date_year,
                include_adult=include_adult,
                language=language,
                page=page,
                year=year,
            ),
        )

    def download_and_parse(  # noqa: PLR0913
        self,
        query: str,
        *,
        first_air_date_year: int | None = None,
        include_adult: bool = False,
        language: str | None = None,
        page: int = 1,
        year: int | None = None,
    ) -> SearchTvModel:
        """Downloads and parses the search TV file."""
        return self.parse(
            self.download(
                query,
                first_air_date_year=first_air_date_year,
                include_adult=include_adult,
                language=language,
                page=page,
                year=year,
            ),
        )
