import itertools


def all_pairs(iterable):
    return itertools.product(iterable, repeat=2)
