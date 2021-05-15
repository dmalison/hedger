import unittest

from hedger import utils


class OsTest(unittest.TestCase):
    def test_write_and_remove_a_file(self):
        path = 'tests/data/test_remove.txt'
        self.assertFalse(utils.path_exists(path))

        file = open(path, 'w')
        file.write('foobar')
        file.close()
        self.assertTrue(utils.path_exists(path))

        utils.remove(path)
        self.assertFalse(utils.path_exists(path))
