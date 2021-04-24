import unittest

import marchmadness
from marchmadness.result import Result


class MatchTest(unittest.TestCase):
    def test_match_with_entries(self):
        team_a = marchmadness.Entry('A')
        team_b = marchmadness.Entry('B')
        match = marchmadness.Match(
            round_=0,
            index=0,
            top=team_a,
            bottom=team_b,
            result=Result.TOP_WINS
        )

        expected = (
            "Match(round_=0, index=0, top=Entry('A'), "
            "bottom=Entry('B'), result=Result.TOP_WINS)"
        )

        self.assertEqual(repr(match), expected)
        self.assertEqual(match.winner, team_a)

    def test_match_with_sub_matches(self):
        team_a = marchmadness.Entry('A')
        team_b = marchmadness.Entry('B')
        submatch_0 = marchmadness.Match(
            round_=0,
            index=0,
            top=team_a,
            bottom=team_b,
            result=Result.TOP_WINS
        )

        team_c = marchmadness.Entry('C')
        team_d = marchmadness.Entry('D')
        submatch_1 = marchmadness.Match(
            round_=0,
            index=1,
            top=team_c,
            bottom=team_d,
            result=Result.BOTTOM_WINS
        )

        match = marchmadness.Match(
            round_=1,
            index=0,
            top=submatch_0,
            bottom=submatch_1,
            result=Result.BOTTOM_WINS
        )

        top_str = (
            "Match(round_=0, index=0, top=Entry('A'), "
            "bottom=Entry('B'), result=Result.TOP_WINS)"
        )
        bottom_str = (
            "Match(round_=0, index=1, top=Entry('C'), "
            "bottom=Entry('D'), result=Result.BOTTOM_WINS)"
        )
        expected_fmt = (
            "Match(round_=1, index=0, top={top}, "
            "bottom={bottom}, result=Result.BOTTOM_WINS)"
        )
        expected = expected_fmt.format(top=top_str, bottom=bottom_str)

        self.assertEqual(repr(match), expected)
        self.assertEqual(match.winner, team_d)

    def test_matches_with_same_entries_are_equal(self):
        team_a = marchmadness.Entry('A')
        team_b = marchmadness.Entry('B')
        match = marchmadness.Match(
            round_=0,
            index=0,
            top=team_a,
            bottom=team_b,
            result=Result.TOP_WINS
        )
        duplicate_match = marchmadness.Match(
            round_=0,
            index=0,
            top=team_a,
            bottom=team_b,
            result=Result.TOP_WINS
        )
        self.assertEqual(match, duplicate_match)

    def test_matches_with_different_entries_are_not_equal(self):
        team_a = marchmadness.Entry('A')
        team_b = marchmadness.Entry('B')
        match = marchmadness.Match(
            round_=0,
            index=0,
            top=team_a,
            bottom=team_b,
            result=Result.TOP_WINS
        )
        top_and_bottom_reveresed_match = marchmadness.Match(
            round_=0,
            index=0,
            top=team_b,
            bottom=team_a,
            result=Result.TOP_WINS
        )
        self.assertNotEqual(match, top_and_bottom_reveresed_match)

    def test_matches_with_different_rounds_are_not_equal(self):
        team_a = marchmadness.Entry('A')
        team_b = marchmadness.Entry('B')
        match = marchmadness.Match(
            round_=0,
            index=0,
            top=team_a,
            bottom=team_b,
            result=Result.TOP_WINS
        )
        different_round_match = marchmadness.Match(
            round_=1,
            index=0,
            top=team_a,
            bottom=team_b,
            result=Result.TOP_WINS
        )
        self.assertNotEqual(match, different_round_match)

    def test_matches_with_different_indexes_are_not_equal(self):
        team_a = marchmadness.Entry('A')
        team_b = marchmadness.Entry('B')
        match = marchmadness.Match(
            round_=0,
            index=0,
            top=team_a,
            bottom=team_b,
            result=Result.TOP_WINS
        )
        different_index_match = marchmadness.Match(
            round_=0,
            index=1,
            top=team_a,
            bottom=team_b,
            result=Result.TOP_WINS
        )
        self.assertNotEqual(match, different_index_match)

    def test_matches_with_different_results_are_not_equal(self):
        team_a = marchmadness.Entry('A')
        team_b = marchmadness.Entry('B')
        match = marchmadness.Match(
            round_=0,
            index=0,
            top=team_a,
            bottom=team_b,
            result=Result.TOP_WINS
        )
        different_result_match = marchmadness.Match(
            round_=0,
            index=0,
            top=team_a,
            bottom=team_b,
            result=Result.BOTTOM_WINS
        )
        self.assertNotEqual(match, different_result_match)

    def test_matches_and_entries_are_not_equal(self):
        empty_entry = marchmadness.EmptyEntry()
        empty_match = marchmadness.Match(
            round_=0,
            index=0,
            top=empty_entry,
            bottom=empty_entry,
            result=None
        )
        self.assertNotEqual(empty_entry, empty_match)
        self.assertNotEqual(empty_match, empty_entry)

    def test_bad_result_returns_none_as_winner(self):
        team_a = marchmadness.Entry('A')
        team_b = marchmadness.Entry('B')
        match = marchmadness.Match(
            round_=0,
            index=0,
            top=team_a,
            bottom=team_b,
            result="not a valid result"
        )
        self.assertIsNone(match.winner)
