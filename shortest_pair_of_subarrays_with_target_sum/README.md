# 10. Shortest pair of subarrays with target sum

## Problem Statement

Given an array of positive integers, find the length of the shortest pair of subarrays both with sum equal to the target sum. The subarrays should be such that they do not overlap.

### Input Format

The input is going to be an array of numbers and an integer, which is the target sum.

### Output Format

If you can find such subarrays, return the sum of their lengths. Otherwise, return -1.

## Examples

### Example 1:

```
Input:
array = [3, 4, 7, 2, -3, 1, 4, 2]
target = 7

Output:
3
```

### Example 2:

```
Input:
array = [1, 1, 1, 1, 1, 1, 1, 1]
target = 11

Output:
-1
```

## Constraints

- The array can contain up to 10,000 integers.

## Solutions

### Solution 1: Bruteforce: Sliding window + Check back: (Time Complexity: O(n^2), Space Complexity: O(1)) - Time Limit Exceeded

We can use a sliding window to effectively enumerate all subarrays with the target sum, and whenever we find one, we can check back and evalueate every subarray we have found before to meet the criteria of: a) forming the shortest sum, and b) the subarrays being not overlapping.

### Solution 2: Dynamic Programming (Time Complexity: O(n), Space Complexity: O(n))

This solution also uses the same idea in that it utilizes the sliding window, but rather than check every subarray we have found so far, we can use space and store the shortest subarray with target sum seen at each index. Thus, rather than checking the entire list of subarrays seen before, we can just use the value of the shortest stored at the left - 1 index.

## Leetcode

- [1477. Find Two Non-overlapping Subarrays Each With Target Sum](https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum)
