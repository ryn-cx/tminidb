# TODO: Validate
"""Get the list of streaming providers we have for a movie.

Source: https://developer.themoviedb.org/reference/movie-watch-providers
"""

from __future__ import annotations

from logging import NullHandler, getLogger

from tminidb.base_watch_providers import BaseWatchProviders
from tminidb.exceptions import MovieNotFoundError, ResourceNotFoundError
from tminidb.movie.watch_providers.models import (
    MovieWatchProvidersModel,
    model_validate_json,
)

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class MovieWatchProviders(BaseWatchProviders[MovieWatchProvidersModel]):
    """Get the list of streaming providers we have for a movie.

    Powered by our partnership with JustWatch, you can query this method to get a list
    of the streaming/rental/purchase availabilities per country by provider.

    This is *not* going to return full deep links, but rather, it's just enough
    information to display what's available where.

    You can link to the provided TMDB URL to help support TMDB and provide the actual
    deep links to the content.

    JustWatch attribution required: in order to use this data you must attribute the
    source of the data as JustWatch. If we find any usage not complying with these terms
    we will revoke access to the API.

    Source: https://developer.themoviedb.org/reference/movie-watch-providers
    """

    MODEL = MovieWatchProvidersModel
    LOAD = staticmethod(model_validate_json)

    # TODO: Validate
    def __call__(self, movie_id: int) -> MovieWatchProvidersModel:
        """Get the list of streaming providers we have for a movie.

        Source: https://developer.themoviedb.org/reference/movie-watch-providers
        """
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(movie_id), log_id)

    # TODO: Validate
    def download(self, movie_id: int) -> str:
        """Download the movie watch providers file.

        Raises:
            MovieNotFoundError: If no movie is under that id.
        """
        log_id = self.get_log_id(self.download, locals())
        try:
            response = self._download(
                f"movie/{movie_id}/watch/providers",
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise MovieNotFoundError(movie_id, err.status_code, err.response) from err
        return self._validate_download(response, "movie id", movie_id)
