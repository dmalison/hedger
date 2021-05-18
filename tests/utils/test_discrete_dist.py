import unittest

from hedger import utils


class DiscreteDistTest(unittest.TestCase):
    def test_discrete_dist_describe_on_uniform_data(self):
        points = [
            utils.Point(omega=0, value=1, prob=.25),
            utils.Point(omega=1, value=2, prob=.25),
            utils.Point(omega=2, value=3, prob=.25),
            utils.Point(omega=3, value=4, prob=.25),
        ]
        dist = utils.DiscreteDist(points)

        expected = utils.Summary(mean=2.5, p10=1, p90=4)
        actual = dist.summarize()

        self.assertEqual(actual, expected)

    def test_discrete_dist_describe_on_unordered_data(self):
        points = [
            utils.Point(omega=0, value=2, prob=.25),
            utils.Point(omega=1, value=3, prob=.25),
            utils.Point(omega=2, value=1, prob=.25),
            utils.Point(omega=3, value=4, prob=.25),
        ]
        dist = utils.DiscreteDist(points)

        expected = utils.Summary(mean=2.5, p10=1, p90=4)
        actual = dist.summarize()

        self.assertEqual(actual, expected)

    def test_discrete_dist_describe_on_nonuniform_data(self):
        points = [
            utils.Point(omega=0, value=0, prob=.4),
            utils.Point(omega=1, value=3, prob=.2),
            utils.Point(omega=2, value=10, prob=.2),
            utils.Point(omega=3, value=20, prob=.1),
            utils.Point(omega=4, value=50, prob=.1)
        ]
        dist = utils.DiscreteDist(points)

        expected = utils.Summary(mean=9.6, p10=0, p90=20)
        actual = dist.summarize()

        self.assertEqual(actual, expected)
