# TODO: Validate
"""Contains the TvSeasonDetails class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any

from tminidb.base_api_endpoint import BaseEndpoint
from tminidb.exceptions import InvalidFileError
from tminidb.tv_season_details.models import TvSeasonDetailsModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class TvSeasonDetails(BaseEndpoint[TvSeasonDetailsModel]):
    """Manage the TV season details file.

    Wraps `GET /tv/{series_id}/season/{season_number}`:
    https://developer.themoviedb.org/reference/tv-season-details
    """

    _response_model = TvSeasonDetailsModel

    def download(
        self,
        series_id: int,
        season_number: int,
        *,
        append_to_response: str | None = None,
        language: str | None = None,
    ) -> dict[str, Any]:
        """Downloads the TV season details file."""
        log_id = self.get_log_id(self.download, locals())
        data = self._client.download(
            f"tv/{series_id}/season/{season_number}",
            {
                "append_to_response": append_to_response,
                "language": language or self._client.language,
            },
            log_id=log_id,
        )
        # `id` is the season's own id, so the season number is what identifies
        # the file as the one that was asked for.
        if data.get("season_number") != season_number:
            raise InvalidFileError(
                field="season number",
                expected=season_number,
                response=data,
            )
        return data

    def download_and_parse(
        self,
        series_id: int,
        season_number: int,
        *,
        append_to_response: str | None = None,
        language: str | None = None,
    ) -> TvSeasonDetailsModel:
        """Downloads and parses the TV season details file."""
        return self.parse(
            self.download(
                series_id,
                season_number,
                append_to_response=append_to_response,
                language=language,
            ),
        )
