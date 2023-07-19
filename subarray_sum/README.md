# 19. Subarray Sum
## Problem Statement
Given an array of integers, and queries of the form `(i, j)`, find the sum of the elements in the subarray `arr[i...j]`. If the array is empty, return 0.

### Input Format
An array of integers and an array of queries.

### Output Format
An array of integers representing the sum of the subarray for each query.

## Examples
### Example 1
```
Input:
arr = [1, 2, 3, 4, 5]
queries = [(1, 3), (2, 4), (0, 0), (0, 4)]

Output:
[9, 9, 1, 15]
```

### Example 2
```
Input:
arr = []
queries = [(1, 3), (2, 4), (0, 0), (0, 4)]

Output:
[0, 0, 0, 0]
```

## Constraints
The length of the array is between 1 and 1,000,000.
The length of the queries array is between 1 and 1,000,000.

## Solutions

## LeetCode
- [303. Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/)