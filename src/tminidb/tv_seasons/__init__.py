# TODO: Validate
"""Contains the TvSeasonEndpoints class.

Every endpoint the API's docs file under TV Seasons is a method here, reached the
way the API reaches it: `client.tv_seasons.details(1396, 1)` is
`tv/1396/season/1` and is the whole of it, because the method both downloads and
reads.

[Official Documentation](https://developer.themoviedb.org/reference/tv-season-details)
"""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any

from tminidb._changes import download_changes
from tminidb.base_endpoint import BaseEndpoint
from tminidb.exceptions import InvalidFileError
from tminidb.tv_seasons.models.changes import TvSeasonChangeLog
from tminidb.tv_seasons.models.details import TvSeason

if TYPE_CHECKING:
    from datetime import date

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class TvSeasonEndpoints(BaseEndpoint):
    """The endpoints the API's docs file under TV Seasons.

    [Official Documentation](https://developer.themoviedb.org/reference/tv-season-details)
    """

    # TODO: Validate
    def changes(
        self,
        season_id: int,
        *,
        start_date: date | None = None,
        end_date: date | None = None,
        page: int = 1,
    ) -> TvSeasonChangeLog:
        """Get the recent changes for a TV season.

        Get the changes for a TV season. By default only the last 24 hours are
        returned.

        You can query up to 14 days in a single query by using the `start_date` and
        `end_date` query parameters.

        > 📘 Note
        >
        > TV season changes are a little different than movie changes in that there
        > are some edits on episodes that will create a top level change entry at the
        > season level. These can be found under the episode keys. These keys will
        > contain a  `episode_id`. You can use the episode changes methods to look
        > these up individually.

        [Official Documentation](https://developer.themoviedb.org/reference/tv-season-changes-by-id)

        If the query is more than 14 days multiple queries will be made and the results
        will be merged together.
        """
        log_id = self.get_log_id(self.changes, locals())

        # TODO: Validate
        def _download(start: str | None, end: str | None) -> dict[str, Any]:
            """Download one window, either end left open if it was not asked for."""
            return self._client.download(
                f"tv/season/{season_id}/changes",
                {
                    "start_date": start,
                    "end_date": end,
                    "page": page,
                },
                log_id=log_id,
            )

        return self.load_changes(
            download_changes(start_date, end_date, _download),
        )

    # TODO: Validate
    def load_changes(self, data: dict[str, Any]) -> TvSeasonChangeLog:
        """Read a response the changes endpoint answered with."""
        return TvSeasonChangeLog.from_response(data)

    # TODO: Validate
    def details(
        self,
        series_id: int,
        season_number: int,
        *,
        append_to_response: str | None = None,
        language: str | None = None,
    ) -> TvSeason:
        """Query the details of a TV season.

        This method supports using `append_to_response`. Read more about this
        [here](https://developer.themoviedb.org/docs/append-to-response).

        [Official Documentation](https://developer.themoviedb.org/reference/tv-season-details)

        Raises:
            InvalidFileError: If the response is for a different season.
        """
        log_id = self.get_log_id(self.details, locals())
        data = self._client.download(
            f"tv/{series_id}/season/{season_number}",
            {
                "append_to_response": append_to_response,
                "language": language or self._client.language,
            },
            log_id=log_id,
        )
        # `id` is the season's own id, so the season number is what identifies
        # the file as the one that was asked for.
        if data.get("season_number") != season_number:
            raise InvalidFileError(
                field="season number",
                expected=season_number,
                response=data,
            )
        return self.load_details(data)

    # TODO: Validate
    def load_details(self, data: dict[str, Any]) -> TvSeason:
        """Read a response the details endpoint answered with."""
        return TvSeason.from_response(data)
