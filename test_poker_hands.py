from unittest import TestCase
from poker_hands import *

example_straight = ['8D', '7H', '6C', '5S', '4C']
royal_flush = ['AC', 'KC', 'QC', 'JC', 'TC']
straight_flush = ['QC', 'JC', 'TC', '9C', '8C']
full_house = ["AC", 'AD', 'AH', '9S', '9D']
normal_flush = ['AC', 'KC', 'TC', '9C', '8C']
four_kind = ["AC", 'AD', 'AH', 'AS', '9D']
three_kind = ["AC", 'AD', 'AH', '8S', '9D']
two_pair = ["AC", 'AD', '8H', '8S', '9D']
pair = ["AC", 'AD', '8H', '7S', '9D']
tie_pair = ["KC", 'KD', '8H', '7S', '9D']


class Test(TestCase):
    def test_flush(self):
        self.assertEqual(flush(royal_flush), 10)
        self.assertEqual(flush(straight_flush), 9)
        self.assertEqual(flush(normal_flush), 6)
        self.assertFalse(flush(example_straight))

    def test_straight(self):
        self.assertEqual(straight(example_straight),5)
        self.assertFalse(straight(normal_flush))

    def test_same_kind(self):
        self.assertEqual(same_kind(four_kind)[0], 8)
        self.assertEqual(same_kind(three_kind)[0], 4)
        self.assertEqual(same_kind(full_house)[0], 7)
        self.assertEqual(same_kind(two_pair)[0], 3)
        self.assertEqual(same_kind(pair)[0], 2)
        self.assertEqual(same_kind(example_straight)[0],0)


    def test_player_1_tie(self):
        self.assertTrue(player_1_tie(pair, tie_pair))
