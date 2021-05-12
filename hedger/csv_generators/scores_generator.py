import hedger
from hedger import utils


class ScoresGenerator:
    def __init__(self, teams):
        self._teams = teams

    def write(self, filepath='data/bracket_scores.csv'):
        fieldnames = ['bracket_code', 'scoring_bracket_code', 'score']
        with utils.CsvWriter(filepath, fieldnames) as writer:
            all_brackets = self._get_all_brackets()
            for bracket, scoring_bracket in utils.all_pairs(all_brackets):
                row = self._get_row(bracket, scoring_bracket)
                writer.writerow(row)

    def _get_row(self, bracket, scoring_bracket):
        score = bracket.compute_score(scoring_bracket)
        row = {
            'bracket_code': bracket.code,
            'scoring_bracket_code': scoring_bracket.code,
            'score': score
        }
        return row

    def _get_all_brackets(self):
        tournament = self._get_tournament()
        return tournament.make_all_brackets()

    def _get_tournament(self):
        entries = self._get_entries()
        return hedger.Tournament(entries)

    def _get_entries(self):
        return [hedger.Entry(team) for team in self._teams]
