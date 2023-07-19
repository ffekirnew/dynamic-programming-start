# 18. Maximum-score path through maze
## Problem Statement
You are given a 2D array of integers. The array represents a maze. Each cell in the maze has a score, and a cell with a `-1` score is a blocked cell. You are initially at the top-left cell in the maze. You are allowed to move either right or down one cell at a time. You have to reach the bottom-right cell in the maze. Find the path that yields the maximum score.

### Input Format
A 2D array of integers.

### Output Format
An integer representing the maximum score.

## Examples
### Example 1
```
Input:
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Output:
29
```

## Constraints
The rows in the maze are between 1 and 1000.
The columns in the maze are between 1 and 1000.

## Solutions
### Solution 1: Top-down (Time complexity: O(n), Space Complexity O(n))
The intuition behind this solution is very easy. By following the rules and backtracking, list every possible sum that can be achieved and pick the maximum. But keep a memo to not calculate the same sum twice.

### Solution 2: Bottom-up (Time complexity: O(n), Space Complexity O(1))
The intuition, here, on the other hand is the idea of extending sums. See, we have a 2D matrix and we want to connect (0, 0) and (n - 1, m - 1) by going to the right or down. So by starting from (0, 0) and going to the right, we can extend the sum to (0, 1). And by going down, we can extend the sum to (1, 0). So we can extend the sum to (1, 1) by taking the maximum of the sum from (0, 1) and (1, 0) and adding it to the current cell. We can keep doing this until we reach (n - 1, m - 1). Then we can be sure that we have the maximum sum at (n - 1, m - 1).

## LeetCode
- [64. Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)
- [1301. Number of Paths with Max Score](https://leetcode.com/problems/number-of-paths-with-max-score/)
- [741. Cherry Pickup](https://leetcode.com/problems/cherry-pickup/)