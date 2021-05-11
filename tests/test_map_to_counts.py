import unittest

from hedger import utils


class MapToCountsTest(unittest.TestCase):
    def test_increment_count_dict_adds_and_updates_keys(self):
        count = utils.MapToCounts()
        count.increment('a')
        count.increment('b', 2)
        count.increment('b')

        self.assertDictEqual({'a': 1, 'b': 3}, count._dict)
