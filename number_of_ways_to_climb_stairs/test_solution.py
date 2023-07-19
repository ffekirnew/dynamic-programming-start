import unittest

from solution import NumberOfWaysToClimbStairs


class TestNumberOfWaysToClimbStairs(unittest.TestCase):
    def setUp(self):
        self.solution = NumberOfWaysToClimbStairs()

        self.functions = [
            self.solution.bottom_up,
            self.solution.top_down,
        ]
    
    def test_1_simple(self):
        for f in self.functions:
            self.assertEqual(f(2), 2)
            self.assertEqual(f(3), 3)
            self.assertEqual(f(4), 5)
    
    def test_2_edge_cases(self):
        for f in self.functions:
            self.assertEqual(f(0), 0)
            self.assertEqual(f(1), 1)

    def test_3_perf(self):
        for f in self.functions:
            self.assertEqual(f(35), 14930352)
 


if __name__ == "__main__":
    unittest.main()