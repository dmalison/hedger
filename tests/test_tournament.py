import unittest

import hedger
from hedger import Result


class TournamentTest(unittest.TestCase):
    def test_make_brackets_with_four_teams(self):
        gryffindor = hedger.Entry('Gryffindor')
        ravenclaw = hedger.Entry('Ravenclaw')
        hufflepuff = hedger.Entry('Hufflepuff')
        slytherin = hedger.Entry('Slytherin')
        entries = [gryffindor, ravenclaw, hufflepuff, slytherin]
        quidditch_cup = hedger.Tournament(entries)
        all_brackets = quidditch_cup.get_brackets()

        all_results = [
            [Result.BOTTOM_WINS, Result.BOTTOM_WINS, Result.BOTTOM_WINS],
            [Result.BOTTOM_WINS, Result.BOTTOM_WINS, Result.TOP_WINS],
            [Result.BOTTOM_WINS, Result.TOP_WINS, Result.BOTTOM_WINS],
            [Result.BOTTOM_WINS, Result.TOP_WINS, Result.TOP_WINS],
            [Result.TOP_WINS, Result.BOTTOM_WINS, Result.BOTTOM_WINS],
            [Result.TOP_WINS, Result.BOTTOM_WINS, Result.TOP_WINS],
            [Result.TOP_WINS, Result.TOP_WINS, Result.BOTTOM_WINS],
            [Result.TOP_WINS, Result.TOP_WINS, Result.TOP_WINS]
        ]

        for bracket, results in zip(all_brackets, all_results):
            actual_matches = bracket.matches

            semifinal_0 = hedger.Match(
                round_=0,
                index=0,
                top=gryffindor,
                bottom=ravenclaw,
                result=results[0]
            )
            semifinal_1 = hedger.Match(
                round_=0,
                index=1,
                top=hufflepuff,
                bottom=slytherin,
                result=results[1]
            )
            final = hedger.Match(
                round_=1,
                index=0,
                top=semifinal_0,
                bottom=semifinal_1,
                result=results[2]
            )
            expected_matches = [semifinal_0, semifinal_1, final]

            self.assertEqual(actual_matches, expected_matches)
