from unittest import TestCase
from target.uri_1048 import func


class URI1048Test(TestCase):

    def test_func(self):
        self.assertEqual(func(400.00), 'Novo salario: 460.00\nReajuste ganho: 60.00\nEm percentual: 15 %')