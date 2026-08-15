# TODO: Validate
"""Contains the SearchMovie class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any

from tminidb.base_api_endpoint import BaseEndpoint
from tminidb.exceptions import InvalidFileError
from tminidb.search_movie.models import SearchMovieModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class SearchMovie(BaseEndpoint[SearchMovieModel]):
    """Manage the search movie file.

    Wraps `GET /search/movie`:
    https://developer.themoviedb.org/reference/search-movie
    """

    _response_model = SearchMovieModel

    def download(  # noqa: PLR0913
        self,
        query: str,
        *,
        include_adult: bool = False,
        language: str | None = None,
        primary_release_year: str | None = None,
        page: int = 1,
        region: str | None = None,
        year: str | None = None,
    ) -> dict[str, Any]:
        """Downloads the search movie file."""
        log_id = self.get_log_id(self.download, locals())
        data = self._client.download(
            "search/movie",
            {
                "query": query,
                "include_adult": include_adult,
                "language": language or self._client.language,
                "primary_release_year": primary_release_year,
                "page": page,
                "region": region,
                "year": year,
            },
            log_id=log_id,
        )
        # Nothing but the page echoes the query, so that and the results
        # are what get checked.
        if data.get("page") != page or data.get("results") is None:
            raise InvalidFileError(field="search page", expected=page, response=data)
        return data

    def download_and_parse(  # noqa: PLR0913
        self,
        query: str,
        *,
        include_adult: bool = False,
        language: str | None = None,
        primary_release_year: str | None = None,
        page: int = 1,
        region: str | None = None,
        year: str | None = None,
    ) -> SearchMovieModel:
        """Downloads and parses the search movie file."""
        return self.parse(
            self.download(
                query,
                include_adult=include_adult,
                language=language,
                primary_release_year=primary_release_year,
                page=page,
                region=region,
                year=year,
            ),
        )
