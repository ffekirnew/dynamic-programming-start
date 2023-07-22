from typing import List


class MaximumProductSubarray:
    @staticmethod
    def bottom_up(array: List[int]) -> int:
        max_product = array[0]
        ending_at = [[num, num] for num in array]

        for i, num in enumerate(array):
            if not i:
                continue

            ending_at[i][0] = max(num, num * ending_at[i - 1][0], num * ending_at[i - 1][1])
            ending_at[i][1] = min(num, num * ending_at[i - 1][0], num * ending_at[i - 1][1])
            
            max_product = max(max_product, ending_at[i][0])

        return max_product
    
    @staticmethod
    def optimal_bottom_up(array: List[int]) -> int:
        max_product = array[0]
        ending_at_last_index = [array[0], array[0]] # at the zeroeth index, bot the maximum and minimum subarray product is the number it self

        for i in range(1, len(array)):
            num = array[i]

            ending_at_index = [
                max(num, num * ending_at_last_index[0], num * ending_at_last_index[1]),
                min(num, num * ending_at_last_index[0], num * ending_at_last_index[1]),
            ]

            max_product = max(max_product, ending_at_index[0])

            ending_at_last_index = ending_at_index
        
        return max_product
