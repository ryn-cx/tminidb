# TODO: Validate
"""Get the translations that have been added to a TV series.

Source: https://developer.themoviedb.org/reference/tv-series-translations
"""

from __future__ import annotations

from logging import NullHandler, getLogger

from tminidb.base_api_endpoint import BaseEndpoint
from tminidb.exceptions import ResourceNotFoundError, SeriesNotFoundError
from tminidb.tv_series.translations.models import (
    TvSeriesTranslationsModel,
    model_validate_json,
)

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class TvSeriesTranslations(BaseEndpoint):
    """Get the translations that have been added to a TV series.

    Take a read through TMDB's language documentation for more information about
    languages on TMDB: https://developer.themoviedb.org/docs/languages

    Source: https://developer.themoviedb.org/reference/tv-series-translations
    """

    # TODO: Validate
    def __call__(self, series_id: int) -> TvSeriesTranslationsModel:
        """Get the translations that have been added to a TV series.

        Source: https://developer.themoviedb.org/reference/tv-series-translations
        """
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(series_id), log_id)

    # TODO: Validate
    def download(self, series_id: int) -> str:
        """Download the TV series translations file.

        Raises:
            SeriesNotFoundError: If no series is under that id.
        """
        log_id = self.get_log_id(self.download, locals())
        try:
            return self._client.download(
                f"tv/{series_id}/translations",
                params={},
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise SeriesNotFoundError(
                series_id,
                err.status_code,
                err.response,
            ) from err

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> TvSeriesTranslationsModel:
        """Read a downloaded TV series translations file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)
