# TODO: Validate
"""The test whose recordings are being read or written."""

from __future__ import annotations

from contextvars import ContextVar

CURRENT_TEST: ContextVar[str] = ContextVar("CURRENT_TEST")
"""The name of the test the recordings in play belong to.

Every test of an endpoint asks for the same thing under a different set of
arguments, so what tells two recordings of one endpoint apart is the test that
asked for them rather than anything in the request.
"""
