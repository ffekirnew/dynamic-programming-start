from collections import defaultdict
from typing import List


class LongestArithmeticSubsequence:
    @staticmethod
    def bottom_up(sequence: List[int]) -> int:
        longest_subsequence = 1

        dp = [defaultdict(int) for _ in range(len(sequence))] # To store [index][arithmetic_difference]
        for index, curr_number in enumerate(sequence):
            for prev_number_index in range(0, index):
                prev_number = sequence[prev_number_index]
                arithmetic_diff = curr_number - prev_number

                if dp[prev_number_index][arithmetic_diff]:
                    dp[index][arithmetic_diff] = dp[prev_number_index][arithmetic_diff] + 1
                else:
                    dp[index][arithmetic_diff] = dp[prev_number_index][arithmetic_diff] + 2

                longest_subsequence = max(
                    longest_subsequence, dp[index][arithmetic_diff])

        return longest_subsequence


if __name__ == "__main__":
    solution = LongestArithmeticSubsequence()

    print(solution.bottom_up([3, 6, 9, 12]))
    print(solution.bottom_up([9, 4, 7, 2, 10]))
