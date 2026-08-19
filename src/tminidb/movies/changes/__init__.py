"""Get the recent changes for a movie.

Get the changes for a movie. By default only the last 24 hours are returned.

You can query up to 14 days in a single query by using the `start_date` and
`end_date` query parameters.

[Official Documentation](https://developer.themoviedb.org/reference/movie-changes)

If the query is more than 14 days multiple queries will be made and the results will be
merged together.
"""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any

from tminidb._changes import download_changes
from tminidb.base_endpoint import BaseEndpoint, records_call
from tminidb.movies.changes.models import MovieChangeLog

if TYPE_CHECKING:
    from datetime import date

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class MovieChanges(BaseEndpoint):
    """Get the recent changes for a movie.

    Get the changes for a movie. By default only the last 24 hours are returned.

    You can query up to 14 days in a single query by using the `start_date` and
    `end_date` query parameters.

    [Official Documentation](https://developer.themoviedb.org/reference/movie-changes)

    If the query is more than 14 days multiple queries will be made and the results will
    be merged together.
    """

    @records_call
    def __call__(
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
        log_id = self.log_id()

        # TODO: Validate
        def _download(start: str | None, end: str | None) -> dict[str, Any]:
            return self._client.download(
                f"movie/{movie_id}/changes",
                {"start_date": start, "end_date": end, "page": page},
                log_id=log_id,
            )

        return MovieChangeLog.from_response(
            download_changes(start_date, end_date, _download),
        )
