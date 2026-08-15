# TODO: Validate
"""Exceptions."""

from __future__ import annotations

from json import JSONDecodeError, loads
from typing import Any


class TminidbError(Exception):
    """Base exception for TMiniDB.

    Every error carries the data that caused it in `response`, so a caller that
    catches one can still inspect what came back instead of only reading the
    message. What `response` holds depends on the error, but it is always the
    original, unmodified value: the parsed body for an error raised from a
    response, and the raw text when the body could not be parsed as JSON.
    """

    response: Any = None
    """The original data that caused the error, or `None` if there was none."""


class HTTPError(TminidbError):
    """Raised when HTTP request fails with unexpected status code."""

    def __init__(self, status_code: int, body: str) -> None:
        """Initialize the HTTPError with the status code and response body.

        An error response is not guaranteed to be JSON, so `response` falls back
        to the raw text when it cannot be parsed.
        """
        self.status_code = status_code
        self.body = body
        self.response = _parsed_or_raw(body)
        super().__init__(f"Unexpected response status code: {status_code}\n{body}")


class InvalidFileError(TminidbError):
    """Raised when a downloaded file does not match what was requested."""

    def __init__(
        self,
        field: str,
        expected: object = None,
        *,
        response: Any = None,  # noqa: ANN401 - A response body can be any JSON value.
    ) -> None:
        """Initialize the InvalidFileError with the field and its expected value.

        `expected` is left out when the check is only that the field has a value.
        `response` is the downloaded data that failed the check, which is what
        makes it possible to see why it failed.
        """
        self.field = field
        self.expected = expected
        self.response = response
        if expected is None:
            super().__init__(f"Downloaded file has no {field}")
        else:
            super().__init__(f"Downloaded file is not for {field} {expected!r}")


def _parsed_or_raw(body: str) -> Any:  # noqa: ANN401 - A response body can be any JSON value.
    """Return `body` parsed as JSON, or the raw text if it is not JSON."""
    try:
        return loads(body)
    except JSONDecodeError:
        return body
