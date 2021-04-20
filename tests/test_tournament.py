import unittest

import marchmadness.entry as entry
import marchmadness.match as match
import marchmadness.tournament as tournament


class TournamentTest(unittest.TestCase):
    def test_make_matches_with_two_teams(self):
        gryffindor = entry.Entry('Gryffindor')
        slytherin = entry.Entry('Slytherin')
        entries = [gryffindor, slytherin]
        quidditch_cup = tournament.Tournament(entries)

        actual = [repr(match) for match in quidditch_cup.matches]
        expected = ["Match('final').set_top(Entry('gryffindor')).set_bottom(Entry('slytherin'))"]
        self.assertEqual(actual, expected)
