#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO


class testRectangle(unittest.TestCase):

    def test_rectangle_init(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.width = -10
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = {}
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)

    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display(self, stream):
        r1 = Rectangle(4, 6)
        r1.display()
        expected_output = "####\n####\n####\n####\n####\n####\n"
        self.assertEqual(stream.getvalue(), expected_output)

    def test___str__(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), "[Rectangle] (4) 1/0 - 5/5")

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_positions(self, stream):
        r1 = Rectangle(2, 3, 2, 2)
        r1.display()
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(stream.getvalue(), expected_output)

    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (11) 10/10 - 10/10")
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")
        r1.update(height=1)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/1")
        r1.update(width=1, x=2)
        self.assertEqual(str(r1), "[Rectangle] (89) 2/5 - 1/1")
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/1")
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")

if __name__ == "__main__":
    unittest.main()
