# TODO: Validate
from __future__ import annotations

import json
from datetime import timedelta
from logging import NullHandler, getLogger
from typing import TYPE_CHECKING

from pydantic import BaseModel

from tminidb.base_api_endpoint import BaseEndpoint

if TYPE_CHECKING:
    from collections.abc import Callable
    from datetime import date

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class BaseChangesList[T: BaseModel](BaseEndpoint):
    MODEL: type[T]
    LOAD: Callable[[str | bytes | object, str], T]
    ENDPOINT: str

    # TODO: Validate
    def __call__(
        self,
        *,
        start_date: date | None = None,
        end_date: date | None = None,
        page: int = 1,
    ) -> T:
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(start_date=start_date, end_date=end_date, page=page),
            log_id,
        )

    # TODO: Validate
    def download(
        self,
        *,
        start_date: date | None = None,
        end_date: date | None = None,
        page: int = 1,
    ) -> str:
        log_id = self.get_log_id(self.download, locals())
        return self._client.download(
            type(self).ENDPOINT,
            params={
                "start_date": start_date.isoformat() if start_date else None,
                "end_date": end_date.isoformat() if end_date else None,
                "page": page,
            },
            log_id=log_id,
        )

    # TODO: Validate
    def download_all(self, start_date: date, end_date: date) -> list[str]:
        downloaded_pages: list[str] = []
        day = start_date
        while day <= end_date:
            page = 1
            while True:
                downloaded_page = self.download(start_date=day, end_date=day, page=page)
                downloaded_pages.append(downloaded_page)
                if page >= json.loads(downloaded_page)["total_pages"]:
                    break
                page += 1
            day += timedelta(days=1)
        return downloaded_pages

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> T:
        return type(self).LOAD(data, log_id or self.default_log_id)
