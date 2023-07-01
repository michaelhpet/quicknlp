#!/usr/bin/env python
"""Model class for summarization algorithm."""
from models.base import Base


class Summarization(Base):
    """Define a summarization object.

    Attributes:
        corpus (str): A URL-safe string/text as input for the
        summarization algorithm
    """

    def __init__(self, corpus, **kwargs):
        """Initialize a summarization object."""
        super().__init__(corpus)
        for key in kwargs:
            setattr(self, key, kwargs[key])

    @classmethod
    def describe(cls):
        """Describe this Summarization class.

        Returns:
            dict: A dictionary representing metadata about the summarization
            algorithm
        """
        return {
            "name": cls.__name__,
            "description": "Text summarization is the problem of reducing "
            "number of sentences and words of a document without changing its "
            "meaning. There are different techniques to extract information "
            "from raw text data and use it for a summarization model, overall "
            "they can be categorized as Extractive and Abstractive."
        }
