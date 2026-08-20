# TODO: Validate
"""Contains the SearchEndpoints class.

Every endpoint the API's docs file under Search is a method here, reached the
way the API reaches it: `client.search.movie("Fight Club")` is `search/movie`
and is the whole of it, because the method both downloads and reads.

[Official Documentation](https://developer.themoviedb.org/reference/search-movie)
"""

from __future__ import annotations

from logging import NullHandler, getLogger

from tminidb.base_endpoint import BaseEndpoint
from tminidb.exceptions import InvalidFileError
from tminidb.search.models.movie import MovieSearchResults
from tminidb.search.models.multi import MultiSearchResults
from tminidb.search.models.tv import TvSearchResults

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class SearchEndpoints(BaseEndpoint):
    """The endpoints the API's docs file under Search.

    [Official Documentation](https://developer.themoviedb.org/reference/search-movie)
    """

    # TODO: Validate
    def movie(  # noqa: PLR0913 - Each parameter maps to an API parameter.
        self,
        query: str,
        *,
        include_adult: bool = False,
        language: str | None = None,
        primary_release_year: str | None = None,
        region: str | None = None,
        year: str | None = None,
        page: int = 1,
    ) -> MovieSearchResults:
        """Download one page of movie search results and read it.

        Search for movies by their original, translated and alternative titles.

        [Official Documentation](https://developer.themoviedb.org/reference/search-movie)

        Raises:
            InvalidFileError: If the response is not the page that was asked
                for.
        """
        log_id = self.get_log_id(self.movie, locals())
        data = self._client.download(
            "search/movie",
            {
                "query": query,
                "include_adult": include_adult,
                "language": language or self._client.language,
                "primary_release_year": primary_release_year,
                "region": region,
                "year": year,
                "page": page,
            },
            log_id=log_id,
        )
        # Nothing but the page echoes the query, so that and the results are
        # what get checked.
        if data.get("page") != page or data.get("results") is None:
            raise InvalidFileError(field="search page", expected=page, response=data)
        return MovieSearchResults.from_response(data)

    # TODO: Validate
    def multi(
        self,
        query: str,
        *,
        include_adult: bool = False,
        language: str | None = None,
        page: int = 1,
    ) -> MultiSearchResults:
        """Download one page of mixed search results and read it.

        Use multi search when you want to search for movies, TV shows and people
        in a single request.

        [Official Documentation](https://developer.themoviedb.org/reference/search-multi)

        Raises:
            InvalidFileError: If the response is not the page that was asked
                for.
        """
        log_id = self.get_log_id(self.multi, locals())
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
        # Nothing but the page echoes the query, so that and the results are
        # what get checked.
        if data.get("page") != page or data.get("results") is None:
            raise InvalidFileError(field="search page", expected=page, response=data)
        return MultiSearchResults.from_response(data)

    # TODO: Validate
    def tv(  # noqa: PLR0913 - Each parameter maps to an API parameter.
        self,
        query: str,
        *,
        first_air_date_year: int | None = None,
        include_adult: bool = False,
        language: str | None = None,
        year: int | None = None,
        page: int = 1,
    ) -> TvSearchResults:
        """Download one page of TV search results and read it.

        Search for TV shows by their original, translated and also known as names.

        [Official Documentation](https://developer.themoviedb.org/reference/search-tv)

        Raises:
            InvalidFileError: If the response is not the page that was asked
                for.
        """
        log_id = self.get_log_id(self.tv, locals())
        data = self._client.download(
            "search/tv",
            {
                "query": query,
                "first_air_date_year": first_air_date_year,
                "include_adult": include_adult,
                "language": language or self._client.language,
                "year": year,
                "page": page,
            },
            log_id=log_id,
        )
        # Nothing but the page echoes the query, so that and the results are
        # what get checked.
        if data.get("page") != page or data.get("results") is None:
            raise InvalidFileError(field="search page", expected=page, response=data)
        return TvSearchResults.from_response(data)
