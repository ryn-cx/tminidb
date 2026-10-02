from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from datetime import date
from pydantic import BaseModel


class Result(BaseModel):
    model_config = ConfigDict(defer_build=True)
    adult: bool
    backdrop_path: str | None
    id: int
    title: str
    original_title: str
    overview: str
    poster_path: str
    media_type: str
    original_language: str
    genre_ids: list[int]
    popularity: float
    release_date: date
    softcore: bool
    video: bool
    vote_average: float
    vote_count: int


class MovieRecommendationsModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    page: int
    results: list[Result]
    total_pages: int
    total_results: int
    _raw_input: Any = PrivateAttr(default=None)

    @model_validator(mode="wrap")
    @classmethod
    def _capture_raw_input(
        cls, data: Any, handler: ModelWrapValidatorHandler[Self]
    ) -> Self:
        """Validate the model and keep the input it was built from."""
        model = handler(data)
        model._raw_input = data
        return model

    @property
    def raw_input(self) -> Any:
        """The input this model was validated from, as it was handed over."""
        return self._raw_input
