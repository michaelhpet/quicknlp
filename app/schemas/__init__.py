#!/usr/bin/env python
"""Schema definitions for request body."""
from pydantic import BaseModel


class Options(BaseModel):
    """Define options for an algorithm."""

    format: str | None = None


class Body(BaseModel):
    """Define body of request."""

    corpus: str
    options: Options | None = Options()

    class Config:
        """Define configurations for Body schema."""

        schema_extra = {
            "examples": [
                {
                    "corpus": "Hello World"
                }
            ]
        }
