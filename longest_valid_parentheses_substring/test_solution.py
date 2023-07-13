import unittest 
from solution import LongestValidParenthesisSubstring


class TestLongestValidParenthesisSubstring(unittest.TestCase):
    def setUp(self):
        self.solution = LongestValidParenthesisSubstring()
        self.functions = [self.solution.bottom_up]

    def test_1_one_pair(self):
        for f in self.functions:
            self.assertEqual(f('()'), 2)
            self.assertEqual(f('(' + '()'), 2)
            self.assertEqual(f('()' + ')'), 2)
            self.assertEqual(f(')' + '()'), 2)

    def test_2_neighbour_pairs(self):
        for f in self.functions:
            self.assertEqual(f('()()'), 4)
            self.assertEqual(f('(' + '()()'), 4)
            self.assertEqual(f('()()' + '('), 4)
            self.assertEqual(f('()()' + ')'), 4)

    def test_3_nested_pairs(self):
        for f in self.functions:
            self.assertEqual(f('(())'), 4)
            self.assertEqual(f('(' + '(())'), 4)
            self.assertEqual(f('(())' + ')'), 4)
            self.assertEqual(f('(())' + '('), 4)

    def test_4_multiple_substrings(self):
        for f in self.functions:
            self.assertEqual(f('()' + '(())'), 6)
            self.assertEqual(f('(())' + '()'), 6)
            self.assertEqual(f('()' + ')' + '(())'), 4)
            self.assertEqual(f('(())' + ')' + '()'), 4)
            self.assertEqual(f('(()))())('), 4)

    def test_5_no_valid_substring(self):
        for f in self.functions:
            self.assertEqual(f(''), 0)
            self.assertEqual(f(')'), 0)
            self.assertEqual(f('('), 0)
            self.assertEqual(f(')))((('), 0)

    def test_6_perf(self):
        n = 1000
        k = 10
        s = ')'.join(['(' * n + ')' * n] * k)
        for f in self.functions:
            self.assertEqual(f(s), n * 2)
        s = ')'.join(['()' * n] * k)
        for f in self.functions:
            self.assertEqual(f(s), n * 2)

if __name__ == '__main__':
    unittest.main()