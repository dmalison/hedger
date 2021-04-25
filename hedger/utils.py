import itertools


def pairwise_grouper(iterable, fillvalue=None):
    args = [iter(iterable)] * 2
    return itertools.zip_longest(*args, fillvalue=fillvalue)


class MapToCounts:
    def __init__(self):
        self._dict = dict()

    def increment(self, key, amount=1):
        previous_count = self._dict.get(key, 0)
        self._dict[key] = previous_count + amount

    def items(self):
        return self._dict.items()

    def get(self, key, value=None):
        return self._dict.get(key, value)
