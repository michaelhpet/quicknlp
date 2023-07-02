#!/usr/bin/env python
"""Schema definitions for request body."""
from pydantic import BaseModel
from enum import Enum


class Formats(Enum):
    """Enumerate accepted output formats."""

    text = 1
    pdf = 2


class Options(BaseModel):
    """Define options for an algorithm."""

    # format: Formats | None = Formats.text
    sentences: int = 2


class Body(BaseModel):
    """Define body of request."""

    corpus: str
    options: Options | None = Options()

    class Config:
        """Define configurations for Body schema."""

        schema_extra = {
            "examples": [
                {
                    "corpus": "Hello World",
                    "options": {
                        "format": "text",
                        "sentences": 5
                    }
                }
            ]
        }
