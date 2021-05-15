from hedger import utils

Point = utils.named_tuple('Point', ['value', 'prob'])
Summary = utils.named_tuple('Summary', ['mean', 'p10', 'p90'])


class DiscreteDist:
    def __init__(self, points):
        self._points = self._convert_to_named_tuples(points)

    def summarize(self):
        summary = Summary(
            mean=self._get_mean(),
            p10=self._get_quantile(.1),
            p90=self._get_quantile(.9)
        )
        return summary._asdict()

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
