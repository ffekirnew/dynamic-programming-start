# 5. Partitioning a Set into Equal-Sum Parts
## Problem Statement
Given a set of integers, determine if the set can be partitioned into two subsets such that the sum of elements in both subsets is same. The subsets should be such that they do not overlap. Also, the union of both the subsets should be equal to the original set.

### Input Format
The only input contains the elements of the set.

### Output Format
The output is a boolean value that indicates whether the set can be partitioned into two subsets with equal sum or not.

## Examples
### Example 1:
```
Input:
1 5 11 5

Output:
True
```

### Example 2:
```
Input:
1 5 3

Output:
False
```

## Constraints
- The set can contain up to 50 elements.

## Solutions
### Solution 1: Bruteforce: Backtracking (Time Complexity: O(2^n), Space Complexity: O(n)) - Time Limit Exceeded
The bruteforce solution is to try all possible combinations of the elements in the set. For each element, we have two choices: either to include it in the first subset or to include it in the second subset. We try both choices and recursively check if the subsets can be partitioned into two subsets with equal sum. If any of the subsets can be partitioned into two subsets with equal sum, we return `True`. Otherwise, we return `False`.

### Solution 2: Dynamic Programming (Time Complexity: O(n), Space Complexity: O(1))
The intuition is the sum of one partition is going to be half of the total sum of the given input set. So we can first find the sum of the set and if it is even, there is a possibility that the set can be partitioned. If the sum is odd, there is no possibility that the set can be partitioned. If the sum is even, we can find a subset of the set with sum equal to half of the total sum of the set. If such a subset exists, the set can be partitioned into two subsets with equal sum. Otherwise, the set cannot be partitioned into two subsets with equal sum.

## Leetcode
- [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)
- [698. Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/)