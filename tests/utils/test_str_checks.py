import unittest

from hedger import utils


class StrChecksTest(unittest.TestCase):
    def test_isint_with_zero_returns_true(self):
        self.assertTrue(utils.is_str_int("0"))

    def test_isint_with_leading_zero_returns_true(self):
        self.assertTrue(utils.is_str_int("01"))

    def test_isint_with_negative_number_returns_true(self):
        self.assertTrue(utils.is_str_int("-1"))

    def test_isint_with_float_returns_false(self):
        self.assertFalse(utils.is_str_int("1.0"))

    def test_isint_with_str_returns_false(self):
        self.assertFalse(utils.is_str_int("foo"))

    def test_isfloat_with_zero_returns_true(self):
        self.assertTrue(utils.is_str_float("0"))

    def test_isfloat_with_leading_zero_returns_true(self):
        self.assertTrue(utils.is_str_float("01"))

    def test_isfloat_with_negative_number_returns_true(self):
        self.assertTrue(utils.is_str_float("-1"))

    def test_isfloat_with_float_returns_true(self):
        self.assertTrue(utils.is_str_float("1.0"))

    def test_isfloat_with_negative_float_returns_true(self):
        self.assertTrue(utils.is_str_float("-1.0"))

    def test_isfloat_with_str_returns_false(self):
        self.assertFalse(utils.is_str_float("foo"))

    def test_isfloat_with_scientific_notation_returns_true(self):
        self.assertTrue(utils.is_str_float("1.0e-7"))
