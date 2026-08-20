# TODO: Validate
"""Exceptions."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    import httpx


# TODO: Validate
class TminidbError(Exception):
    """Base exception for TMiniDB.

    Every error carries what caused it in `response`, so a caller that catches
    one can still inspect it instead of only reading the message. What
    `response` holds depends on the error, but it is always the original,
    unmodified value: the whole response for an error raised from one, and the
    data that failed the check for the rest.
    """

    response: Any = None
    """The original data that caused the error, or `None` if there was none."""


# TODO: Validate
class HTTPError(TminidbError):
    """Raised when HTTP request fails with unexpected status code."""

    response: httpx.Response
    """The response that caused the error, request included."""

    # TODO: Validate
    def __init__(self, response: httpx.Response) -> None:
        """Initialize the HTTPError with the response that caused it.

        The response is kept whole rather than as its parsed body, so what was
        asked for is still reachable through `response.request`.
        """
        self.response = response
        super().__init__(
            f"Unexpected response status code: {response.status_code}\n{response.text}",
        )

    # TODO: Validate
    @property
    def status_code(self) -> int:
        """The status code of the response that caused the error."""
        return self.response.status_code

    # TODO: Validate
    @property
    def body(self) -> str:
        """The raw text of the response that caused the error."""
        return self.response.text


# TODO: Validate
class InvalidFileError(TminidbError):
    """Raised when a downloaded file does not match what was requested."""

    # TODO: Validate
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
