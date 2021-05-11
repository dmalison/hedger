import csv


class CsvReader:
    def __init__(self, filepath: str):
        self._filepath = filepath
        self._file = None
        self._reader = None

    def __enter__(self):
        self._file = open(self._filepath, 'r', newline='')
        self._reader = csv.DictReader(self._file)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file.close()

    def __next__(self):
        return next(self._reader)

    def __iter__(self):
        return self
