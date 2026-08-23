# TODO: Validate
"""Contains the TvSeason class."""

from __future__ import annotations

import json
from logging import NullHandler, getLogger

from tminidb.details.base import BaseDetails
from tminidb.details.tv_season.models import TvSeasonModel, model_validate_json
from tminidb.exceptions import (
    InvalidFileError,
    ResourceNotFoundError,
    SeasonNotFoundError,
)

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class TvSeason(BaseDetails[TvSeasonModel]):
    """Manage the TV season details file.

    Source: https://www.themoviedb.org/tv/{series_id}/season/{season_number}

    Example request:
        - GET /3/tv/{series_id}/season/{season_number}?
            - language=en-US
            - HTTP/2
        - Host: api.themoviedb.org
        - Accept: application/json
        - Authorization: Bearer __REDACTED__
    """

    MODEL = TvSeasonModel
    LOAD = staticmethod(model_validate_json)

    # TODO: Validate
    def __call__(
        self,
        series_id: int,
        season_number: int,
        *,
        append_to_response: str | None = None,
        language: str | None = None,
    ) -> TvSeasonModel:
        """Look the TV season up and return the model it is read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(
                series_id,
                season_number,
                append_to_response=append_to_response,
                language=language,
            ),
            log_id,
        )

    # TODO: Validate
    def download(
        self,
        series_id: int,
        season_number: int,
        *,
        append_to_response: str | None = None,
        language: str | None = None,
    ) -> str:
        """Download the TV season details file.

        Raises:
            SeasonNotFoundError: If the series has no such season.
        """
        log_id = self.get_log_id(self.download, locals())
        try:
            response = self._download(
                f"tv/{series_id}/season/{season_number}",
                append_to_response=append_to_response,
                language=language,
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise SeasonNotFoundError(
                series_id,
                season_number,
                err.status_code,
                err.response,
            ) from err
        return self._validate_download(response, season_number)

    # TODO: Validate
    @staticmethod
    def _validate_download(response: str, season_number: int) -> str:
        # `id` is the season's own id, so the season number is what says the file
        # is the one that was asked for.
        if json.loads(response).get("season_number") != season_number:
            raise InvalidFileError(
                field="season number",
                expected=season_number,
                response=response,
            )
        return response
