import hedger
from hedger import utils


class ScoresGenerator:
    def __init__(self, teams):
        self._teams = teams

    def write_csv(self, filepath='data/bracket_scores.csv'):
        tournament = self._get_tournament()
        all_brackets = tournament.make_all_brackets()

        fieldnames = ['bracket_code', 'scoring_bracket_code', 'score']
        with utils.CsvWriter(filepath, fieldnames) as writer:
            for bracket, scoring_bracket in utils.all_pairs(all_brackets):
                score = bracket.compute_score(scoring_bracket)
                row = {
                    'bracket_code': bracket.code,
                    'scoring_bracket_code': scoring_bracket.code,
                    'score': score
                }
                writer.writerow(row)

    def _get_tournament(self):
        entries = self._get_entries()
        return hedger.Tournament(entries)

    def _get_entries(self):
        return [hedger.Entry(team) for team in self._teams]
