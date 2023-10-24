import unittest
from isTriangle import Triangle
# import sys
# sys.path.append("..")
# from src.Triangle import Triangle

class DecisionCoverageTest(unittest.TestCase):

    def test1(self):
        actual = Triangle.classify(10, 10, 10)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

    def test2(self):
        actual = Triangle.classify(1, 0, 0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

        actual = Triangle.classify(1, 2, 3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

        actual = Triangle.classify(1, 1, 3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test3(self):
        actual = Triangle.classify(2, 3, 4)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)

        actual = Triangle.classify(2, 3, 3)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

        actual = Triangle.classify(3, 2, 3)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

        actual = Triangle.classify(3, 3, 2)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
