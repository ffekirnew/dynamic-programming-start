# 9. The Maximum Product Subarray
## Problem Statement
Given an integer array `nums`, find the contiguous subarray within an array (containing at least one number) which has the largest product.

### Input Format
An integer array `nums`.

### Output Format
An integer representing the maximum product.

## Examples
### Example 1
```
Input:
[2, 3, -2, 4]

Output:
6
```

### Example 2
```
Input:
[-2, 0, -1]

Output:
0
```

## Constraints
The length of the array is between 1 and 10,000.

## Solutions
### Solution 1: Bottom Up (Time Complexity: O(n), Space Complexity: O(n))
We maintain a 2D list, ending_at, to store the maximum and minimum products ending at each index. Starting from the second element, we iteratively calculate the maximum and minimum products ending at the current index by considering three cases: the current element itself, the product of the current element with the maximum product ending at the previous index, and the product of the current element with the minimum product ending at the previous index. We continuously update the maximum product encountered during the iteration in the max_product variable. After the loop, we return the final max_product, representing the maximum product of a contiguous subarray within the input array.

### Solution 2: Bottom Up (Time Complexity: O(n), Space Complexity: O(1))
This is just an optimization of the previous solution, as the keen eyed would notice we don't need to keep the max and min for each index, rather just for the last index. We can just keep track of the max and min for the last index and update them as we iterate through the array.

## LeetCode
- [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray)