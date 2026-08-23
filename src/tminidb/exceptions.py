# TODO: Validate
"""Exceptions."""

from __future__ import annotations

from typing import Any


# TODO: Validate
class TminidbError(Exception):
    """Base exception for TMiniDB."""

    response: str | dict[str, Any] | None = None


# TODO: Validate
class HTTPError(TminidbError):
    """Raised when HTTP request fails with unexpected status code."""

    # TODO: Validate
    def __init__(
        self,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize the HTTPError with the status code and response body."""
        self.status_code = status_code
        self.response = response
        super().__init__(f"Unexpected response status code: {status_code}")


# TODO: Validate
class ResourceNotFoundError(HTTPError):
    """Raised when the API reports that the requested resource does not exist."""


# TODO: Validate
class MovieNotFoundError(ResourceNotFoundError):
    """Raised when the requested movie does not exist."""

    # TODO: Validate
    def __init__(
        self,
        movie_id: int,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the movie id and the originating response."""
        self.movie_id = movie_id
        super().__init__(status_code, response)


# TODO: Validate
class SeriesNotFoundError(ResourceNotFoundError):
    """Raised when the requested TV series does not exist."""

    # TODO: Validate
    def __init__(
        self,
        series_id: int,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the series id and the originating response."""
        self.series_id = series_id
        super().__init__(status_code, response)


# TODO: Validate
class SeasonNotFoundError(ResourceNotFoundError):
    """Raised when the requested season of a TV series does not exist."""

    # TODO: Validate
    def __init__(
        self,
        series_id: int,
        season_number: int,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the series id, season number and originating response."""
        self.series_id = series_id
        self.season_number = season_number
        super().__init__(status_code, response)


# TODO: Validate
class SeasonChangesNotFoundError(ResourceNotFoundError):
    """Raised when the season a change log was asked for does not exist."""

    # TODO: Validate
    def __init__(
        self,
        season_id: int,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the season id and the originating response."""
        self.season_id = season_id
        super().__init__(status_code, response)


# TODO: Validate
class EpisodeNotFoundError(ResourceNotFoundError):
    """Raised when the requested episode of a TV series does not exist."""

    # TODO: Validate
    def __init__(
        self,
        series_id: int,
        season_number: int,
        episode_number: int,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the episode's numbers and the originating response."""
        self.series_id = series_id
        self.season_number = season_number
        self.episode_number = episode_number
        super().__init__(status_code, response)


# TODO: Validate
class EpisodeChangesNotFoundError(ResourceNotFoundError):
    """Raised when the episode a change log was asked for does not exist."""

    # TODO: Validate
    def __init__(
        self,
        episode_id: int,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the episode id and the originating response."""
        self.episode_id = episode_id
        super().__init__(status_code, response)


# TODO: Validate
class EpisodeGroupNotFoundError(ResourceNotFoundError):
    """Raised when the requested episode group does not exist."""

    # TODO: Validate
    def __init__(
        self,
        episode_group_id: str,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the episode group id and the originating response."""
        self.episode_group_id = episode_group_id
        super().__init__(status_code, response)


# TODO: Validate
class InvalidFileError(TminidbError):
    """Raised when a downloaded file does not match what was requested."""

    # TODO: Validate
    def __init__(
        self,
        field: str,
        expected: object,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the field, the value it should hold and the response."""
        self.field = field
        self.expected = expected
        self.response = response
        super().__init__(f"Downloaded file is not for {field} {expected!r}")
