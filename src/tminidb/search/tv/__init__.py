# TODO: Validate
"""Search for TV shows by their original, translated and also known as names.

[Official Documentation](https://developer.themoviedb.org/reference/search-tv)
"""

from __future__ import annotations

from logging import NullHandler, getLogger

from tminidb.base_endpoint import BaseEndpoint, records_call
from tminidb.exceptions import InvalidFileError
from tminidb.search.tv.models import TvSearchResults

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class SearchTv(BaseEndpoint):
    """Search for TV shows by their original, translated and also known as names.

    [Official Documentation](https://developer.themoviedb.org/reference/search-tv)
    """

    # TODO: Validate
    @records_call
    def __call__(  # noqa: PLR0913 - Each parameter maps to an API parameter.
        self,
        query: str,
        *,
        first_air_date_year: int | None = None,
        include_adult: bool = False,
        language: str | None = None,
        year: int | None = None,
        page: int = 1,
    ) -> TvSearchResults:
        """Downloads one page of TV search results and reads it.

        Raises:
            InvalidFileError: If the response is not the page that was asked
                for.
        """
        log_id = self.log_id()
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
