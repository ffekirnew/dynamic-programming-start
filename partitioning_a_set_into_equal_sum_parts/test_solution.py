import unittest
import inspect

from solution import PartitioningASetIntoEqualSumParts


class TestPartitioningASetIntoEqualSumParts(unittest.TestCase):
    def setUp(self):
        self.solution = PartitioningASetIntoEqualSumParts()

        # Retrieve all the methods from the solution instance and store all the methods for testing
        self.functions = [method for name, method in inspect.getmembers(
            self.solution, predicate=inspect.ismethod)]

    def test_easy_cases(self):
        for f in self.functions:
            self.assertEqual(f([1, 2, 3, 4]), True)
            self.assertEqual(f([1, 2, 3, 5]), False)
            self.assertEqual(f([1, 2, 3, 6]), False)
            self.assertEqual(f([1, 2, 3, 7]), False)


if __name__ == "__main__":
    unittest.main()
