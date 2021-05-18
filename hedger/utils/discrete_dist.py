from hedger import utils

Point = utils.named_tuple('Point', ['omega', 'prob', 'value'])
Summary = utils.named_tuple('Summary', ['mean', 'p10', 'p90'])


class DiscreteDist:
    def __init__(self, points):
        self._points = points
        self._sort_points()

    def summarize(self):
        return Summary(
            mean=self._get_mean(),
            p10=self._get_quantile(.1),
            p90=self._get_quantile(.9)
        )

    def _sort_points(self):
        self._points.sort(key=lambda pt: pt.value)

    def _get_mean(self):
        return sum(p.value * p.prob for p in self._points)

    def _get_quantile(self, q):
        cdf = 0
        for p in self._points:
            cdf += p.prob
            if cdf >= q:
                return p.value
