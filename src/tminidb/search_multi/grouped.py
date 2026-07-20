"""Contains the SearchMultiGrouped class."""

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, cast, override

from tminidb.search_multi import BaseSearchMulti, SearchMulti
from tminidb.search_multi.grouped_models import SearchMultiGroupedModel

if TYPE_CHECKING:
    from pathlib import Path

    from good_ass_pydantic_integrator.constants import INPUT_TYPE


class SearchMultiGrouped(BaseSearchMulti[SearchMultiGroupedModel]):
    """SearchMultiGrouped endpoint.

    Wraps `GET /search/multi` and groups the results by `media_type`:
    https://developer.themoviedb.org/reference/search-multi
    """

    _response_model = SearchMultiGroupedModel

    @override
    @classmethod
    def json_files_folder(cls) -> Path:
        return SearchMulti.json_files_folder()

    @override
    @classmethod
    def transform_input(cls, data: INPUT_TYPE) -> INPUT_TYPE:
        """Groups `results` by `media_type`."""
        if not isinstance(data, Mapping):
            msg = "Invalid input data type."
            raise TypeError(msg)

        model = SearchMulti.parse(data, update_model=False)
        # Start with empty lists so the values are never None.
        grouped: dict[str, list[dict[str, Any]]] = {"movie": [], "tv": [], "person": []}
        for item in model.results:
            result = cast("dict[str, Any]", item.raw_input)
            grouped[item.media_type].append(
                {key: value for key, value in result.items() if key != "media_type"},
            )

        return cast("INPUT_TYPE", {**data, "results": grouped})
