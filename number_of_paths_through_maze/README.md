# 17. Number of paths through maze
## Problem Statement
You are given a 2D array of integers. The array represents a maze. Each cell in the maze has a score, and a cell with a `1` score is a blocked cell. You are initially at the top-left cell in the maze. You are allowed to move either right or down one cell at a time. You have to reach the bottom-right cell in the maze. Find the number of paths that lead to the bottom-right cell.

### Input Format
A 2D array of integers.

### Output Format
An integer representing the number of paths.

## Examples
### Example 1
```
Input:
[
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]

Output:
2
```

## Constraints
The rows in the maze are between 1 and 1000.
The columns in the maze are between 1 and 1000.

## Solutions
### Solution 1: Top-down (Time complexity: O(n), Space Complexity O(n))
The intuition behind this solution is very easy.Standing on any cell, the path between itself and the bottom-right cell is the sum of the paths between the cell to the right of it and the bottom-right cell and the cell below it and the bottom-right cell. So we can recursively calculate the number of paths between the cell to the right of it and the bottom-right cell and the cell below it and the bottom-right cell. But keep a memo to not calculate the same path twice.

### Solution 2: Bottom-up (Time complexity: O(n), Space Complexity O(1))
The intuition, here, on the other hand is the idea of extending paths. See, we have a 2D matrix and we want to connect (0, 0) and (n - 1, m - 1) by going to the right or down. But the end goal is to reach that bottom-right corner. So by hook-or-crook, if that bottom-right is reached, that is counted as one path. Then we move to it's neighbouring cells in the opposite direction the (n - 2, m - 1) and (n - 1, m - 2) cells. And we can extend the path to them, since they are direct neighbours, there's only one path with the given rules. Like this we can work our way backward until we reach (0, 0). Then we can be sure that we have the number of paths at (0, 0).

## LeetCode
- [62. Unique Paths](https://leetcode.com/problems/unique-paths/)