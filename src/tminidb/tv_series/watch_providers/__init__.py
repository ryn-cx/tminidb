# TODO: Validate
"""Get the list of streaming providers we have for a TV show.

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

[Official Documentation](https://developer.themoviedb.org/reference/tv-series-watch-providers)
"""

from __future__ import annotations

from logging import NullHandler, getLogger

from tminidb.base_endpoint import BaseEndpoint, records_call
from tminidb.exceptions import InvalidFileError
from tminidb.tv_series.watch_providers.models import TvProviders

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class TvWatchProviders(BaseEndpoint):
    """Get the list of streaming providers we have for a TV show.

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

    [Official Documentation](https://developer.themoviedb.org/reference/tv-series-watch-providers)
    """

    # TODO: Validate
    @records_call
    def __call__(self, series_id: int) -> TvProviders:
        """Get the list of streaming providers we have for a TV show.

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

        [Official Documentation](https://developer.themoviedb.org/reference/tv-series-watch-providers)

        Raises:
            InvalidFileError: If the response is for a different series.
        """
        log_id = self.log_id()
        data = self._client.download(
            f"tv/{series_id}/watch/providers",
            {},
            log_id=log_id,
        )
        if data.get("id") != series_id:
            raise InvalidFileError(field="series id", expected=series_id, response=data)
        return TvProviders.from_response(data)
