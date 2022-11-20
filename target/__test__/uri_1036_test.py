from unittest import TestCase
from target.uri_1036 import func


class URI1036Test(TestCase):

    def test_func(self):
        self.assertEqual(func(0.0, 20.0, 5.0), 'Impossivel calcular')