#!/usr/bin/env python
"""Test cases for main.py."""
import unittest
import main
from fastapi import FastAPI


class TestMain(unittest.TestCase):
    """Define tests for main program."""

    def test_instance(self):
        """Test instance of app is FastAPI."""
        self.assertIsInstance(main.app, FastAPI)


if __name__ == "__main__":
    unittest.main()
