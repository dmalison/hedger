import unittest

import marchmadness
from marchmadness.result import Result


class BracketTest(unittest.TestCase):
    def test_bracket_for_two_team_tournament(self):
        gryffindor = marchmadness.Entry('Gryffindor')
        slytherin = marchmadness.Entry('Slytherin')
        entries = [gryffindor, slytherin]
        quidditch_cup = marchmadness.Tournament(entries)

        bracket_0 = marchmadness.Bracket(quidditch_cup, [Result.TOP_WINS])
        bracket_1 = marchmadness.Bracket(quidditch_cup, [Result.BOTTOM_WINS])

        self.assertEqual(bracket_0.winners, [gryffindor])
        self.assertEqual(bracket_1.winners, [slytherin])
