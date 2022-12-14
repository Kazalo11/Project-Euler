from unittest import TestCase
from reversible_numbers import *


class Test(TestCase):
    def test_sum_reversible(self):
        self.assertEqual(sum_reversible(36), 99)

    def test_all_odd(self):
        self.assertTrue(all_odd((409)))

