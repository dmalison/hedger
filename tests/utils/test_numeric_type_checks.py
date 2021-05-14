import unittest

from hedger import utils


class NumericTypeChecksTest(unittest.TestCase):
    def test_isint_with_zero_returns_true(self):
        self.assertTrue(utils.isint("0"))

    def test_isint_with_leading_zero_returns_true(self):
        self.assertTrue(utils.isint("01"))

    def test_isint_with_negative_number_returns_true(self):
        self.assertTrue(utils.isint("-1"))

    def test_isint_with_float_returns_false(self):
        self.assertFalse(utils.isint("1.0"))

    def test_isint_with_str_returns_false(self):
        self.assertFalse(utils.isint("foo"))

    def test_isfloat_with_zero_returns_true(self):
        self.assertTrue(utils.isfloat("0"))

    def test_isfloat_with_leading_zero_returns_true(self):
        self.assertTrue(utils.isfloat("01"))

    def test_isfloat_with_negative_number_returns_true(self):
        self.assertTrue(utils.isfloat("-1"))

    def test_isfloat_with_float_returns_true(self):
        self.assertTrue(utils.isfloat("1.0"))

    def test_isfloat_with_negative_float_returns_true(self):
        self.assertTrue(utils.isfloat("-1.0"))

    def test_isfloat_with_str_returns_false(self):
        self.assertFalse(utils.isfloat("foo"))

    def test_isfloat_with_scientific_notation_returns_true(self):
        self.assertTrue(utils.isfloat("1.0e-7"))
