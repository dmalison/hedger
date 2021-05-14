import csv

from hedger import utils


class CsvReader:
    def __init__(self, filepath, cast_numeric=True):
        self._filepath = filepath
        self._file = None
        self._reader = None
        self._cast_numeric = cast_numeric

    def __enter__(self):
        self._file = open(self._filepath, 'r', newline='')
        self._reader = csv.DictReader(self._file)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file.close()

    def __next__(self):
        row = next(self._reader)
        if self._cast_numeric:
            self._cast_numeric_values(row)
        return row

    def _cast_numeric_values(self, row):
        for k, v in row.items():
            if utils.isint(v):
                row[k] = int(v)
            elif utils.isfloat(v):
                row[k] = float(v)

    def __iter__(self):
        return self
