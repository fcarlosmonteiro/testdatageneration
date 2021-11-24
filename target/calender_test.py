from unittest import TestCase
from calender import find_day_string


class CalenderTest(TestCase):

    def test_calender(self):
        self.assertEqual(find_day_string(2019, 1, 1), 'Tuesday')
