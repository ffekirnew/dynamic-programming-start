from typing import List


class NumberOfExpressionsWithATargetResult:
    @staticmethod
    def top_down(array: List[int], target: int) -> int:
        memo = {}
        def helper(index: int, curr_sum: int) -> int:
            if index == len(array):
                return curr_sum == target
            
            if (index, curr_sum) not in memo:
                memo[(index, curr_sum)] = helper(index + 1, curr_sum + array[index]) + helper(index + 1, curr_sum - array[index])
            
            return memo[(index, curr_sum)]
            