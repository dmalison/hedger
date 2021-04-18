import unittest

import marchmadness.entry as entry


class EntryTest(unittest.TestCase):
    def test_entry_repr(self):
        my_team = entry.Entry('my_team')
        self.assertEqual(repr(my_team), "Entry('my_team')")