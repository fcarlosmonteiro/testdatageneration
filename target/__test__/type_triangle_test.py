from unittest import TestCase
from target.type_triangle import type_triangle


class TypeTriangleTest(TestCase):

    def test_type_triangle(self):
        self.assertEqual(type_triangle(2, 2, 5), 'isosceles triangle')
