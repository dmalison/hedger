import csv


class CsvWriter:
    def __init__(self, filepath, fieldnames):
        self._filepath = filepath
        self._fieldnames = fieldnames
        self._file = None
        self._writer = None

    def __enter__(self):
        self._file = open(self._filepath, 'w', newline='')
        self._writer = csv.DictWriter(self._file, self._fieldnames)
        self._writer.writeheader()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file.close()

    def writerow(self, row) -> None:
        self._writer.writerow(row)
