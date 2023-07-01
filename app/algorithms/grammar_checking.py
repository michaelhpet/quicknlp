#!/usr/bin/env python
"""Model class for grammar checking algorithm."""
from app.algorithms.base import Base


class GrammarChecking(Base):
    """Define a grammar checking object.

    Attributes:
        corpus (str): A URL-safe string/text as input for the
        grammar checking algorithm
    """

    def __init__(self, corpus, **options):
        """Initialize a grammar checking object."""
        super().__init__(corpus)
        for key in options:
            setattr(self, key, options[key])

    @classmethod
    def describe(cls):
        """Describe this grammar checking class.

        Returns:
            dict: A dictionary representing metadata about the grammar checking
            algorithm
        """
        return {
            "name": "Grammar checking",
            "description": "Grammar checking is one of the most widely used "
            "tools within natural language processing (NLP) applications. "
            "Grammar checkers check the grammatical structure of sentences "
            "based on morphological processing and syntactic processing."
        }
