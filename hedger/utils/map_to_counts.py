import collections


class MapToCounts(collections.UserDict):
    def __setitem__(self, key, value):
        if self._is_valid_value(value):
            self.data[key] = value
        else:
            raise ValueError("Value must be non-negative int.")

    def increment(self, key):
        previous_count = self.data.get(key, 0)
        self.data[key] = previous_count + 1

    def _is_valid_value(self, value):
        return isinstance(value, int) and value >= 0
