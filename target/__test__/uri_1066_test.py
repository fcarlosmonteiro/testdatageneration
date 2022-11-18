from unittest import TestCase
from target.uri_1066 import func


class URI1066Test(TestCase):

    def test_func(self):
        self.assertEqual(func(-5, 0, -3, -4, 12), '3 valor(es) par(es), 2 valor(es) impar(es), 1 valor(es) positivo(s) e 3 valor(es) negativo(s)')