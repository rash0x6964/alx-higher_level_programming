#!/usr/bin/python3
import unittest
from models.square import Square
from unittest.mock import patch
from io import StringIO

class testSquare(unittest.TestCase):

    def test_square_init(self):
        with self.assertRaises(TypeError):
            Square("2")
        with self.assertRaises(ValueError):
            r = Square(10)
            r.size = -10
        with self.assertRaises(TypeError):
            r = Square(10)
            r.size = {}
        with self.assertRaises(ValueError):
            Square(10, 2, -1)

    def test_area(self):
        r1 = Square(5)
        self.assertEqual(r1.area(), 25)
        r2 = Square(2, 2)
        self.assertEqual(r2.area(), 4)
        r3 = Square(3, 1, 3)
        self.assertEqual(r3.area(), 9)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display(self, stream):
        r1 = Square(5)
        r1.display()
        expected_output = "#####\n#####\n#####\n#####\n#####\n"
        self.assertEqual(stream.getvalue(), expected_output)

    def test_size_attribute(self):
        s1 = Square(5, 0, 0, 16)
        self.assertEqual(str(s1), "[Square] (16) 0/0 - 5")
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(str(s1), "[Square] (16) 0/0 - 10")
        with self.assertRaises(TypeError):
            s1.size = "9"
        with self.assertRaises(TypeError):
            Square(None)
        with self.assertRaises(ValueError):
            Square(-1)

    def test_update(self):
        r1 = Square(5, 0, 0, 19)
        self.assertEqual(str(r1), "[Square] (19) 0/0 - 5")
        r1.update(10)
        self.assertEqual(str(r1), "[Square] (10) 0/0 - 5")
        r1.update(1, 2)
        self.assertEqual(str(r1), "[Square] (1) 0/0 - 2")
        r1.update(1, 2, 3)
        self.assertEqual(str(r1), "[Square] (1) 3/0 - 2")
        r1.update(1, 2, 3, 4)
        self.assertEqual(str(r1), "[Square] (1) 3/4 - 2")
        r1.update(x=12)
        self.assertEqual(str(r1), "[Square] (1) 12/4 - 2")
        r1.update(size=7, y=1)
        self.assertEqual(str(r1), "[Square] (1) 12/1 - 7")
        r1.update(size=7, id=89, y=1)
        self.assertEqual(str(r1), "[Square] (89) 12/1 - 7")

    def test_to_dictionary(self):
        s1 = Square(10, 2, 1, 1)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, {'id': 1, 'x': 2, 'size': 10, 'y': 1})
        self.assertEqual(type(s1_dictionary), dict)
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        self.assertNotEqual(s1, s2)



if __name__ == "__main__":
    unittest.main()
