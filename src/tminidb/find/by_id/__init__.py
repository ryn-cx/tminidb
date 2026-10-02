# TODO: Validate
"""Find data by one of the external sources TMDB keeps ids for.

Source: https://developer.themoviedb.org/reference/find-by-id
"""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Literal

from tminidb.base_api_endpoint import BaseEndpoint
from tminidb.find.by_id.models import FindByIdModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())

type ExternalSource = Literal[
    "imdb_id",
    "facebook_id",
    "instagram_id",
    "tvdb_id",
    "tiktok_id",
    "twitter_id",
    "wikidata_id",
    "youtube_id",
]
"""The external sources TMDB can find an id from."""


# TODO: Validate
class FindById(BaseEndpoint):
    """Find data by one of the external sources TMDB keeps ids for.

    An id TMDB does not know returns every result list empty.

    Source: https://developer.themoviedb.org/reference/find-by-id
    """

    # TODO: Validate
    def __call__(
        self,
        external_id: str,
        external_source: ExternalSource,
        *,
        language: str | None = None,
    ) -> FindByIdModel:
        """Find data by one of the external sources TMDB keeps ids for.

        Source: https://developer.themoviedb.org/reference/find-by-id
        """
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(external_id, external_source, language=language),
            log_id,
        )

    # TODO: Validate
    def download(
        self,
        external_id: str,
        external_source: ExternalSource,
        *,
        language: str | None = None,
    ) -> str:
        """Download the find by id file."""
        log_id = self.get_log_id(self.download, locals())
        return self._client.download(
            f"find/{external_id}",
            params={
                "external_source": external_source,
                "language": language or self._client.language,
            },
            log_id=log_id,
        )

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> FindByIdModel:
        """Load a find by id file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)
