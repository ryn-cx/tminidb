# TODO: Validate
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

If the query is more than 14 days multiple queries will be made and the results will be
merged together.
"""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any

from tminidb._changes import download_changes
from tminidb.base_endpoint import BaseEndpoint, records_call
from tminidb.tv_series.changes.models import TvSeriesChangeLog

if TYPE_CHECKING:
    from datetime import date

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class TvSeriesChanges(BaseEndpoint):
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

    If the query is more than 14 days multiple queries will be made and the results will
    be merged together.
    """

    # TODO: Validate
    @records_call
    def __call__(
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
        log_id = self.log_id()

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
