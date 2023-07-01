#!/usr/bin/env python
"""Model class for paraphrasing algorithm."""
from models.base import Base


class Paraphrasing(Base):
    """Define a paraphrasing object.

    Attributes:
        corpus (str): A URL-safe string/text as input for the
        paraphrasing algorithm
    """

    def __init__(self, corpus, **kwargs):
        """Initialize a paraphrasing object."""
        super().__init__(corpus)
        for key in kwargs:
            setattr(self, key, kwargs[key])

    @classmethod
    def describe(cls):
        """Describe this paraphrasing class.

        Returns:
            dict: A dictionary representing metadata about the paraphrasing
            algorithm
        """
        return {
            "name": cls.__name__,
            "description": "Paraphrase generation is the task of generating "
            "an output sentence that preserves the meaning of the input "
            "sentence with variations in word choice and grammar. Two "
            "sentences are paraphrases if their meanings are equivalent "
            "but their words and syntax are different."
        }
