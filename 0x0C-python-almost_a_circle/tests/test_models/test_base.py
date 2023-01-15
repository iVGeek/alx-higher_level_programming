#!/usr/bin/python3
"""Module for unit test"""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def id(self):
        u = Base(id=15)
        self.assertEqual(u.id,15)

if __name__ == '__main__':
    unittest.main()
