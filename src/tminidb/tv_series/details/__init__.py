# TODO: Validate
"""Get the details of a TV show.

## Append To Response

This method supports using `append_to_response`. Read more about this
[here](https://developer.themoviedb.org/docs/append-to-response).

[Official Documentation](https://developer.themoviedb.org/reference/tv-series-details)
"""

from __future__ import annotations

from logging import NullHandler, getLogger

from tminidb.base_endpoint import BaseEndpoint, records_call
from tminidb.exceptions import InvalidFileError
from tminidb.tv_series.details.models import TvSeries

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class TvSeriesDetails(BaseEndpoint):
    """Get the details of a TV show.

    ## Append To Response

    This method supports using `append_to_response`. Read more about this
    [here](https://developer.themoviedb.org/docs/append-to-response).

    [Official Documentation](https://developer.themoviedb.org/reference/tv-series-details)
    """

    # TODO: Validate
    @records_call
    def __call__(
        self,
        series_id: int,
        *,
        append_to_response: str | None = None,
        language: str | None = None,
    ) -> TvSeries:
        """Get the details of a TV show.

        ## Append To Response

        This method supports using `append_to_response`. Read more about this
        [here](https://developer.themoviedb.org/docs/append-to-response).

        [Official Documentation](https://developer.themoviedb.org/reference/tv-series-details)

        Raises:
            InvalidFileError: If the response is for a different series.
        """
        log_id = self.log_id()
        data = self._client.download(
            f"tv/{series_id}",
            {
                "append_to_response": append_to_response,
                "language": language or self._client.language,
            },
            log_id=log_id,
        )
        if data.get("id") != series_id:
            raise InvalidFileError(field="series id", expected=series_id, response=data)
        return TvSeries.from_response(data)
