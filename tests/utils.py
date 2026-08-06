# TODO: Validate
"""Utils."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest

from tminidb.constants import FILES_PATH

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path
    from typing import Any

    from good_ass_pydantic_integrator import GAPIBaseModel, GAPIClient

    from tminidb.base_api_endpoint import BaseEndpoint


def json_path(
    endpoint: GAPIClient[Any],
    name: str,
    *,
    folder: str | None = None,
) -> Path:
    if folder is not None:
        return FILES_PATH / folder / f"{name}.json"
    return endpoint.json_files_folder() / f"{name}.json"


def parse_json_to_model[T: GAPIBaseModel](endpoint: BaseEndpoint[T], name: str) -> T:
    path = json_path(endpoint, name)
    return endpoint.parse(json.loads(path.read_text()))


def parse_json_to_dict(endpoint: BaseEndpoint[Any], name: str) -> dict[str, Any]:
    return json.loads(json_path(endpoint, name).read_text())


def parse_json_to_list_of_dicts(
    endpoint: BaseEndpoint[Any],
    name: str,
    *,
    folder: str | None = None,
) -> list[dict[str, Any]]:
    content: list[dict[str, Any]] | dict[str, Any] = json.loads(
        json_path(endpoint, name, folder=folder).read_text(),
    )
    return content if isinstance(content, list) else [content]


def parse_json_to_list_of_models[T: GAPIBaseModel](
    endpoint: BaseEndpoint[T],
    name: str,
    *,
    folder: str | None = None,
) -> list[T]:
    return [
        endpoint.parse(page)
        for page in parse_json_to_list_of_dicts(endpoint, name, folder=folder)
    ]


def download_and_save(
    endpoint: GAPIClient[Any],
    name: str,
    get: Callable[[], dict[str, Any] | list[dict[str, Any]]],
    *,
    folder: str | None = None,
) -> Path:
    path = json_path(endpoint, name, folder=folder)
    if path.exists():
        pytest.skip(f"File already recorded for {type(endpoint).__name__}/{name}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(get(), indent=2))
    return path


def assert_error(
    endpoint: GAPIClient[Any],
    name: str,
    download: Callable[[], object],
    error: type[Exception],
) -> None:
    if get_error_path(endpoint, name).exists():
        pytest.skip(f"File already recorded for {type(endpoint).__name__}/{name}")
    with pytest.raises(error) as excinfo:
        download()
    record_error(endpoint, name, getattr(excinfo.value, "response", None))


def get_error_path(endpoint: GAPIClient[Any], name: str) -> Path:
    folder = f"Errors/{endpoint.json_files_folder().name}"
    return json_path(endpoint, name, folder=folder)


def record_error(
    endpoint: GAPIClient[Any],
    name: str,
    data: dict[str, Any] | None = None,
) -> None:
    path = get_error_path(endpoint, name)
    path.parent.mkdir(parents=True, exist_ok=True)
    content = json.dumps(data, indent=2) if data is not None else ""
    path.write_text(content)
