# TODO: Validate
"""Get the list of streaming providers we have for a movie.

Powered by our partnership with JustWatch, you can query this method to get a
list of the streaming/rental/purchase availabilities per country by provider.

This is *not* going to return full deep links, but rather, it's just enough
information to display what's available where.

You can link to the provided TMDB URL to help support TMDB and provide the
actual deep links to the content.

> 📘 JustWatch Attribution Required
>
> In order to use this data you must attribute the source of the data as
> **JustWatch**. If we find any usage not complying with these terms we will
> revoke access to the API.

[Official Documentation](https://developer.themoviedb.org/reference/movie-watch-providers)
"""

from __future__ import annotations

from logging import NullHandler, getLogger

from tminidb.base_endpoint import BaseEndpoint, records_call
from tminidb.exceptions import InvalidFileError
from tminidb.movies.watch_providers.models import MovieProviders

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class MovieWatchProviders(BaseEndpoint):
    """Get the list of streaming providers we have for a movie.

    Powered by our partnership with JustWatch, you can query this method to get a
    list of the streaming/rental/purchase availabilities per country by provider.

    This is *not* going to return full deep links, but rather, it's just enough
    information to display what's available where.

    You can link to the provided TMDB URL to help support TMDB and provide the
    actual deep links to the content.

    > 📘 JustWatch Attribution Required
    >
    > In order to use this data you must attribute the source of the data as
    > **JustWatch**. If we find any usage not complying with these terms we will
    > revoke access to the API.

    [Official Documentation](https://developer.themoviedb.org/reference/movie-watch-providers)
    """

    # TODO: Validate
    @records_call
    def __call__(self, movie_id: int) -> MovieProviders:
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
        log_id = self.log_id()
        data = self._client.download(
            f"movie/{movie_id}/watch/providers",
            {},
            log_id=log_id,
        )
        if data.get("id") != movie_id:
            raise InvalidFileError(field="movie id", expected=movie_id, response=data)
        return MovieProviders.from_response(data)
