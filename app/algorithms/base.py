#!/usr/bin/env python
"""Module for Base class definition."""


class Base():
    """Define the base characteristics of every algorithm object.

    Attributes:
        corpus (str): A URL-safe string/text as input for the
        summarization algorithm
    """

    def __init__(self, corpus):
        """Initialize a base object."""
        if corpus is None or not isinstance(corpus, str):
            raise ValueError("Corpus must be provided and must be a string")
        self.corpus = corpus
