from typing import List


class SubmatrixSum:
    @staticmethod
    def prefix_sum(matrix: List[List[int]], queries: List[List[int]]):
        prefix_sum = []
        
        for r, row in enumerate(matrix):
            prefix_sum.append([])
            
            for c, cell in enumerate(row):
                prefix_sum_left = prefix_sum[r][c-1] if c > 0 else 0
                prefix_sum_above = prefix_sum[r-1][c] if r > 0 else 0
                prefix_sum_diagonal = prefix_sum[r-1][c-1] if r > 0 and c > 0 else 0
                
                formula = cell + prefix_sum_left + prefix_sum_above - prefix_sum_diagonal
                
                prefix_sum[-1].append(formula)


        result = []
        for row1, col1, row2, col2 in queries:
            all_sum = prefix_sum[row2][col2]
            left_sum = prefix_sum[row2][col1 - 1] if col1 > 0 else 0
            top_sum = prefix_sum[row1 - 1][col2] if row1 > 0 else 0
            
            tobe_added_sum = prefix_sum[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
            
            result.append(all_sum - left_sum - top_sum + tobe_added_sum)
        

        return result
