# TODO: Validate
"""Use multi search when you want to search for movies, TV shows and people in a single request.

[Official Documentation](https://developer.themoviedb.org/reference/search-multi)
"""  # noqa: E501

from __future__ import annotations

from logging import NullHandler, getLogger

from tminidb.base_endpoint import BaseEndpoint, records_call
from tminidb.exceptions import InvalidFileError
from tminidb.search.multi.models import MultiSearchResults

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class SearchMulti(BaseEndpoint):
    """Use multi search when you want to search for movies, TV shows and people in a single request.

    [Official Documentation](https://developer.themoviedb.org/reference/search-multi)
    """  # noqa: E501

    # TODO: Validate
    @records_call
    def __call__(
        self,
        query: str,
        *,
        include_adult: bool = False,
        language: str | None = None,
        page: int = 1,
    ) -> MultiSearchResults:
        """Downloads one page of mixed search results and reads it.

        Raises:
            InvalidFileError: If the response is not the page that was asked
                for.
        """
        log_id = self.log_id()
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
