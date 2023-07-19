# 20. Subarray Matrix
## Problem Statement
Given a matrix of integers, and queries of the form `(i1, j1, i2, j2)`, find the sum of the elements in the submatrix `matrix[i1...i2][j1...j2]`. If the matrix is empty, return 0.

### Input Format
A matrix of integers and an array of queries.

### Output Format
An array of integers representing the sum of the submatrix for each query.

## Examples
### Example 1
```
Input:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
queries = [(1, 1, 2, 2), (0, 0, 2, 2), (1, 2, 2, 2)]

Output:
[12, 45, 6]
```

## Constraints
The number of rows in the matrix is between 1 and 1,000.
The number of columns in the matrix is between 1 and 1,000.
The number of queries is between 1 and 1,000,000.

## Solutions

## LeetCode
- [304. Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/)