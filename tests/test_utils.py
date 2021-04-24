import unittest

from hedger import utils


class UtilsTest(unittest.TestCase):
    def test_pairwise_grouper_on_a_string(self):
        actual = list(utils.pairwise_grouper('ABCDEFG', 'x'))
        expected = [('A', 'B'), ('C', 'D'), ('E', 'F'), ('G', 'x')]

        self.assertListEqual(actual, expected)
