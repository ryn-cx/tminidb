# TODO: Validate
"""Contains the SearchMulti class."""

from __future__ import annotations

from logging import NullHandler, getLogger

from tminidb.base_search import BaseSearch
from tminidb.search.multi.models import SearchMultiModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class SearchMulti(BaseSearch[SearchMultiModel]):
    """Manage the multi search file.

    Searches movies, TV shows and people in a single request.

    Source: https://www.themoviedb.org/search?query={query}

    Example request:
        - GET /3/search/multi?
            - query={query}&
            - include_adult=false&
            - language=en-US&
            - page=1
            - HTTP/2
        - Host: api.themoviedb.org
        - Accept: application/json
        - Authorization: Bearer __REDACTED__
    """

    MODEL = SearchMultiModel
    LOAD = staticmethod(model_validate_json)

    # TODO: Validate
    def __call__(
        self,
        query: str,
        *,
        include_adult: bool = False,
        language: str | None = None,
        page: int = 1,
    ) -> SearchMultiModel:
        """Run the multi search and return the model it is read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(
                query,
                include_adult=include_adult,
                language=language,
                page=page,
            ),
            log_id,
        )

    # TODO: Validate
    def download(
        self,
        query: str,
        *,
        include_adult: bool = False,
        language: str | None = None,
        page: int = 1,
    ) -> str:
        """Download one page of multi search results."""
        log_id = self.get_log_id(self.download, locals())
        return self._download(
            "search/multi",
            query,
            include_adult=include_adult,
            language=language,
            page=page,
            filters={},
            log_id=log_id,
        )
