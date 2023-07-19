from typing import List


class SubarraySum:
    @staticmethod
    def prefix_sum(array: List[int], queries: List[List[int]]) -> List[int]:
        prefix_sum = [0] * (len(array) + 1)

        for i in range(len(array)):
            prefix_sum[i + 1] = prefix_sum[i] + array[i]
        

        result = []
        for query in queries:
            result.append(prefix_sum[query[1] + 1] - prefix_sum[query[0]])
        
        return result
