import unittest

import marchmadness.entry as entry


class EntryTest(unittest.TestCase):
    def test_entry_repr_with_name(self):
        my_team = entry.Entry('my_team')
        self.assertEqual(repr(my_team), "Entry('my_team')")

    def test_entry_repr_with_no_name(self):
        empty_team = entry.EmptyEntry()
        self.assertEqual(repr(empty_team), "EmptyEntry()")
