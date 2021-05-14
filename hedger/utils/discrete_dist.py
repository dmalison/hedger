import collections

Point = collections.namedtuple('Point', ['value', 'prob'])


class DiscreteDist:
    def __init__(self, points):
        self._points = self._convert_to_named_tuples(points)

    def describe(self):
        return {
            'mean': self._get_mean(),
            'p10': self._get_quantile(.1),
            'p90': self._get_quantile(.9)
        }

    def _convert_to_named_tuples(self, points):
        pts = [Point(**p) for p in points]
        pts.sort(key=lambda pt: pt.value)
        return pts

    def _get_mean(self):
        return sum(p.value * p.prob for p in self._points)

    def _get_quantile(self, q):
        cdf = 0
        for p in self._points:
            cdf += p.prob
            if cdf >= q:
                return p.value
