# TODO: Validate
"""Contains the MovieEndpoints class.

Every endpoint the API's docs file under Movies is a method here, reached the
way the API reaches it: `client.movies.details(278)` is `movie/278` and is the
whole of it, because the method both downloads and reads.

[Official Documentation](https://developer.themoviedb.org/reference/movie-details)
"""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any

from tminidb._changes import download_changes
from tminidb.base_endpoint import BaseEndpoint
from tminidb.exceptions import InvalidFileError
from tminidb.movies.models.changes import MovieChangeLog
from tminidb.movies.models.details import Movie
from tminidb.movies.models.watch_providers import MovieProviders

if TYPE_CHECKING:
    from datetime import date

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class MovieEndpoints(BaseEndpoint):
    """The endpoints the API's docs file under Movies.

    [Official Documentation](https://developer.themoviedb.org/reference/movie-details)
    """

    # TODO: Validate
    def changes(
        self,
        movie_id: int,
        *,
        start_date: date | None = None,
        end_date: date | None = None,
        page: int = 1,
    ) -> MovieChangeLog:
        """Get the recent changes for a movie.

        Get the changes for a movie. By default only the last 24 hours are returned.

        You can query up to 14 days in a single query by using the `start_date` and
        `end_date` query parameters.

        [Official
        Documentation](https://developer.themoviedb.org/reference/movie-changes)

        If the query is more than 14 days multiple queries will be made and the results
        will be merged together.
        """
        log_id = self.get_log_id(self.changes, locals())

        # TODO: Validate
        def _download(start: str | None, end: str | None) -> dict[str, Any]:
            """Download one window, either end left open if it was not asked for."""
            return self._client.download(
                f"movie/{movie_id}/changes",
                {"start_date": start, "end_date": end, "page": page},
                log_id,
            )

        return MovieChangeLog.from_response(
            download_changes(start_date, end_date, _download),
        )

    # TODO: Validate
    def details(
        self,
        movie_id: int,
        *,
        append_to_response: str | None = None,
        language: str | None = None,
    ) -> Movie:
        """Get the top level details of a movie by ID.

        ## Append To Response

        This method supports using `append_to_response`. Read more about this
        [here](https://developer.themoviedb.org/docs/append-to-response).

        [Official Documentation](https://developer.themoviedb.org/reference/movie-details)

        Raises:
            InvalidFileError: If the response is for a different movie.
        """
        log_id = self.get_log_id(self.details, locals())
        data = self._client.download(
            f"movie/{movie_id}",
            {
                "append_to_response": append_to_response,
                "language": language or self._client.language,
            },
            log_id=log_id,
        )
        if data.get("id") != movie_id:
            raise InvalidFileError(field="movie id", expected=movie_id, response=data)
        return Movie.from_response(data)

    # TODO: Validate
    def watch_providers(self, movie_id: int) -> MovieProviders:
        """Get the list of streaming providers we have for a movie.

        Powered by our partnership with JustWatch, you can query this method to get
        a list of the streaming/rental/purchase availabilities per country by
        provider.

        This is *not* going to return full deep links, but rather, it's just enough
        information to display what's available where.

        You can link to the provided TMDB URL to help support TMDB and provide the
        actual deep links to the content.

        > 📘 JustWatch Attribution Required
        >
        > In order to use this data you must attribute the source of the data as
        > **JustWatch**. If we find any usage not complying with these terms we
        > will revoke access to the API.

        [Official Documentation](https://developer.themoviedb.org/reference/movie-watch-providers)

        Raises:
            InvalidFileError: If the response is for a different movie.
        """
        log_id = self.get_log_id(self.watch_providers, locals())
        data = self._client.download(
            f"movie/{movie_id}/watch/providers",
            {},
            log_id=log_id,
        )
        if data.get("id") != movie_id:
            raise InvalidFileError(field="movie id", expected=movie_id, response=data)
        return MovieProviders.from_response(data)
