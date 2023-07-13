# 12. Longest Valid Parenthesis Substring
## Problem Statement

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

### Input Format
A string containing just the characters '(' and ')'.

### Output Format
An integer representing the length of the longest valid parentheses substring.

## Examples
### Example 1:
```
Input:
(()

Output:
2
```
### Example 2:
```
Input:
)()())

Output:
4
```

## Constraints
* 1 <= length of string <= 10^4

## Solution
### Solution 1: Bottom-up Dynamic Programming (Time Complexity: O(n), Space Complexity: O(n))
The intuition for this approach is, we look at each single parenthesis (we should ignore the opening ones since they alone cannot show if they are part of a valid one) and try and find out if it can be used to make a simple valid parenthesis (), if it can be used to make a sandwiching valid parenthesis, like, (()) or if it can be used to extend and already valid parenthesis, like so, ()(). For this purpose, we will keep track of the longest valid parenthesis at each closing bracket and do if-else checks in a single loop.

## Leetcode
- [Longest Valid Parenthesis](https://leetcode.com/problems/longest-valid-parentheses/)