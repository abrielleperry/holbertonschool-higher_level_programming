#!/usr/bin/python3

import unittest
from models.base import Base
import pycodestyle


class TestBase(unittest.TestCase):

    def test_module_docstring(self):
        self.assertTrue(len(__import__("models").base.__doc__) > 0)

    def test_class_docstring(self):
        self.assertTrue(len(__import__("models").base.Base.__doc__))

    def test_isinstance(self):
        b2 = Base()
        self.assertIsInstance(b2, Base)

    def test_no_input(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id - b1.id, 1)

    def test_input_with_id(self):
        b3 = Base(12)
        self.assertEqual(b3.id, 12)

    def test_pycodestyle(self):
        style = pycodestyle.StyleGuide(quiet=True)
        checkPyC = style.check_files(["models/base.py"])
        self.assertEqual(checkPyC.total_errors, 0, "Found code style errors (and warnings)")
