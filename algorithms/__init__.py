#!/usr/bin/env python
"""Module for defining algorithms."""
from algorithms.paraphrasing import Paraphrasing
from algorithms.summarization import Summarization
from algorithms.grammar_checking import GrammarChecking


algorithms = [
            Paraphrasing.describe(),
            Summarization.describe(),
            GrammarChecking.describe()
        ]
