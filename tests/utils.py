from __future__ import annotations

import json
from pathlib import Path
from typing import TYPE_CHECKING, Any, Protocol, Self

import pytest

from tests.current_test import CURRENT_TEST

if TYPE_CHECKING:
    from collections.abc import Callable


# TODO: Validate
def _recording_path(folder: str, endpoint: type, name: str) -> Path:
    """Returns the path a recording of `name` is kept at."""
    root = Path(__file__).parent / folder / endpoint.__name__
    return root / CURRENT_TEST.get() / f"{name}.json"


# TODO: Validate
class ResponseModel(Protocol):
    """A model that is read from an API response.

    Every endpoint reads its response into its own model, and what they have in
    common is only that they are read from one, so that is what is asked for
    here rather than a shared base class.
    """

    # TODO: Validate
    @classmethod
    def from_response(cls, data: dict[str, Any]) -> Self:
        """Returns the model the response is read into."""
        ...

    # TODO: Validate
    @classmethod
    def model_validate_json(cls, json_data: str) -> Self:
        """Returns the model read back from its recorded dump."""
        ...

    # TODO: Validate
    def model_dump(self, *, mode: str) -> dict[str, Any]:
        """Returns the model as the data it is recorded as."""
        ...


def recorded_file_path(endpoint: type, name: str) -> Path:
    """Returns the path of the recorded file."""
    return _recording_path("_files", endpoint, name)


def recorded_content(endpoint: type, name: str) -> dict[str, Any]:
    """Returns the content of the recorded file."""
    path = recorded_file_path(endpoint, name)
    if not path.exists():
        pytest.skip(f"No recorded response for {name}")
    content: dict[str, Any] = json.loads(path.read_text(encoding="utf-8"))
    return content


# TODO: Validate
def new_file_path(endpoint: type, name: str) -> Path:
    """Returns the path a response that does not match its recording is put."""
    return _recording_path("_new_files", endpoint, name)


# TODO: Validate
def record_test(
    endpoint: type,
    name: str,
    download: Callable[[], dict[str, Any]],
) -> None:
    """Downloads a response and checks it against what was recorded.

    Writing a recording fails the test rather than skipping it, because what was
    just written is only whatever the API happened to answer: it has to be read
    before it can stand in for correct.

    A response that does not match its recording is written to `_new_files` and
    the test fails. The recording is left alone, so the two can be diffed and
    the new one moved over the old one once it has been looked at.
    """
    path = recorded_file_path(endpoint, name)
    downloaded = download()

    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(downloaded, indent=2), encoding="utf-8")
        pytest.fail(f"No recorded response for {name}, so it was recorded now")

    new_path = new_file_path(endpoint, name)
    if downloaded != json.loads(path.read_text(encoding="utf-8")):
        new_path.parent.mkdir(parents=True, exist_ok=True)
        new_path.write_text(json.dumps(downloaded, indent=2), encoding="utf-8")
        pytest.fail(f"Response for {name} is not what was recorded, see {new_path}")

    # What is in `_new_files` is whatever last failed to match, so a response
    # that matches again clears it rather than leaving a stale mismatch behind.
    new_path.unlink(missing_ok=True)


# TODO: Validate
def recorded_model_path(endpoint: type, name: str) -> Path:
    """Returns the path of the recorded model dump."""
    return _recording_path("_models", endpoint, name)


# TODO: Validate
def recorded_model[ModelT: ResponseModel](
    endpoint: type,
    name: str,
    model: ModelT,
) -> ModelT:
    """Returns `model` as it was recorded, writing the recording the first time.

    A parse test compares what it read against this rather than against a model
    it builds from the same response, because a model built from the response
    mirrors whatever the reading does and cannot disagree with it.

    Writing a recording fails the test rather than skipping it, because what was
    just written is only whatever the reading currently produces: it is the
    thing being checked and has to be read before it can stand in for correct.
    """
    path = recorded_model_path(endpoint, name)
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(model.model_dump(mode="json"), indent=2),
            encoding="utf-8",
        )
        pytest.fail(f"No recorded model for {name}, so it was recorded now")
    return type(model).model_validate_json(path.read_text(encoding="utf-8"))


# TODO: Validate
def parse_test(endpoint: type, name: str, model: type[ResponseModel]) -> None:
    """Reads a recorded response and checks it against the recorded model."""
    data = recorded_content(endpoint, name)
    parsed = model.from_response(data)

    assert parsed == recorded_model(endpoint, name, parsed)
