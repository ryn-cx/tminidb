# TODO: Validate
"""Query the details of a TV season.

This method supports using `append_to_response`. Read more about this
[here](https://developer.themoviedb.org/docs/append-to-response).

[Official Documentation](https://developer.themoviedb.org/reference/tv-season-details)
"""

from __future__ import annotations

from logging import NullHandler, getLogger

from tminidb.base_endpoint import BaseEndpoint, records_call
from tminidb.exceptions import InvalidFileError
from tminidb.tv_seasons.details.models import TvSeason

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class TvSeasonDetails(BaseEndpoint):
    """Query the details of a TV season.

    This method supports using `append_to_response`. Read more about this
    [here](https://developer.themoviedb.org/docs/append-to-response).

    [Official Documentation](https://developer.themoviedb.org/reference/tv-season-details)
    """

    # TODO: Validate
    @records_call
    def __call__(
        self,
        series_id: int,
        season_number: int,
        *,
        append_to_response: str | None = None,
        language: str | None = None,
    ) -> TvSeason:
        """Query the details of a TV season.

        This method supports using `append_to_response`. Read more about this
        [here](https://developer.themoviedb.org/docs/append-to-response).

        [Official Documentation](https://developer.themoviedb.org/reference/tv-season-details)

        Raises:
            InvalidFileError: If the response is for a different season.
        """
        log_id = self.log_id()
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
        return TvSeason.from_response(data)
