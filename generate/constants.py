# TODO: Validate
"""Constants."""

from pathlib import Path

FILES_PATH = Path(__file__).parent / "_files"
"""Where the recorded responses live."""

IDS_PATH = Path(__file__).parent / "ids"
"""Where the ids each model's responses are recorded for live."""

TMINIDB_PATH = Path(__file__).parent.parent / "src" / "tminidb"
"""The package the models are written into."""

ACCESS_TOKEN_CREDENTIAL = "TMDB_ACCESS_TOKEN"  # noqa: S105
"""The credential holding the TMDB API read access token."""
