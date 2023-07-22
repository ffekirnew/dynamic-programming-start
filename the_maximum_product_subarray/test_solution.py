import unittest
import random
from solution import MaximumProductSubarray


class TestMaximumProductSubarray(unittest.TestCase):
    def setUp(self):
        self.functions = [MaximumProductSubarray.bottom_up]

    def test_1_simple(self):
        array = [2, 3, -2, 4]
        expected_result = 6
        for f in self.functions:
            result = f(array)
            self.assertEqual(result, expected_result)

    def test_2_edge(self):
        array = [-2, 0, -1]
        expected_result = 0
        for f in self.functions:
            result = f(array)
            self.assertEqual(result, expected_result)

    def test_3_perf(self):
        array = [random.randint(-1000, 1000) for _ in range(10000)]
        expected_result = self.brute_force_max_product(array)
        for f in self.functions:
            result = f(array)
            self.assertEqual(result, expected_result)

    def brute_force_max_product(self, array):
        max_product = array[0]
        for i in range(len(array)):
            product = 1
            for j in range(i, len(array)):
                product *= array[j]
                max_product = max(max_product, product)
        return max_product


if __name__ == "__main__":
    unittest.main()
