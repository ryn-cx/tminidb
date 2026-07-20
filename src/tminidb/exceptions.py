# TODO: Validate
"""Exceptions."""

from __future__ import annotations


class TminidbError(Exception):
    """Base exception for TMiniDB."""


class HTTPError(TminidbError):
    """Raised when HTTP request fails with unexpected status code."""
