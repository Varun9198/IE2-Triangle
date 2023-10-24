import unittest
from isTriangle import Triangle
# import sys
# sys.path.append("..")
# from src.Triangle import Triangle

class TriangleTest(unittest.TestCase):

    def test1(self):
        actual = Triangle.classify(10, 10, 10)
        expected = Triangle.Type(2)
        self.assertEqual(actual, expected)

    def test2(self):
        actual = Triangle.classify(-1, -1, -1)
        expected = Triangle.Type(0)
        self.assertEqual(actual, expected)

        actual = Triangle.classify(-1, -1, -1)
        expected = Triangle.Type(0)
        self.assertEqual(actual, expected)

        actual = Triangle.classify(-1, 1, 1)
        expected = Triangle.Type(0)
        self.assertEqual(actual, expected)

        actual = Triangle.classify(1, 1, 0)
        expected = Triangle.Type(0)
        self.assertEqual(actual, expected)

        actual = Triangle.classify(1, 0, 1)
        expected = Triangle.Type(0)
        self.assertEqual(actual, expected)

        actual = Triangle.classify(1, 1, 1)
        expected = Triangle.Type(2)
        self.assertEqual(actual, expected)

        actual = Triangle.classify(0, 1, 1)
        expected = Triangle.Type(0)
        self.assertEqual(actual, expected)

        actual = Triangle.classify(1, 3, 4)
        expected = Triangle.Type(0)
        self.assertEqual(actual, expected)

        actual = Triangle.classify(4, 3, 1)
        expected = Triangle.Type(0)
        self.assertEqual(actual, expected)

        actual = Triangle.classify(1, 4, 3)
        expected = Triangle.Type(0)
        self.assertEqual(actual, expected)



        actual = Triangle.classify(1, 2, 3)
        expected = Triangle.Type(0)
        self.assertEqual(actual, expected)

        actual = Triangle.classify(1, 1, 3)
        expected = Triangle.Type(0)
        self.assertEqual(actual, expected)

    def test3(self):
        actual = Triangle.classify(2, 3, 4)
        expected = Triangle.Type(1)
        self.assertEqual(actual, expected)

        actual = Triangle.classify(2, 3, 3)
        expected = Triangle.Type(3)
        self.assertEqual(actual, expected)

        actual = Triangle.classify(3, 2, 3)
        expected = Triangle.Type(3)
        self.assertEqual(actual, expected)

        actual = Triangle.classify(3, 3, 2)
        expected = Triangle.Type(3)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
