from hedger import utils, csv_generators


class ScoresGenerator(csv_generators.CsvGenerator):
    def write(self, filepath='data/scores.csv'):
        super().write(filepath)

        fieldnames = ['bracket_code', 'scoring_bracket_code', 'score']
        with utils.CsvWriter(filepath, fieldnames) as writer:
            all_brackets = self._get_all_brackets()
            for bracket, scoring_bracket in utils.all_pairs_product(all_brackets):
                row = {
                    'bracket_code': bracket.get_code(),
                    'scoring_bracket_code': scoring_bracket.get_code(),
                    'score': bracket.get_score(scoring_bracket)
                }
                writer.writerow(row)
