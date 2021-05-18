import unittest

from hedger import utils


class NamedTupleTest(unittest.TestCase):
    def setUp(self):
        self.Point = utils.named_tuple('Point', ('x', 'y'))
        self.point = self.Point(1, y=2)

    def test_named_tuple_field_access(self):
        self.assertEqual(self.point.x, 1)
        self.assertEqual(self.point.y, 2)

    def test_named_tuple_index_access(self):
        self.assertEqual(self.point[0], 1)
        self.assertEqual(self.point[1], 2)

    def test_named_tuple_unpacking(self):
        x, y = self.point

        self.assertEqual(x, 1)
        self.assertEqual(y, 2)

    def test_named_tuple_repr(self):
        self.assertEqual(repr(self.point), "Point(x=1, y=2)")

    def test_named_tuple_fields(self):
        self.assertEqual(self.Point._fields, ('x', 'y'))
        self.assertEqual(self.point._fields, ('x', 'y'))

    def test_named_tuple_asdict(self):
        self.assertDictEqual(self.point._asdict(), {'x': 1, 'y': 2})

    def test_named_tuple_raises_error_if_fields_are_missing(self):
        with self.assertRaises(TypeError):
            self.Point(1)

        with self.assertRaises(TypeError):
            self.Point(y=2)
