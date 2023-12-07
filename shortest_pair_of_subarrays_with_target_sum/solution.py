from math import inf
from typing import List


class FindTwoSubarrays:
    def __init__(self, arr: List[int], target: int):
        self.arr = arr
        self.target_sum = target

        self.N = len(arr)

    def dp_approach(self) -> int:
        answer = inf

        dp = []  # shortest subarray with target sum at index

        shortest_with_target_sum = inf

        window_sum = 0
        left = 0
        for right in range(self.N):
            window_sum += self.arr[right]
            while window_sum > self.target_sum:
                window_sum -= self.arr[left]
                left += 1

            if window_sum == self.target_sum:
                window_length = right - left + 1
                if left > 0:
                    answer = min(answer, window_length + dp[left - 1])
                shortest_with_target_sum = min(shortest_with_target_sum, window_length)

            dp.append(shortest_with_target_sum)

        return int(answer) if answer != inf else -1


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        solution = FindTwoSubarrays(arr, target)
        return solution.dp_approach()
