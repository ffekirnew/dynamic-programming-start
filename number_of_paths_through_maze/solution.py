from typing import List


class NumberOfPathsThroughMaze:
    @staticmethod
    def top_down(maze: List[List[int]]):
        def in_bound(row, col):
            return 0 <= row < len(maze) and 0 <= col < len(maze[0])
        
        memo = {}
        def dp(row, col):
            if not in_bound(row, col) or maze[row][col] == 1:
                return 0
            
            if row == len(maze) - 1 and col == len(maze[0]) - 1:
                return 1
            
            if (row, col) not in memo:
                memo[(row, col)] = dp(row + 1, col) + dp(row, col + 1)

            return memo[(row, col)]
        
        return dp(0, 0)
    
    @staticmethod
    def bottom_up(maze: List[List[int]]):
        ROWS, COLS = len(maze), len(maze[0])

        for row in range(ROWS - 1, -1, -1):
            for col in range(COLS - 1, -1, -1):
                if row == ROWS - 1 and col == COLS - 1:
                    maze[row][col] = 1
                    continue

                if maze[row][col] == 1:
                    maze[row][col] = 0
                    continue

                if row < ROWS - 1:
                    maze[row][col] += maze[row + 1][col]

                if col < COLS - 1:
                    maze[row][col] += maze[row][col + 1]
        
        return maze[0][0]