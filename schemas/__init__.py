#!/usr/bin/env python
"""Schema definitions for request body."""
from pydantic import BaseModel
from typing import Union


class Options(BaseModel):
    """Define options for an algorithm."""

    format: Union[str, None] = None


class Body(BaseModel):
    """Define body of request."""

    corpus: str
    options: Union[Options, None] = None
