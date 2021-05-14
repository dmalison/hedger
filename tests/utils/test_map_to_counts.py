import unittest

from hedger import utils


class MapToCountsTest(unittest.TestCase):
    def test_increment_adds_and_updates_keys(self):
        count = utils.MapToCounts({'a': 1})
        count.increment('a')
        count.increment('b')

        self.assertDictEqual({'a': 2, 'b': 1}, dict(count))

    def test_value_error_raised_for_float_values(self):
        with self.assertRaises(ValueError):
            utils.MapToCounts({'a': 1, "b": 2.})

    def test_value_error_raised_for_str_values(self):
        with self.assertRaises(ValueError):
            utils.MapToCounts({'a': 1, "b": "2"})
