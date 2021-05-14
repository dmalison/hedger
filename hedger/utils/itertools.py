import itertools


def all_pairs_product(iterable):
    return itertools.product(iterable, repeat=2)


def pairwise_grouper(iterable, fillvalue=None):
    args = [iter(iterable)] * 2
    return itertools.zip_longest(*args, fillvalue=fillvalue)
