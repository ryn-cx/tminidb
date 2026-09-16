# TODO: Validate
"""Constants."""

from pathlib import Path

from good_ass_pydantic_integrator.recordings import GeneratorPaths

GENERATOR_PATHS = GeneratorPaths(
    files_path=Path(__file__).parent / "_files",
    ids_path=Path(__file__).parent / "ids",
    package_path=Path(__file__).parent.parent / "src" / "",
)
"""Where the recordings, the ids they came from, and the models live."""

ACCESS_TOKEN_CREDENTIAL = "TMDB_ACCESS_TOKEN"  # noqa: S105
"""The credential holding the TMDB API read access token."""
