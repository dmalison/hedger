import unittest

import marchmadness
from marchmadness.result import Result


class BracketTest(unittest.TestCase):
    def test_bracket_for_two_team_tournament(self):
        gryffindor = marchmadness.Entry('Gryffindor')
        slytherin = marchmadness.Entry('Slytherin')

        entries = [gryffindor, slytherin]
        quidditch_cup = marchmadness.Tournament(entries)

        bracket = marchmadness.Bracket(quidditch_cup, [Result.TOP_WINS])
        self.assertEqual(bracket.winners, [gryffindor])

    def test_bracket_for_four_team_tournament(self):
        gryffindor = marchmadness.Entry('Gryffindor')
        ravenclaw = marchmadness.Entry('Ravenclaw')
        hufflepuff = marchmadness.Entry('Hufflepuff')
        slytherin = marchmadness.Entry('Slytherin')

        entries = [gryffindor, ravenclaw, hufflepuff, slytherin]
        quidditch_cup = marchmadness.Tournament(entries)

        bracket = marchmadness.Bracket(
            quidditch_cup, 
            [Result.TOP_WINS, Result.BOTTOM_WINS, Result.TOP_WINS]
        )

        self.assertEqual(bracket.winners, [gryffindor, slytherin, gryffindor])