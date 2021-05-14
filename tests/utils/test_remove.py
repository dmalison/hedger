import unittest

from hedger import utils


class RemoveTest(unittest.TestCase):
    def test_write_and_remove_a_file(self):
        filepath = 'tests/data/test_remove.txt'
        self.assertFalse(utils.path_exists(filepath))

        file = open(filepath, 'w')
        file.write('foobar')
        file.close()
        self.assertTrue(utils.path_exists(filepath))

        utils.remove(filepath)
        self.assertFalse(utils.path_exists(filepath))
