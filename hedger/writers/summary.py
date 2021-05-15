from hedger import utils, writers


PATH = 'data/summary.csv'


class SummaryGenerator(writers.Writer):
    def __init__(self, teams):
        super().__init__(teams, PATH)

    def write(self):
        super().write()

        summary_fields = self._get_summary_fields()
        fieldnames = ['bracket_code'] + summary_fields

        with utils.CsvWriter(self._path, fieldnames) as writer:
            scores = writers.ScoresReader.read()
            probs = writers.ProbsReader.read()

            all_brackets = self._get_all_brackets()
            for bracket in all_brackets:
                row = {'bracket_code': bracket.get_code()}
                row.update()
                writer.writerow(row)

    def _get_summary_fields(self):
        return list(utils.Summary._fields)

