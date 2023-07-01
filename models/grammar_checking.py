#!/usr/bin/env python
"""Model class for grammar checking algorithm."""
from models.base import Base


class GrammarChecking(Base):
    """Define a grammar checking object.

    Attributes:
        corpus (str): A URL-safe string/text as input for the
        grammar checking algorithm
    """

    def __init__(self, corpus, **kwargs):
        """Initialize a grammar checking object."""
        super().__init__(corpus)
        for key in kwargs:
            setattr(self, key, kwargs[key])

    @classmethod
    def describe(cls):
        """Describe this grammar checking class.

        Returns:
            dict: A dictionary representing metadata about the grammar checking
            algorithm
        """
        return {
            "name": "Grammar checking",
            "description": "Paraphrase generation is the task of generating "
            "an output sentence that preserves the meaning of the input "
            "sentence with variations in word choice and grammar. Two "
            "sentences are paraphrases if their meanings are equivalent "
            "but their words and syntax are different."
        }
