import unittest

import marchmadness


class MatchTest(unittest.TestCase):
    def test_match_repr_with_entries(self):
        team_a = marchmadness.Entry('A')
        team_b = marchmadness.Entry('B')
        match = marchmadness.Match(
            round_=0,
            index=0,
            top=team_a,
            bottom=team_b
        )

        expected = \
            "Match(round_=0, index=0, top=Entry('A'), bottom=Entry('B'))"

        self.assertEqual(repr(match), expected)

    def test_match_repr_with_sub_matches(self):
        team_a = marchmadness.Entry('A')
        team_b = marchmadness.Entry('B')
        submatch_0 = marchmadness.Match(
            round_=0,
            index=0,
            top=team_a,
            bottom=team_b
        )

        team_c = marchmadness.Entry('C')
        team_d = marchmadness.Entry('D')
        submatch_1 = marchmadness.Match(
            round_=0,
            index=1,
            top=team_c,
            bottom=team_d
        )

        match = marchmadness.Match(
            round_=1,
            index=0,
            top=submatch_0,
            bottom=submatch_1
        )

        top_str = \
            "Match(round_=0, index=0, top=Entry('A'), bottom=Entry('B'))"
        bottom_str = \
            "Match(round_=0, index=1, top=Entry('C'), bottom=Entry('D'))"

        expected_fmt = "Match(round_=1, index=0, top={top}, bottom={bottom})"
        expected = expected_fmt.format(top=top_str, bottom=bottom_str)
        self.assertEqual(repr(match), expected)

    def test_matches_with_same_entries_are_equal(self):
        team_a = marchmadness.Entry('A')
        team_b = marchmadness.Entry('B')
        match = marchmadness.Match(
            round_=0,
            index=0,
            top=team_a,
            bottom=team_b
        )
        duplicate_match = marchmadness.Match(
            round_=0,
            index=0,
            top=team_a,
            bottom=team_b
        )
        self.assertEqual(match, duplicate_match)

    def test_matches_with_different_entries_are_not_equal(self):
        team_a = marchmadness.Entry('A')
        team_b = marchmadness.Entry('B')
        match = marchmadness.Match(
            round_=0,
            index=0,
            top=team_a,
            bottom=team_b
        )
        not_a_duplicate_match = marchmadness.Match(
            round_=0,
            index=0,
            top=team_b,
            bottom=team_a
        )
        self.assertNotEqual(match, not_a_duplicate_match)

    def test_matches_with_different_rounds_are_not_equal(self):
        team_a = marchmadness.Entry('A')
        team_b = marchmadness.Entry('B')
        match = marchmadness.Match(
            round_=0,
            index=0,
            top=team_a,
            bottom=team_b
        )
        not_a_duplicate_match = marchmadness.Match(
            round_=1,
            index=0,
            top=team_a,
            bottom=team_b
        )
        self.assertNotEqual(match, not_a_duplicate_match)

    def test_matches_with_different_indexes_are_not_equal(self):
        team_a = marchmadness.Entry('A')
        team_b = marchmadness.Entry('B')
        match = marchmadness.Match(
            round_=0,
            index=0,
            top=team_a,
            bottom=team_b
        )
        not_a_duplicate_match = marchmadness.Match(
            round_=0,
            index=1,
            top=team_a,
            bottom=team_b
        )
        self.assertNotEqual(match, not_a_duplicate_match)

    def test_matches_and_entries_are_not_equal(self):
        empty_entry = marchmadness.EmptyEntry()
        empty_match = marchmadness.Match(
            round_=0,
            index=0,
            top=empty_entry,
            bottom=empty_entry
        )
        self.assertNotEqual(empty_entry, empty_match)
        self.assertNotEqual(empty_match, empty_entry)
