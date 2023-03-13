import unittest
from LBTT import calc_lbbt


class TestCalc(unittest.TestCase):

    def test_calc_lbbt(self):
        self.assertRaises(ValueError, calc_lbbt, -10000)     # This is testing the bottom extreme scenario
        self.assertEqual(calc_lbbt(130000), 0)               # These unit test the different price brackets
        self.assertEqual(calc_lbbt(225000), 1600)
        self.assertEqual(calc_lbbt(300000), 4600)
        self.assertEqual(calc_lbbt(500000), 23350)
        self.assertEqual(calc_lbbt(825000), 57350)
        self.assertEqual(calc_lbbt(10000000), 1158350)      # This is testing the top extreme scenario
