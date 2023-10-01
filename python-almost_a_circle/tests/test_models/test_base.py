#!/usr/bin/python3

import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_module_docstring(self):
        self.assertTrue(len(__import__("modules").base.__doc__) > 0)

    def test_class_docstring(self):
        self.assertTrue(len(__import__("modules").base.Base.__doc__))

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
