#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle


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
        r1 = Rectangle(10, 7, 2, 8, 1)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(dictionary, {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8})
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(json_dictionary, '[{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}]')
        self.assertEqual(type(json_dictionary), str)

if __name__ == "__main__":
    unittest.main()
