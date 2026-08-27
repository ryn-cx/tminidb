# TODO: Validate
"""Contains the SearchMovie class."""

from __future__ import annotations

from logging import NullHandler, getLogger

from tminidb.base_search import BaseSearch
from tminidb.search.movie.models import SearchMovieModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class SearchMovie(BaseSearch[SearchMovieModel]):
    """Manage the movie search file.

    Searches movies by their original, translated and alternative titles.

    Source: https://www.themoviedb.org/search/movie?query={query}

    Example request:
        - GET /3/search/movie?
            - query={query}&
            - include_adult=false&
            - language=en-US&
            - page=1
            - HTTP/2
        - Host: api.themoviedb.org
        - Accept: application/json
        - Authorization: Bearer __REDACTED__
    """

    MODEL = SearchMovieModel
    LOAD = staticmethod(model_validate_json)

    # TODO: Validate
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
    ) -> SearchMovieModel:
        """Run the movie search and return the model it is read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(
                query,
                include_adult=include_adult,
                language=language,
                primary_release_year=primary_release_year,
                region=region,
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
        include_adult: bool = False,
        language: str | None = None,
        primary_release_year: str | None = None,
        region: str | None = None,
        year: str | None = None,
        page: int = 1,
    ) -> str:
        """Download one page of movie search results."""
        log_id = self.get_log_id(self.download, locals())
        return self._download(
            "search/movie",
            query,
            include_adult=include_adult,
            language=language,
            page=page,
            filters={
                "primary_release_year": primary_release_year,
                "region": region,
                "year": year,
            },
            log_id=log_id,
        )
