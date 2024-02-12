#!/usr/bin/python3
import unittest
from models.base import Base


class testBase(unittest.TestCase):

    def test_base_init(slef):
        b1 = Base()
        slef.assertEqual(b1.id, 1)
        b2 = Base()
        slef.assertEqual(b2.id, 2)
        b3 = Base(12)
        slef.assertEqual(b3.id, 12)
        b4 = Base()
        slef.assertEqual(b4.id, 3)

    def test_to_json_string(self):
        pass

if __name__ == "__main__":
    unittest.main()
