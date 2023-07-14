from typing import List


class PartitioningASetIntoEqualSumParts:
    @staticmethod
    def brute_force(set: List[int]) -> bool:
        def backtrack(index: int, partiton1_sum: int, partition2_sum: int):
            if index == len(set):
                return partiton1_sum == partition2_sum
            
            return backtrack(index + 1, partiton1_sum + set[index], partition2_sum) or \
                backtrack(index + 1, partiton1_sum, partition2_sum + set[index])
        
        return backtrack(0, 0, 0)

    @staticmethod
    def dynamic_programming(set: List[int]) -> bool:
        total_sum = sum(set)

        if total_sum % 2:
            return False
        
        half_sum = [total_sum // 2]

        memo = {}
        def dp(index: int, curr_sum: int):
            if index == len(set):
                return curr_sum == half_sum
            
            if (index, curr_sum) not in memo:
                memo[(index, curr_sum)] = dp(index + 1, curr_sum) or dp(index + 1, curr_sum + set[index])
            
            return memo[(index, curr_sum)]
        
        return dp(0, 0)
