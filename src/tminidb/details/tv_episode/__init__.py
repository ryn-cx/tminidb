# TODO: Validate
"""Contains the TvEpisode class."""

from __future__ import annotations

import json
from logging import NullHandler, getLogger

from tminidb.details.base import BaseDetails
from tminidb.details.tv_episode.models import TvEpisodeModel, model_validate_json
from tminidb.exceptions import (
    EpisodeNotFoundError,
    InvalidFileError,
    ResourceNotFoundError,
)

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class TvEpisode(BaseDetails[TvEpisodeModel]):
    """Manage the TV episode details file.

    Source: https://www.themoviedb.org/tv/{series_id}/season/{season_number}/episode/{episode_number}

    Example request:
        - GET /3/tv/{series_id}/season/{season_number}/episode/{episode_number}?
            - language=en-US
            - HTTP/2
        - Host: api.themoviedb.org
        - Accept: application/json
        - Authorization: Bearer __REDACTED__
    """

    MODEL = TvEpisodeModel
    LOAD = staticmethod(model_validate_json)

    # TODO: Validate
    def __call__(
        self,
        series_id: int,
        season_number: int,
        episode_number: int,
        *,
        append_to_response: str | None = None,
        language: str | None = None,
    ) -> TvEpisodeModel:
        """Look the TV episode up and return the model it is read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(
                series_id,
                season_number,
                episode_number,
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
        episode_number: int,
        *,
        append_to_response: str | None = None,
        language: str | None = None,
    ) -> str:
        """Download the TV episode details file.

        Raises:
            EpisodeNotFoundError: If the series has no such episode.
        """
        log_id = self.get_log_id(self.download, locals())
        try:
            response = self._download(
                f"tv/{series_id}/season/{season_number}/episode/{episode_number}",
                append_to_response=append_to_response,
                language=language,
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise EpisodeNotFoundError(
                series_id,
                season_number,
                episode_number,
                err.status_code,
                err.response,
            ) from err
        return self._validate_download(response, season_number, episode_number)

    # TODO: Validate
    @staticmethod
    def _validate_download(
        response: str,
        season_number: int,
        episode_number: int,
    ) -> str:
        # `id` is the episode's own id, so the season and episode numbers are
        # what say the file is the one that was asked for.
        parsed = json.loads(response)
        if parsed.get("season_number") != season_number:
            raise InvalidFileError(
                field="season number",
                expected=season_number,
                response=response,
            )
        if parsed.get("episode_number") != episode_number:
            raise InvalidFileError(
                field="episode number",
                expected=episode_number,
                response=response,
            )
        return response
