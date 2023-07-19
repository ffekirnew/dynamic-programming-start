# 8. The maximum-sum subarray
## Problem Statement
Given an array of integers, find the contiguous subarray with the largest sum. If the array is empty, return 0.

### Input Format
An array of integers.

### Output Format
An integer representing the largest sum.

## Examples
### Example 1
```
Input:
[-2, 1, -3, 4, -1, 2, 1, -5, 4]

Output:
6
```

### Example 2
```
Input:
[1, 2, 3, 4, -10]

Output:
10
```

## Constraints
The length of the array is between 1 and 1,000,000.

## Solutions
### Solution 1: Bottom-up (Time complexity: O(n), Space Complexity O(1))
The intuition for maximizing a sum in an array of numbers is to always take in positive numbers. That makes sense, because adding in another positive number makes the sum larger. Another intuition that makes sense is, combining different collection of positve numbers. I.e. let's say you have 3 positive numbers over on one side and another 4 numbers over on the other side. It only makes sense to combine them to make a larger group of positive numbers of 7 numbers with a larger sum. But what if to connect them, there is a negative number in between them. Well, we are now obliged to add this negative number in. A small price to pay for the greater good.

## LeetCode
- [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)