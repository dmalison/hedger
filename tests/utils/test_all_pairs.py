import unittest

from hedger import utils


class AllPairsTest(unittest.TestCase):
    def test_all_pairs_on_a_string(self):
        expected = [('A', 'A'), ('A', 'B'), ('A', 'C'),
                    ('B', 'A'), ('B', 'B'), ('B', 'C'),
                    ('C', 'A'), ('C', 'B'), ('C', 'C')]
        actual = list(utils.all_pairs('ABC'))
        self.assertListEqual(expected, actual)
