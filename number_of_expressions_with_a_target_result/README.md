# 4. Number of Expressions with a Target Result
## Problem Statement
Given a string of numbers and operators, find the number of ways to evaluate the expression to a given target result. The expression is given as a list of numbers. The operators are `+` and `-`. The target result is a non-negative integer.

### Input Format
The first line of input contains the string of numbers and operators. The second line of input contains the target result.

### Output Format
An integer representing the number of ways to evaluate the expression to the target result.

## Examples
### Example 1
```
Input:
[1, 1, 1, 1, 1]
3

Output:
5
```

### Example 2
```
Input:
[1, 2, 3, 4, 5]
5

Output:
1
```

## Constraints
The length of the expression is between 1 and 1000.

## Solutions
### Solution 1: Top-down (Time complexity: O(n * T), Space Complexity O(n * T)), n for length of expression, T for target result
The intuition behind this solution is very easy. Standing on any number, the number of ways to evaluate the expression to the target result is the sum of the number of ways to evaluate the expression to the target result with the number to the right of it and the number to the right of it with a minus sign. So we can recursively calculate the number of ways to evaluate the expression to the target result with the number to the right of it and the number to the right of it with a minus sign. But keep a memo to not calculate the same path twice.

## LeetCode
- [494. Target Sum](https://leetcode.com/problems/target-sum/)