from hedger import utils, csv_generators


class ProbsGenerator(csv_generators.CsvGenerator):
    def write(self, filepath='data/probs.csv'):
        super().write(filepath)

        fieldnames = ['bracket_code', 'prob']
        with utils.CsvWriter(filepath, fieldnames) as writer:
            all_brackets = self._get_all_brackets()
            for bracket in all_brackets:
                row = {
                    'bracket_code': bracket.get_code(),
                    'prob': bracket.get_prob()
                }
                writer.writerow(row)
