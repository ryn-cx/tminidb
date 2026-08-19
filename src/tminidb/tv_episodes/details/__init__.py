# TODO: Validate
"""Query the details of a TV episode.

This method supports using `append_to_response`. Read more about this
[here](https://developer.themoviedb.org/docs/append-to-response).

[Official Documentation](https://developer.themoviedb.org/reference/tv-episode-details)
"""

from __future__ import annotations

from logging import NullHandler, getLogger

from tminidb.base_endpoint import BaseEndpoint, records_call
from tminidb.exceptions import InvalidFileError
from tminidb.tv_episodes.details.models import Details

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class TvEpisodeDetails(BaseEndpoint):
    """Query the details of a TV episode.

    This method supports using `append_to_response`. Read more about this
    [here](https://developer.themoviedb.org/docs/append-to-response).

    [Official Documentation](https://developer.themoviedb.org/reference/tv-episode-details)
    """

    # TODO: Validate
    @records_call
    def __call__(
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
        log_id = self.log_id()
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
        return Details.from_response(data)
