from unittest import TestCase
from bubble_sort import bubble_sort


class BubbleSortTest(TestCase):

    def test_orelse(self):
        self.assertEqual(bubble_sort(52, 46, 2, 7584, 542), [2.0, 46.0, 52.0, 542.0, 7584.0])