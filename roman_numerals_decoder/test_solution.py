from unittest import TestCase

from solution import solution as s


class TestSolution(TestCase):
    def test_simple_case(self):
        res = s("I")
        self.assertEqual(res, 1)

        res = s("III")
        self.assertEqual(res, 3)

        res = s("IV")
        self.assertEqual(res, 4)

    def test_kata(self):
        self.assertEqual(s("XXI"), 21)
        self.assertEqual(s("MMVIII"), 2008)
        self.assertEqual(s("MDCLXVI"), 1666)
