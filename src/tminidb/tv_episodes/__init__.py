from __future__ import annotations

from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any

from tminidb._changes import download_changes
from tminidb.base_endpoint import BaseEndpoint
from tminidb.exceptions import InvalidFileError
from tminidb.tv_episodes.models.changes import TvEpisodeChangeLog
from tminidb.tv_episodes.models.details import Details
from tminidb.tv_episodes.models.translations import Translations

if TYPE_CHECKING:
    from datetime import date

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class TvEpisodeEndpoints(BaseEndpoint):
    # TODO: Validate
    def changes(
        self,
        episode_id: int,
        *,
        start_date: date | None = None,
        end_date: date | None = None,
        page: int = 1,
    ) -> TvEpisodeChangeLog:
        """Get the recent changes for a TV episode.

        Get the changes for a TV episode. By default only the last 24 hours are
        returned.

        You can query up to 14 days in a single query by using the `start_date` and
        `end_date` query parameters.

        > 📘 Note
        >
        > TV episode changes are a little different than movie changes in that there
        > are some edits on episodes that will create a top level change entry at the
        > season level. These can be found under the episode keys. These keys will
        > contain a  `episode_id`. You can use the episode changes methods to look
        > these up individually.

        [Official Documentation](https://developer.themoviedb.org/reference/tv-episode-changes-by-id)

        If the query is more than 14 days multiple queries will be made and the results
        will be merged together.
        """
        log_id = self.get_log_id(self.changes, locals())

        # TODO: Validate
        def _download(start: str | None, end: str | None) -> dict[str, Any]:
            return self._client.download(
                f"tv/episode/{episode_id}/changes",
                {
                    "start_date": start,
                    "end_date": end,
                    "page": page,
                },
                log_id=log_id,
            )

        return self.load_changes(
            download_changes(start_date, end_date, _download),
        )

    # TODO: Validate
    def load_changes(self, data: dict[str, Any]) -> TvEpisodeChangeLog:
        """Read a response the changes endpoint answered with."""
        return TvEpisodeChangeLog.from_response(data)

    # TODO: Validate
    def details(
        self,
        series_id: int,
        season_number: int,
        episode_number: int,
        *,
        append_to_response: str | None = None,
        language: str | None = None,
    ) -> Details:
        """Query the details of a TV episode.

        This method supports using `append_to_response`. Read more about this
        [here](https://developer.themoviedb.org/docs/append-to-response).

        [Official Documentation](https://developer.themoviedb.org/reference/tv-episode-details)

        Raises:
            InvalidFileError: If the response is for a different episode.
        """
        log_id = self.get_log_id(self.details, locals())
        data = self._client.download(
            f"tv/{series_id}/season/{season_number}/episode/{episode_number}",
            {
                "append_to_response": append_to_response,
                "language": language or self._client.language,
            },
            log_id=log_id,
        )
        # `id` is the episode's own id, so the season and episode numbers are
        # what identify the file as the one that was asked for.
        if data.get("season_number") != season_number:
            raise InvalidFileError(
                field="season number",
                expected=season_number,
                response=data,
            )
        if data.get("episode_number") != episode_number:
            raise InvalidFileError(
                field="episode number",
                expected=episode_number,
                response=data,
            )
        return self.load_details(data)

    # TODO: Validate
    def load_details(self, data: dict[str, Any]) -> Details:
        """Read a response the details endpoint answered with."""
        return Details.from_response(data)

    # TODO: Validate
    def translations(
        self,
        series_id: int,
        season_number: int,
        episode_number: int,
    ) -> Translations:
        """Get the translations that have been added to a TV episode.

        Take a read through our
        [language](https://developer.themoviedb.org/docs/languages) documentation
        for more information about languages on TMDB.

        [Official Documentation](https://developer.themoviedb.org/reference/tv-episode-translations)
        """
        log_id = self.get_log_id(self.translations, locals())
        data = self._client.download(
            f"tv/{series_id}/season/{season_number}/episode/{episode_number}"
            "/translations",
            {},
            log_id=log_id,
        )
        return self.load_translations(data)

    # TODO: Validate
    def load_translations(self, data: dict[str, Any]) -> Translations:
        """Read a response the translations endpoint answered with."""
        return Translations.from_response(data)
