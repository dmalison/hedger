import unittest

import marchmadness.utils as utils


class UtilsTest(unittest.TestCase):
    def test_grouper_on_collection_of_letters(self):
        actual = list(utils.grouper('ABCDEFG', 3, 'x'))
        expected = [('A', 'B', 'C'), ('D', 'E', 'F'), ('G', 'x', 'x')]

        self.assertListEqual(actual, expected)
