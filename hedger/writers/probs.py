from hedger import utils, writers

PATH = 'data/probs.csv'


class ProbsWriter(writers.Writer):

    def __init__(self, teams):
        super().__init__(teams, PATH)

    def write(self):
        super().write()

        fieldnames = ['bracket_code', 'prob']
        with utils.CsvWriter(self._path, fieldnames) as writer:
            all_brackets = self._get_all_brackets()
            for bracket in all_brackets:
                row = {
                    'bracket_code': bracket.get_code(),
                    'prob': bracket.get_prob()
                }
                writer.writerow(row)


class ProbsReader(writers.Reader):
    @classmethod
    def _get_path(cls):
        return PATH
