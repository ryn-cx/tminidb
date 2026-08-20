# TODO: Validate
"""Contains the TvSeriesEndpoints class.

Every endpoint the API's docs file under TV Series is a method here, reached the
way the API reaches it: `client.tv_series.details(1396)` is `tv/1396` and is the
whole of it, because the method both downloads and reads.

[Official Documentation](https://developer.themoviedb.org/reference/tv-series-details)
"""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any

from tminidb._changes import download_changes
from tminidb.base_endpoint import BaseEndpoint
from tminidb.exceptions import InvalidFileError
from tminidb.tv_series.models.changes import TvSeriesChangeLog
from tminidb.tv_series.models.details import TvSeries
from tminidb.tv_series.models.episode_groups import EpisodeGroups
from tminidb.tv_series.models.watch_providers import TvProviders

if TYPE_CHECKING:
    from datetime import date

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class TvSeriesEndpoints(BaseEndpoint):
    """The endpoints the API's docs file under TV Series.

    [Official Documentation](https://developer.themoviedb.org/reference/tv-series-details)
    """

    # TODO: Validate
    def changes(
        self,
        series_id: int,
        *,
        start_date: date | None = None,
        end_date: date | None = None,
        page: int = 1,
    ) -> TvSeriesChangeLog:
        """Get the recent changes for a TV show.

        Get the changes for a TV show. By default only the last 24 hours are
        returned.

        You can query up to 14 days in a single query by using the `start_date` and
        `end_date` query parameters.

        > 📘 Note
        >
        > TV show changes are a little different than movie changes in that there are
        > some edits on seasons and episodes that will create a top level change entry
        > at the show level. These can be found under the season and episode keys.
        > These keys will contain a `series_id` and `episode_id`. You can use the
        > season changes and episode changes methods to look these up individually.

        [Official Documentation](https://developer.themoviedb.org/reference/tv-series-changes)

        If the query is more than 14 days multiple queries will be made and the results
        will be merged together.
        """
        log_id = self.get_log_id(self.changes, locals())

        # TODO: Validate
        def _download(start: str | None, end: str | None) -> dict[str, Any]:
            """Download one window, either end left open if it was not asked for."""
            return self._client.download(
                f"tv/{series_id}/changes",
                {
                    "start_date": start,
                    "end_date": end,
                    "page": page,
                },
                log_id=log_id,
            )

        return TvSeriesChangeLog.from_response(
            download_changes(start_date, end_date, _download),
        )

    # TODO: Validate
    def details(
        self,
        series_id: int,
        *,
        append_to_response: str | None = None,
        language: str | None = None,
    ) -> TvSeries:
        """Get the details of a TV show.

        ## Append To Response

        This method supports using `append_to_response`. Read more about this
        [here](https://developer.themoviedb.org/docs/append-to-response).

        [Official Documentation](https://developer.themoviedb.org/reference/tv-series-details)

        Raises:
            InvalidFileError: If the response is for a different series.
        """
        log_id = self.get_log_id(self.details, locals())
        data = self._client.download(
            f"tv/{series_id}",
            {
                "append_to_response": append_to_response,
                "language": language or self._client.language,
            },
            log_id=log_id,
        )
        if data.get("id") != series_id:
            raise InvalidFileError(field="series id", expected=series_id, response=data)
        return TvSeries.from_response(data)

    # TODO: Validate
    def episode_groups(self, series_id: int) -> EpisodeGroups:
        """Get the episode groups that have been added to a TV show.

        With a group ID you can call the get TV episode group details method.

        [Official Documentation](https://developer.themoviedb.org/reference/tv-series-episode-groups)

        Raises:
            InvalidFileError: If the response is for a different series.
        """
        log_id = self.get_log_id(self.episode_groups, locals())
        data = self._client.download(
            f"tv/{series_id}/episode_groups",
            {},
            log_id=log_id,
        )
        if data.get("id") != series_id:
            raise InvalidFileError(field="series id", expected=series_id, response=data)
        return EpisodeGroups.from_response(data)

    # TODO: Validate
    def watch_providers(self, series_id: int) -> TvProviders:
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
        log_id = self.get_log_id(self.watch_providers, locals())
        data = self._client.download(
            f"tv/{series_id}/watch/providers",
            {},
            log_id=log_id,
        )
        if data.get("id") != series_id:
            raise InvalidFileError(field="series id", expected=series_id, response=data)
        return TvProviders.from_response(data)
