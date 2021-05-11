import unittest

from tests import utils as tests_utils


class RemoveTest(unittest.TestCase):
    def test_write_and_remove_a_file(self):
        filepath = 'tests/data/test_remove.txt'
        self.assertFalse(tests_utils.path_exists(filepath))

        file = open(filepath, 'w')
        file.write('foobar')
        file.close()
        self.assertTrue(tests_utils.path_exists(filepath))

        tests_utils.remove(filepath)
        self.assertFalse(tests_utils.path_exists(filepath))
