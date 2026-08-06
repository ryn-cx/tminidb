# TODO: Validate
"""Exceptions."""

from __future__ import annotations


class TminidbError(Exception):
    """Base exception for TMiniDB."""


class HTTPError(TminidbError):
    """Raised when HTTP request fails with unexpected status code."""

    def __init__(self, status_code: int, body: str) -> None:
        """Initialize the HTTPError with the status code and response body."""
        self.status_code = status_code
        self.body = body
        super().__init__(f"Unexpected response status code: {status_code}\n{body}")
