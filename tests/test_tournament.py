import unittest

import marchmadness.entry as entry
import marchmadness.tournament as tournament


class TournamentTest(unittest.TestCase):
    def test_make_matches_with_two_teams(self):
        gryffindor = entry.Entry('Gryffindor')
        slytherin = entry.Entry('Slytherin')
        entries = [gryffindor, slytherin]
        quidditch_cup = tournament.Tournament(entries)

        actual = [repr(m) for m in quidditch_cup.matches]
        final_str = (
            "Match('final')"
            ".set_top(Entry('Gryffindor'))"
            ".set_bottom(Entry('Slytherin'))"
        )
        expected = [final_str]
        self.assertEqual(actual, expected)
