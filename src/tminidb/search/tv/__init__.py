# TODO: Validate
"""Search for TV shows by their original, translated and also known as names.

Source: https://developer.themoviedb.org/reference/search-tv
"""

from __future__ import annotations

from logging import NullHandler, getLogger

from tminidb.base_search import BaseSearch
from tminidb.search.tv.models import SearchTvModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class SearchTv(BaseSearch[SearchTvModel]):
    """Search for TV shows by their original, translated and also known as names.

    Source: https://developer.themoviedb.org/reference/search-tv
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
        """Search for TV shows by their original, translated and also known as names.

        Source: https://developer.themoviedb.org/reference/search-tv
        """
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
