# TODO: Validate
"""Contains the SearchTv class."""

from __future__ import annotations

from logging import NullHandler, getLogger

from tminidb.base_search import BaseSearch
from tminidb.search.tv.models import SearchTvModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class SearchTv(BaseSearch[SearchTvModel]):
    """Manage the TV search file.

    Searches TV shows by their original, translated and also known as names.

    Source: https://www.themoviedb.org/search/tv?query={query}

    Example request:
        - GET /3/search/tv?
            - query={query}&
            - include_adult=false&
            - language=en-US&
            - page=1
            - HTTP/2
        - Host: api.themoviedb.org
        - Accept: application/json
        - Authorization: Bearer __REDACTED__
    """

    MODEL = SearchTvModel
    LOAD = staticmethod(model_validate_json)

    # TODO: Validate
    def __call__(  # noqa: PLR0913 - Each parameter maps to an API parameter.
        self,
        query: str,
        *,
        first_air_date_year: int | None = None,
        include_adult: bool = False,
        language: str | None = None,
        year: int | None = None,
        page: int = 1,
    ) -> SearchTvModel:
        """Run the TV search and return the model it is read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(
                query,
                first_air_date_year=first_air_date_year,
                include_adult=include_adult,
                language=language,
                year=year,
                page=page,
            ),
            log_id,
        )

    # TODO: Validate
    def download(  # noqa: PLR0913 - Each parameter maps to an API parameter.
        self,
        query: str,
        *,
        first_air_date_year: int | None = None,
        include_adult: bool = False,
        language: str | None = None,
        year: int | None = None,
        page: int = 1,
    ) -> str:
        """Download one page of TV search results."""
        log_id = self.get_log_id(self.download, locals())
        return self._download(
            "search/tv",
            query,
            include_adult=include_adult,
            language=language,
            page=page,
            filters={"first_air_date_year": first_air_date_year, "year": year},
            log_id=log_id,
        )
