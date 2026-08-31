# TODO: Validate
"""Get the list of streaming providers we have for a TV season.

Source: https://developer.themoviedb.org/reference/tv-season-watch-providers
"""

from __future__ import annotations

from logging import NullHandler, getLogger

from tminidb.base_watch_providers import BaseWatchProviders
from tminidb.exceptions import ResourceNotFoundError, SeasonNotFoundError
from tminidb.tv_season.watch_providers.models import (
    TvSeasonWatchProvidersModel,
    model_validate_json,
)

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class TvSeasonWatchProviders(BaseWatchProviders[TvSeasonWatchProvidersModel]):
    """Get the list of streaming providers we have for a TV season.

    Powered by our partnership with JustWatch, you can query this method to get a list
    of the streaming/rental/purchase availabilities per country by provider.

    This is *not* going to return full deep links, but rather, it's just enough
    information to display what's available where.

    You can link to the provided TMDB URL to help support TMDB and provide the actual
    deep links to the content.

    JustWatch attribution required: in order to use this data you must attribute the
    source of the data as JustWatch. If we find any usage not complying with these terms
    we will revoke access to the API.

    Source: https://developer.themoviedb.org/reference/tv-season-watch-providers
    """

    MODEL = TvSeasonWatchProvidersModel
    LOAD = staticmethod(model_validate_json)

    # TODO: Validate
    def __call__(
        self,
        series_id: int,
        season_number: int,
    ) -> TvSeasonWatchProvidersModel:
        """Get the list of streaming providers we have for a TV season.

        Source: https://developer.themoviedb.org/reference/tv-season-watch-providers
        """
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(series_id, season_number), log_id)

    # TODO: Validate
    def download(self, series_id: int, season_number: int) -> str:
        """Download the TV season watch providers file.

        The file carries the season's own id rather than the series id or the
        season number, so there is nothing in it to hold against what was asked
        for.

        Raises:
            SeasonNotFoundError: If the series has no such season.
        """
        log_id = self.get_log_id(self.download, locals())
        try:
            return self._download(
                f"tv/{series_id}/season/{season_number}/watch/providers",
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise SeasonNotFoundError(
                series_id,
                season_number,
                err.status_code,
                err.response,
            ) from err
