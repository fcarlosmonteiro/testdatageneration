from unittest import TestCase
from target.uri_1040 import func


class URI1040Test(TestCase):

    def test_func(self):
        self.assertEqual(func(2.0, 4.0, 7.5, 8.0, 6.4), 'Media: 5.4\nAluno em exame.\nNota do exame: 6.4\nAluno aprovado.\nMedia final: 5.9')