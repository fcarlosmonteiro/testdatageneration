from unittest import TestCase
from target.triangle import triangle


class TriangleTest(TestCase):

    def test_triangle(self):
        self.assertEqual(triangle(5, 5, 5), True)
