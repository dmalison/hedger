import unittest

from hedger import utils


class DiscreteDistTest(unittest.TestCase):
    def test_discrete_dist_describe_on_uniform_data(self):
        points = [
            {'value': 1, 'prob': .25},
            {'value': 2, 'prob': .25},
            {'value': 3, 'prob': .25},
            {'value': 4, 'prob': .25}
        ]
        dist = utils.DiscreteDist(points)

        expected = {
            'mean': 2.5,
            'p10': 1,
            'p90': 4
        }
        actual = dist.describe()

        self.assertDictEqual(actual, expected)

    def test_discrete_dist_describe_on_unordered_data(self):
        points = [
            {'value': 2, 'prob': .25},
            {'value': 3, 'prob': .25},
            {'value': 1, 'prob': .25},
            {'value': 4, 'prob': .25}
        ]
        dist = utils.DiscreteDist(points)

        expected = {
            'mean': 2.5,
            'p10': 1,
            'p90': 4
        }
        actual = dist.describe()

        self.assertDictEqual(actual, expected)

    def test_discrete_dist_describe_on_nonuniform_data(self):
        points = [
            {'value': 0, 'prob': .4},
            {'value': 3, 'prob': .2},
            {'value': 10, 'prob': .2},
            {'value': 20, 'prob': .1},
            {'value': 50, 'prob': .1}
        ]
        dist = utils.DiscreteDist(points)

        expected = {
            'mean': 9.6,
            'p10': 0,
            'p90': 20
        }
        actual = dist.describe()

        self.assertDictEqual(actual, expected)
