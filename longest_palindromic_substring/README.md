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

### Solution 2: Dynamic Programming (Time complexity: O(n^2), Space complexity: O(n))
This is an optimization to the first solution that will eliminate the need to check if a substring is a palindrome. We will use a dynamic programming approach to solve this problem. We will look at each index and assume it is in the center of a palindrome and expand outwards to find the longest palindrome. We will do this for each index and keep track of the longest palindrome found so far. The problem with this is it will not work for palindromes of even length. To solve this we will add a dummy character between each character in the string and at the beginning and end of the string. This will make all palindromes odd length and we can use the same algorithm to find the longest palindrome.

## Leetcode
- [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
- [647. Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/)
- [516. Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/)
