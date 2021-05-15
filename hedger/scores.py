class Reader:
    @classmethod
    def read(cls, path):
        with utils.CsvReader(path) as reader:
            return reader.read_all()


class Scores:
    def __init__(self):
        self._data = writers.Reader.read(PATH, ROW._fieldnames)

    def get_scores_for_bracket(self, bracket):
        pass
