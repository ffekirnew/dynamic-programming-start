from math import inf
from typing import List


class TheMaximumSumSubarray:
    @staticmethod
    def bottom_up(array: List[int]) -> int:
        best_sum_ending_at_last_index = 0 # will keep the best sum ending at the previous index

        max_sum_subarray = -inf
        for number in array:
            best_sum_ending_at_index = max(best_sum_ending_at_last_index + number, number)
            max_sum_subarray = max(max_sum_subarray, best_sum_ending_at_index)
            best_sum_ending_at_last_index = best_sum_ending_at_index

        return max_sum_subarray if max_sum_subarray != -inf else 0

if __name__ == "__main__":
    print(TheMaximumSumSubarray.bottom_up([-2, 1, -3, 4, -1, 2, 1, -5, 4]))



