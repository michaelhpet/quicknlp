#!/usr/bin/env python
"""Model class for summarization algorithm."""
from app.algorithms.base import Base


class Summarization(Base):
    """Define a summarization object.

    Attributes:
        corpus (str): A URL-safe string/text as input for the
        summarization algorithm
    """

    def __init__(self, corpus, **options):
        """Initialize a summarization object."""
        super().__init__(corpus)
        self.summary = ""
        if options:
            for key in options:
                setattr(self, key, options[key])

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

    def summarize(self):
        """Summarize the corpus of a Summarization instance."""
        return None
