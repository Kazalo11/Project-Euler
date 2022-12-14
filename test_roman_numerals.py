from unittest import TestCase

from roman_numerals import roman_to_decimal, convert_roman

numerals = 'MCMXCIV'
number = 1904


class Test(TestCase):
    def test_roman_to_decimal(self):
        self.assertEqual(roman_to_decimal(numerals), 1994)


class Test(TestCase):
    def test_convert_roman(self):
        self.assertEqual(convert_roman(number),'MCMIV')
