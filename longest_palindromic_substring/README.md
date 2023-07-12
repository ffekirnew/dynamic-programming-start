# 11. Longest Palindromic Substring

## Problem Statement

Given a string, find the longest substring which is palindrome. For example, if the given string is “forgeeksskeegfor”, the output should be “geeksskeeg”.

### Input Format

The input is a string.

### Output Format

The output is a string.

## Examples

### Example 1:

```
Input:
forgeeksskeegfor

Output:
geeksskeeg
```

### Example 2:

```
Input:
abababa

Output:
abababa
```

## Constraints

- The input string length is at most 10,000.

## Solutions
### Solution 1: Brute Force (Time complexity: O(n^3), Space complexity: O(1))
The brute force solution is to check every substring of the given string starting from the shortest to the longest and check if it is a palindrome. If it is a palindrome then we check if it is longer than the longest palindrome found so far. If it is longer then we update the longest palindrome found so far.
