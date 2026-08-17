# TODO: Validate
"""Contains the MovieChanges class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any

from tminidb._changes import download_chunks
from tminidb.base_api_endpoint import BaseEndpoint
from tminidb.exceptions import InvalidFileError
from tminidb.movie_changes.models import MovieChangesModel

if TYPE_CHECKING:
    from datetime import date

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class MovieChanges(BaseEndpoint[MovieChangesModel]):
    """Manage the movie changes file.

    Wraps `GET /movie/{movie_id}/changes`:
    https://developer.themoviedb.org/reference/movie-changes

    Every change is grouped under the field it happened to, and each group
    holds one item per edit. An item carries `value`, and `original_value` when
    the edit replaced something, but what those hold depends on the field the
    group is for, so a change is only meaningful alongside its `key`.

    The window defaults to the last 24 hours and cannot be wider than 14 days.
    Nothing in the response says which movie it is for, and an id that
    belongs to no movie is answered with an empty list rather than with an
    error, so an empty result does not mean the id was good.
    """

    _response_model = MovieChangesModel

    # TODO: Validate
    def download(
        self,
        movie_id: int,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
        page: int = 1,
    ) -> dict[str, Any]:
        """Downloads the movie changes file.

        Args:
            movie_id: The movie to read the changes of.
            start_date: Oldest change to return, as `YYYY-MM-DD`.
            end_date: Newest change to return, as `YYYY-MM-DD`.
            page: Page of changes to return.
        """
        log_id = self.get_log_id(self.download, locals())
        data = self._client.download(
            f"movie/{movie_id}/changes",
            {
                "start_date": start_date,
                "end_date": end_date,
                "page": page,
            },
            log_id=log_id,
        )
        # Nothing in the response identifies the movie it is for, so the
        # only thing worth checking is that there is a list of changes at all.
        if data.get("changes") is None:
            raise InvalidFileError(field="changes", response=data)
        return data

    # TODO: Validate
    def download_and_parse(
        self,
        movie_id: int,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
        page: int = 1,
    ) -> MovieChangesModel:
        """Downloads and parses the movie changes file."""
        return self.parse(
            self.download(
                movie_id,
                start_date=start_date,
                end_date=end_date,
                page=page,
            ),
        )

    # TODO: Validate
    def download_since(
        self,
        movie_id: int,
        start_date: date,
        *,
        end_date: date | None = None,
        page: int = 1,
    ) -> dict[str, Any]:
        """Downloads every movie change since a date, 14 days at a time.

        A window cannot be wider than 14 days, so a longer one is asked for a
        chunk at a time and the chunks are merged into a single response of the
        same shape a single window comes back in.

        Args:
            movie_id: The movie to read the changes of.
            start_date: Oldest change to return.
            end_date: Newest change to return. Defaults to today.
            page: Page of changes to return from each window.
        """
        return download_chunks(
            start_date,
            end_date,
            lambda chunk_start, chunk_end: self.download(
                movie_id,
                start_date=chunk_start,
                end_date=chunk_end,
                page=page,
            ),
        )

    # TODO: Validate
    def download_and_parse_since(
        self,
        movie_id: int,
        start_date: date,
        *,
        end_date: date | None = None,
        page: int = 1,
    ) -> MovieChangesModel:
        """Downloads and parses every movie change since a date."""
        return self.parse(
            self.download_since(
                movie_id,
                start_date,
                end_date=end_date,
                page=page,
            ),
        )
