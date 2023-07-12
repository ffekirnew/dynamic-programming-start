# 13. Longest Increasing Subsequence
## Problem Statement
Given an array A of integers, return the length of the longest monotonically increasing subsequence in A.

### Input Format
The first and the only argument of input contains an integer array, A.

### Output Format
Return an integer representing the length of the longest arithmetic subsequence in A.

### Examples
#### Example 1:
```
Input:
[3, 6, 9, 12]

Output:
4
```

#### Example 2:
```
Input:
[9, 4, 7, 2, 10]

Output:
3
```

## Solutions
### Solution 1: Bottom-up Dynamic Programming
It's time complexity is O(n^2) and space complexity is O(n) - n being the length of the input sequence. The intuition for this solution is, at any index we can either start a new increasing subsequence or we can try and find other subsequences we have built in the past and extend them. So in our dp, we can keep what was the length of the longest subsequence that can be built with the number in the current index included. The when we move on to the next indices, we can look at previous indexes and their longest increasing subsequence lengths and see if we can extend it and so on.

