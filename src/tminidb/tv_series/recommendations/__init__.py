# TODO: Validate
"""Get a list of recommended TV shows for a TV show.

Source: https://developer.themoviedb.org/reference/tv-series-recommendations
"""

from __future__ import annotations

from logging import NullHandler, getLogger

from tminidb.base_recommendations import BaseRecommendations
from tminidb.exceptions import ResourceNotFoundError, SeriesNotFoundError
from tminidb.tv_series.recommendations.models import (
    TvSeriesRecommendationsModel,
    model_validate_json,
)

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class TvSeriesRecommendations(BaseRecommendations[TvSeriesRecommendationsModel]):
    """Get a list of recommended TV shows for a TV show.

    Source: https://developer.themoviedb.org/reference/tv-series-recommendations
    """

    MODEL = TvSeriesRecommendationsModel
    LOAD = staticmethod(model_validate_json)

    # TODO: Validate
    def __call__(
        self,
        series_id: int,
        *,
        language: str | None = None,
        page: int = 1,
    ) -> TvSeriesRecommendationsModel:
        """Get a list of recommended TV shows for a TV show.

        Source: https://developer.themoviedb.org/reference/tv-series-recommendations
        """
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(series_id, language=language, page=page),
            log_id,
        )

    # TODO: Validate
    def download(
        self,
        series_id: int,
        *,
        language: str | None = None,
        page: int = 1,
    ) -> str:
        """Download one page of TV shows recommended for a TV show.

        Raises:
            SeriesNotFoundError: If no series is under that id.
        """
        log_id = self.get_log_id(self.download, locals())
        try:
            return self._download(
                f"tv/{series_id}/recommendations",
                language=language,
                page=page,
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise SeriesNotFoundError(series_id, err.status_code, err.response) from err
