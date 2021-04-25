import unittest

from hedger import utils


class UtilsTest(unittest.TestCase):
    def test_pairwise_grouper_on_a_string(self):
        actual = list(utils.pairwise_grouper('ABCDEFG', 'x'))
        expected = [('A', 'B'), ('C', 'D'), ('E', 'F'), ('G', 'x')]

        self.assertListEqual(actual, expected)

    def test_increment_count_dict_adds_and_updates_keys(self):
        count = utils.MapToCounts()
        count.increment('a')
        count.increment('b', 2)
        count.increment('b')

        self.assertDictEqual({'a': 1, 'b': 3}, count._dict)
