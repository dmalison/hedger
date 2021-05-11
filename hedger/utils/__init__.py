from hedger.utils.map_to_counts import MapToCounts
from hedger.utils.csv_reader import CsvReader

import itertools


def pairwise_grouper(iterable, fillvalue=None):
    args = [iter(iterable)] * 2
    return itertools.zip_longest(*args, fillvalue=fillvalue)
