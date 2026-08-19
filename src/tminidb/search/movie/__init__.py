# TODO: Validate
"""Search for movies by their original, translated and alternative titles.

[Official Documentation](https://developer.themoviedb.org/reference/search-movie)
"""

from __future__ import annotations

from logging import NullHandler, getLogger

from tminidb.base_endpoint import BaseEndpoint, records_call
from tminidb.exceptions import InvalidFileError
from tminidb.search.movie.models import MovieSearchResults

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class SearchMovie(BaseEndpoint):
    """Search for movies by their original, translated and alternative titles.

    [Official Documentation](https://developer.themoviedb.org/reference/search-movie)
    """

    # TODO: Validate
    @records_call
    def __call__(  # noqa: PLR0913 - Each parameter maps to an API parameter.
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
        """Downloads one page of movie search results and reads it.

        Raises:
            InvalidFileError: If the response is not the page that was asked
                for.
        """
        log_id = self.log_id()
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
