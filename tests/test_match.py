import unittest

import hedger
from hedger.result import Result


class MatchTest(unittest.TestCase):
    def test_match_with_two_entries(self):
        entry_a = hedger.Entry('A')
        entry_b = hedger.Entry('B')
        match = hedger.Match(
            round_=0,
            index=0,
            top=entry_a,
            bottom=entry_b,
            result=Result.TOP_WINS
        )

        expected = (
            "Match(round_=0, index=0, top=Entry('A'), "
            "bottom=Entry('B'), result=Result.TOP_WINS)"
        )

        self.assertEqual(repr(match), expected)
        self.assertEqual(match.get_winner(), entry_a)

    def test_match_with_two_submatches(self):
        entry_a = hedger.Entry('A')
        entry_b = hedger.Entry('B')
        submatch_0 = hedger.Match(
            round_=0,
            index=0,
            top=entry_a,
            bottom=entry_b,
            result=Result.TOP_WINS
        )

        entry_c = hedger.Entry('C')
        entry_d = hedger.Entry('D')
        submatch_1 = hedger.Match(
            round_=0,
            index=1,
            top=entry_c,
            bottom=entry_d,
            result=Result.BOTTOM_WINS
        )

        match = hedger.Match(
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
        self.assertEqual(match.get_winner(), entry_d)

    def test_matches_with_same_entries_are_equal(self):
        entry_a = hedger.Entry('A')
        entry_b = hedger.Entry('B')
        match = hedger.Match(
            round_=0,
            index=0,
            top=entry_a,
            bottom=entry_b,
            result=Result.TOP_WINS
        )
        duplicate_match = hedger.Match(
            round_=0,
            index=0,
            top=entry_a,
            bottom=entry_b,
            result=Result.TOP_WINS
        )
        self.assertEqual(match, duplicate_match)

    def test_matches_with_different_entries_are_not_equal(self):
        entry_a = hedger.Entry('A')
        entry_b = hedger.Entry('B')
        match = hedger.Match(
            round_=0,
            index=0,
            top=entry_a,
            bottom=entry_b,
            result=Result.TOP_WINS
        )
        match_with_top_and_bottom_switched = hedger.Match(
            round_=0,
            index=0,
            top=entry_b,
            bottom=entry_a,
            result=Result.TOP_WINS
        )
        self.assertNotEqual(match, match_with_top_and_bottom_switched)

    def test_matches_with_different_rounds_are_not_equal(self):
        entry_a = hedger.Entry('A')
        entry_b = hedger.Entry('B')
        match = hedger.Match(
            round_=0,
            index=0,
            top=entry_a,
            bottom=entry_b,
            result=Result.TOP_WINS
        )
        match_with_different_round = hedger.Match(
            round_=1,
            index=0,
            top=entry_a,
            bottom=entry_b,
            result=Result.TOP_WINS
        )
        self.assertNotEqual(match, match_with_different_round)

    def test_matches_with_different_indexes_are_not_equal(self):
        entry_a = hedger.Entry('A')
        entry_b = hedger.Entry('B')
        match = hedger.Match(
            round_=0,
            index=0,
            top=entry_a,
            bottom=entry_b,
            result=Result.TOP_WINS
        )
        match_with_different_index = hedger.Match(
            round_=0,
            index=1,
            top=entry_a,
            bottom=entry_b,
            result=Result.TOP_WINS
        )
        self.assertNotEqual(match, match_with_different_index)

    def test_matches_with_different_results_are_not_equal(self):
        entry_a = hedger.Entry('A')
        entry_b = hedger.Entry('B')
        match = hedger.Match(
            round_=0,
            index=0,
            top=entry_a,
            bottom=entry_b,
            result=Result.TOP_WINS
        )
        match_with_different_result = hedger.Match(
            round_=0,
            index=0,
            top=entry_a,
            bottom=entry_b,
            result=Result.BOTTOM_WINS
        )
        self.assertNotEqual(match, match_with_different_result)

    def test_matches_and_entries_are_not_equal(self):
        empty_entry = hedger.EmptyEntry()
        empty_match = hedger.Match(
            round_=0,
            index=0,
            top=empty_entry,
            bottom=empty_entry,
            result=Result.TOP_WINS
        )
        self.assertNotEqual(empty_entry, empty_match)
        self.assertNotEqual(empty_match, empty_entry)

    def test_winner_of_match_with_invalid_result_is_none(self):
        entry_a = hedger.Entry('A')
        entry_b = hedger.Entry('B')
        match = hedger.Match(
            round_=0,
            index=0,
            top=entry_a,
            bottom=entry_b,
            result="not a valid result"
        )
        self.assertIsNone(match.get_winner())
