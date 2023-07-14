import unittest
import inspect

from solution import SplittingAStringWithoutSpacesIntoWords


class TestSplittingAStringWithoutSpacesIntoWords(unittest.TestCase):
    def setUp(self):
        self.solution = SplittingAStringWithoutSpacesIntoWords()

        # Retrieve all the methods from the solution instance and store all the methods for testing
        self.functions = [self.solution.top_down]
        print(self.functions)

    def test_1_easy_test(self):
        for f in self.functions:
            print(f.__name__)
            self.assertEqual(f('a', ['a']), True)
            self.assertEqual(f('ab', ['a', 'b']), True)
            self.assertEqual(f('catseatmice', ['cat', 'eat', 'mice']), False)
            self.assertEqual(f('catseatmice', ['cat', 'seat', 'mice']), True)

    def test_2_stress_test(self):
        for f in self.functions:
            print(f.__name__)
            self.assertEqual(f('aaaaaaaaaaaaaaaaaaaaaaaaaaaa', ['a']), True)

if __name__ == "__main__":
    unittest.main()
