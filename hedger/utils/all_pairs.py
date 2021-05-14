import itertools


def all_pairs_product(iterable):
    return itertools.product(iterable, repeat=2)
