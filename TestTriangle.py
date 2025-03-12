import unittest
import Triangle as Triangle


class TestTriangleClassification(unittest.TestCase):
    def test_equilateral(self):
        self.assertEqual(Triangle.classify_triangle(5, 5, 5), "equilateral")
        self.assertEqual(Triangle.classify_triangle(10, 10, 10), "equilateral")
    def test_isoc(self):
        self.assertEqual(Triangle.classify_triangle(2,2,3), "isosceles")
        self.assertEqual(Triangle.classify_triangle(4, 4, 6), "isosceles")
        self.assertEqual(Triangle.classify_triangle(2, 3, 2), "isosceles")
    def test_scalene(self):
        self.assertEqual(Triangle.classify_triangle(7, 8, 9), "scalene")
        self.assertEqual(Triangle.classify_triangle(3, 4, 6), "scalene")
    def test_right_triangle(self):
        self.assertEqual(Triangle.classify_triangle(3, 4, 5), "scalene right triangle")
        self.assertEqual(Triangle.classify_triangle(5, 12, 13), "scalene right triangle")
        self.assertEqual(Triangle.classify_triangle(8, 15, 17), "scalene right triangle")
        self.assertEqual(Triangle.classify_triangle(7, 24, 25), "scalene right triangle")
    def test_isosceles_right_triangle(self):
        self.assertEqual(Triangle.classify_triangle(1, 1, 2**0.5), "isosceles right triangle")
        self.assertEqual(Triangle.classify_triangle(2, 2, (2*(2**0.5))), "isosceles right triangle")
    def test_invalid_triangles(self):
        self.assertEqual(Triangle.classify_triangle(-1, 2, 3), "Not a valid triangle")
        self.assertEqual(Triangle.classify_triangle(0, 4, 4), "Not a valid triangle")
        self.assertEqual(Triangle.classify_triangle(1, 2, 3), "Not a valid triangle")
        self.assertEqual(Triangle.classify_triangle(2, 3, 5), "Not a valid triangle")
        self.assertEqual(Triangle.classify_triangle(1, 10, 100), "Not a valid triangle")

if __name__ == '__main__':
    unittest.main()
