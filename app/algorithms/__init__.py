#!/usr/bin/env python
"""Module for defining algorithms."""
from app.algorithms.paraphrasing import Paraphrasing
from app.algorithms.summarization import Summarization
from app.algorithms.grammar_checking import GrammarChecking


algorithms = [
            Paraphrasing.describe(),
            Summarization.describe(),
            GrammarChecking.describe()
        ]
