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
