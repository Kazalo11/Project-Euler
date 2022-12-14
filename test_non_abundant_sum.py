from unittest import TestCase

from non_abundant_sum import divisors,abundant

number = 12


class Test(TestCase):
    def test_divisors(self):
        self.assertEqual(divisors(number), 16)

    def test_abundant(self):
        self.assertTrue(abundant(number))
