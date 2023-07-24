from typing import List
from math import inf


class MaximumScorePathThroughMaze:
    @staticmethod
    def top_down(grid: List[List[int]]) -> int:
        def in_bound(row: int, col: int) -> bool:
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        memo = {}

        def dp(row, col) -> int:
            if not in_bound(row, col):
                return int(-inf)

            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return grid[row][col]

            if not (row, col) in memo:
                memo[(row, col)] = max(dp(row + 1, col),
                                       dp(row, col + 1)) + grid[row][col]

            return memo[(row, col)]

        return dp(0, 0)

    @staticmethod
    def bottom_up(grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        for row in range(ROWS):
            for col in range(COLS):
                value = grid[row][col]
                if row > 0:
                    grid[row][col] = max(grid[row][col], grid[row - 1][col] + value)
                if col > 0:
                    grid[row][col] = max(grid[row][col], grid[row][col - 1] + value)

        return grid[ROWS - 1][COLS - 1]
