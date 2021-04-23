import unittest

import marchmadness


class EntryTest(unittest.TestCase):
    def test_entry_repr_with_name(self):
        my_team = marchmadness.Entry('my_team')
        self.assertEqual(repr(my_team), "Entry('my_team')")

    def test_empty_entry_repr(self):
        empty_team = marchmadness.EmptyEntry()
        self.assertEqual(repr(empty_team), "EmptyEntry()")

    def test_two_entries_with_same_name_are_equal(self):
        my_team = marchmadness.Entry('my_team')
        my_team_duplicate = marchmadness.Entry('my_team')

        self.assertEqual(my_team, my_team_duplicate)

    def test_two_entries_with_different_names_are_not_equal(self):
        my_team = marchmadness.Entry('my_team')
        not_my_team = marchmadness.Entry('not_my_team')

        self.assertNotEqual(my_team, not_my_team)

    def test_empty_entry_equal_to_itself(self):
        empty_entry_0 = marchmadness.EmptyEntry()
        empty_entry_1 = marchmadness.EmptyEntry()

        self.assertEqual(empty_entry_0, empty_entry_1)

    def test_empty_entry_not_equal_to_entry_with_name(self):
        my_team = marchmadness.Entry('my_team')
        empty_entry = marchmadness.EmptyEntry()

        self.assertNotEqual(empty_entry, my_team)
        self.assertNotEqual(my_team, empty_entry)
