from unittest import TestCase
from target.orelse import func1


class OrelseTest(TestCase):

    def test_orelse(self):
        self.assertEqual(func1(15, 5, 15), (15, 15, 15))
