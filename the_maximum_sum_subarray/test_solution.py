import unittest
from solution import TheMaximumSumSubarray


class TestTheMaximumSumSubarray(unittest.TestCase):
    def setUp(self):
        self.the_maximum_sum_subarray = TheMaximumSumSubarray()
        self.functions = [
            self.the_maximum_sum_subarray.bottom_up,
        ]

    def test_1_simple(self):
        for f in self.functions:
            self.assertEqual(f([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
            self.assertEqual(f([1, 2, 3, 4, 5, 6, 7, 8, 9]), 45)
            self.assertEqual(f([-1, -2, -3, -4, -5, -6, -7, -8, -9]), -1)
            self.assertEqual(f([1, -2, 3, -4, 5, -6, 7, -8, 9]), 9)
            self.assertEqual(f([1, 2, 3, 4, 5, 6, 7, 8, -45]), 36)
            self.assertEqual(f([1, 1, 2, 3, 2]), 9)

    def test_2_negative_elements(self):
        for f in self.functions:
            self.assertEqual(f([1, 1, -2, 3, 2, -3]), 5)

    def test_4_all_positive(self):
        for f in self.functions:
            self.assertEqual(f([1] * 10), 10)

    def test_5_all_negative(self):
        for f in self.functions:
            self.assertEqual(f([-1] * 10), -1)

    def test_6_empty_input(self):
        for f in self.functions:
            self.assertEqual(f([]), 0)

    def test_7_perf(self):
        for f in self.functions:
            self.assertEqual(f([1] * 1_000_000), 1_000_000)


if __name__ == "__main__":
    unittest.main()
