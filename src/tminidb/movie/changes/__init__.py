# TODO: Validate
"""Get the recent changes for a movie.

Source: https://developer.themoviedb.org/reference/movie-changes
"""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import TYPE_CHECKING

from tminidb.base_changes import BaseChanges
from tminidb.exceptions import MovieNotFoundError, ResourceNotFoundError
from tminidb.movie.changes.models import MovieChangesModel, model_validate_json

if TYPE_CHECKING:
    from datetime import date

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class MovieChanges(BaseChanges[MovieChangesModel]):
    """Get the recent changes for a movie.

    By default only the last 24 hours are returned.

    You can query up to 14 days in a single query by using the `start_date` and
    `end_date` query parameters.

    A longer range is downloaded a window at a time by `download_merged`.

    Source: https://developer.themoviedb.org/reference/movie-changes
    """

    MODEL = MovieChangesModel
    LOAD = staticmethod(model_validate_json)

    # TODO: Validate
    def __call__(
        self,
        movie_id: int,
        *,
        start_date: date | None = None,
        end_date: date | None = None,
        page: int = 1,
    ) -> MovieChangesModel:
        """Get the recent changes for a movie.

        Source: https://developer.themoviedb.org/reference/movie-changes
        """
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(
                movie_id,
                start_date=start_date,
                end_date=end_date,
                page=page,
            ),
            log_id,
        )

    # TODO: Validate
    def download(
        self,
        movie_id: int,
        *,
        start_date: date | None = None,
        end_date: date | None = None,
        page: int = 1,
    ) -> str:
        """Download one window of the movie change log.

        Raises:
            MovieNotFoundError: If nothing is under that id.
        """
        log_id = self.get_log_id(self.download, locals())
        try:
            return self._download(
                f"movie/{movie_id}/changes",
                start_date=start_date,
                end_date=end_date,
                page=page,
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise MovieNotFoundError(movie_id, err.status_code, err.response) from err

    # TODO: Validate
    def download_merged(
        self,
        movie_id: int,
        start_date: date,
        end_date: date,
        *,
        page: int = 1,
    ) -> str:
        """Download the whole range as one file, a 14 day window at a time.

        Raises:
            MovieNotFoundError: If nothing is under that id.
        """
        log_id = self.get_log_id(self.download_merged, locals())
        try:
            return self._download_merged(
                f"movie/{movie_id}/changes",
                start_date=start_date,
                end_date=end_date,
                page=page,
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise MovieNotFoundError(movie_id, err.status_code, err.response) from err
