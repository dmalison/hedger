from hedger import utils, writers

PATH = 'data/scores.csv'
ScoreRow = utils.named_tuple('ScoreRow', ['bracket_code', 'scoring_bracket_code', 'score'])


class ScoresWriter(writers.Writer):
    def __init__(self, teams):
        super().__init__(teams, PATH)

    def write(self):
        super().write()

        with utils.CsvWriter(self._path, ScoreRow._fieldnames) as writer:
            all_brackets = self._get_all_brackets()
            all_bracket_pairs = utils.all_pairs_product(all_brackets)
            for bracket, scoring_bracket in all_bracket_pairs:
                row = ScoreRow(
                    bracket_code=bracket.get_code(),
                    scoring_bracket_code=scoring_bracket.get_code(),
                    score=bracket.get_score(scoring_bracket)
                )
                writer.writerow(row)
