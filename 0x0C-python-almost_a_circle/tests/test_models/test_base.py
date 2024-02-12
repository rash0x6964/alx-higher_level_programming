#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

import os


class testBase(unittest.TestCase):

    # def setUp(self):
    #     print(os.getcwd())
    #     file_path = "Rectangle.json"
    #     if os.path.exists(file_path):
    #         os.remove(file_path)

    def tearDown(self):
        files_path = ["Rectangle.json", "Square.json"]
        for file in files_path:
            if os.path.exists(file):
                os.remove(file)

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

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 1)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), '[{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}, {"x": 0, "y": 0, "id": 1, "height": 4, "width": 2}]')

    def test_from_json_string(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, [{'height': 4, 'width': 10, 'id': 89}, {'height': 7, 'width': 1, 'id': 7}])
        self.assertEqual(type(list_input), list)
        self.assertEqual(json_list_input, '[{"id": 89, "width": 10, "height": 4}, {"id": 7, "width": 1, "height": 7}]')
        self.assertEqual(type(json_list_input), str)
        self.assertEqual(list_output, [{'height': 4, 'width': 10, 'id': 89}, {'height': 7, 'width': 1, 'id': 7}])
        self.assertEqual(type(list_output), list)

    def test_create(self):
        r1 = Rectangle(3, 5, 1, 0, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), "[Rectangle] (1) 1/0 - 3/5")
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 3/5")
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_load_from_file(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(list_rectangles_output, [])

        Rectangle.save_to_file([r1])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(list_rectangles_output[0]), "[Rectangle] (1) 2/8 - 10/7")

        s1 = Square(5, 0, 0, 1)
        Square.save_to_file([s1])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(list_squares_output[0]), "[Square] (1) 0/0 - 5")


if __name__ == "__main__":
    unittest.main()
