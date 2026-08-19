# TODO: Validate
"""Get the top level details of a movie by ID.

## Append To Response

This method supports using `append_to_response`. Read more about this
[here](https://developer.themoviedb.org/docs/append-to-response).

[Official Documentation](https://developer.themoviedb.org/reference/movie-details)
"""

from __future__ import annotations

from logging import NullHandler, getLogger

from tminidb.base_endpoint import BaseEndpoint, records_call
from tminidb.exceptions import InvalidFileError
from tminidb.movies.details.models import Movie

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class MovieDetails(BaseEndpoint):
    """Get the top level details of a movie by ID.

    ## Append To Response

    This method supports using `append_to_response`. Read more about this
    [here](https://developer.themoviedb.org/docs/append-to-response).

    [Official Documentation](https://developer.themoviedb.org/reference/movie-details)
    """

    # TODO: Validate
    @records_call
    def __call__(
        self,
        movie_id: int,
        *,
        append_to_response: str | None = None,
        language: str | None = None,
    ) -> Movie:
        """Get the top level details of a movie by ID.

        ## Append To Response

        This method supports using `append_to_response`. Read more about this
        [here](https://developer.themoviedb.org/docs/append-to-response).

        [Official Documentation](https://developer.themoviedb.org/reference/movie-details)

        Raises:
            InvalidFileError: If the response is for a different movie.
        """
        log_id = self.log_id()
        data = self._client.download(
            f"movie/{movie_id}",
            {
                "append_to_response": append_to_response,
                "language": language or self._client.language,
            },
            log_id=log_id,
        )
        if data.get("id") != movie_id:
            raise InvalidFileError(field="movie id", expected=movie_id, response=data)
        return Movie.from_response(data)
