import itertools


def pairwise_grouper(iterable, fillvalue=None):
    args = [iter(iterable)] * 2
    return itertools.zip_longest(*args, fillvalue=fillvalue)
