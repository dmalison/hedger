import os

from tests.utils.assert_csv_equal import assert_csv_equal


def path_exists(path):
    return os.path.exists(path)


def remove(path):
    os.remove(path)
