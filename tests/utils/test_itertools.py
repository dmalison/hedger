import unittest

from hedger import utils


class ItertoolsTest(unittest.TestCase):
    def test_all_pairs_on_a_string(self):
        expected = [('A', 'A'), ('A', 'B'), ('A', 'C'),
                    ('B', 'A'), ('B', 'B'), ('B', 'C'),
                    ('C', 'A'), ('C', 'B'), ('C', 'C')]
        actual = list(utils.all_pairs_product('ABC'))
        self.assertListEqual(expected, actual)

    def test_pairwise_grouper_on_a_string(self):
        actual = list(utils.pairwise_grouper('ABCDEFG', 'x'))
        expected = [('A', 'B'), ('C', 'D'), ('E', 'F'), ('G', 'x')]

        self.assertListEqual(actual, expected)
