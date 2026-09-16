# TODO: Validate
"""Get the similar TV shows.

Source: https://developer.themoviedb.org/reference/tv-series-similar
"""

from __future__ import annotations

from logging import NullHandler, getLogger

from tminidb.base_similar import BaseSimilar
from tminidb.exceptions import ResourceNotFoundError, SeriesNotFoundError
from tminidb.tv_series.similar.models import TvSeriesSimilarModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class TvSeriesSimilar(BaseSimilar[TvSeriesSimilarModel]):
    """Get the similar TV shows.

    Source: https://developer.themoviedb.org/reference/tv-series-similar
    """

    MODEL = TvSeriesSimilarModel
    LOAD = staticmethod(model_validate_json)

    # TODO: Validate
    def __call__(
        self,
        series_id: int,
        *,
        language: str | None = None,
        page: int = 1,
    ) -> TvSeriesSimilarModel:
        """Get the similar TV shows.

        Source: https://developer.themoviedb.org/reference/tv-series-similar
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
        """Download one page of TV shows similar to a TV show.

        Raises:
            SeriesNotFoundError: If no series is under that id.
        """
        log_id = self.get_log_id(self.download, locals())
        try:
            return self._download(
                f"tv/{series_id}/similar",
                language=language,
                page=page,
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise SeriesNotFoundError(series_id, err.status_code, err.response) from err
