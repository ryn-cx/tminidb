"""Rebuilds Tminidb models."""

import logging

from good_ass_pydantic_integrator.utils import rebuild_models

import tminidb

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    rebuild_models(tminidb)
