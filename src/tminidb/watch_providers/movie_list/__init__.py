# TODO: Validate
"""Get the list of streaming providers we have for movies.

Source: https://developer.themoviedb.org/reference/watch-providers-movie-list
"""

from __future__ import annotations

from logging import NullHandler, getLogger

from tminidb.base_watch_providers_list import BaseWatchProvidersList
from tminidb.watch_providers.movie_list.models import (
    WatchProvidersMovieListModel,
    model_validate_json,
)

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class WatchProvidersMovieList(BaseWatchProvidersList[WatchProvidersMovieListModel]):
    """Get the list of streaming providers we have for movies.

    Returns a list of the watch provider (OTT/streaming) data we have available for
    movies. You can specify a `watch_region` param if you want to further filter the
    list by country.

    JustWatch attribution required: in order to use this data you must attribute the
    source of the data as JustWatch. If we find any usage not complying with these terms
    we will revoke access to the API.

    Source: https://developer.themoviedb.org/reference/watch-providers-movie-list
    """

    MODEL = WatchProvidersMovieListModel
    LOAD = staticmethod(model_validate_json)

    # TODO: Validate
    def __call__(
        self,
        *,
        language: str | None = None,
        watch_region: str | None = None,
    ) -> WatchProvidersMovieListModel:
        """Get the list of streaming providers we have for movies.

        Source: https://developer.themoviedb.org/reference/watch-providers-movie-list
        """
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(language=language, watch_region=watch_region),
            log_id,
        )

    # TODO: Validate
    def download(
        self,
        *,
        language: str | None = None,
        watch_region: str | None = None,
    ) -> str:
        """Download the movie watch provider list file."""
        log_id = self.get_log_id(self.download, locals())
        return self._download(
            "watch/providers/movie",
            language=language,
            watch_region=watch_region,
            log_id=log_id,
        )
