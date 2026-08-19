from __future__ import annotations

from contextvars import ContextVar
from functools import wraps
from inspect import signature
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Callable

    from tminidb import TMiniDB

_CALL_ARGS: ContextVar[dict[str, Any]] = ContextVar("_CALL_ARGS")
"""The arguments the endpoint being run was called with."""


# TODO: Validate
def records_call[**P, R](func: Callable[P, R]) -> Callable[P, R]:
    """Records the arguments an endpoint was called with, for `log_id`.

    The defaults are bound by the time the body runs, so an argument that was
    given and one that was left out are the same thing to `locals()`. Binding
    the call here keeps only what the caller actually passed, which is what
    makes a log id say what was asked for rather than what it amounted to.
    """

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        supplied = signature(func).bind(*args, **kwargs).arguments
        supplied.pop("self", None)
        token = _CALL_ARGS.set(supplied)
        try:
            return func(*args, **kwargs)
        finally:
            _CALL_ARGS.reset(token)

    return wrapper


class BaseEndpoint:
    """Base class for API endpoints."""

    def __init__(self, client: TMiniDB) -> None:
        """Initialize the endpoint with the TMiniDB client."""
        self._client = client

    # TODO: Validate
    def log_id(self) -> str:
        """Returns the log id of the call being run.

        Example: ClassName (arg1='value1' arg2='value2')

        Only a call through a `records_call` endpoint has arguments to name, so
        anything else is identified by the endpoint alone.
        """
        parts = [f"{name}={value!r}" for name, value in _CALL_ARGS.get({}).items()]
        name = self.__class__.__name__
        if not parts:
            return name
        return f"{name} ({' '.join(parts)})"
