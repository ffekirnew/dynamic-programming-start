# 2 Optimal stock market strategy

## Problem Statement
When evaluating stock market trading strategies, it is useful to determine the maximum pos-
sible profit that can be made by trading a certain stock. Write an algorithm that, given the
daily price of a stock, computes the maximum profit that can be made by buying and selling
that stock. Assume that you are allowed to own no more than 1 share at any time, and that
you have an unlimited budget.

### Input Format
The input consists of a single integer n, followed by a line containing n integers, the daily
price of the stock.

### Output Format
The output consists of a single integer, the maximum profit that can be made by buying and
selling the stock.

### Examples
```
Input: 
3
2 5 1

Output:
3
```

Example 2:
```
Input:
4
2 5 1 3

Output:
5
```

## Solutions
I have provided three solutions, each of which is in a separate file. The first solution is
### Solution 1: Brute Force (Recursive)
The first solution is a brute force solution that uses recursion. This solution is the most
straightforward, but it is also the least efficient. The time complexity of this solution is
O(2^n), and the space complexity is O(n).

### Solution 2: Memoization (Recursive) - Top-Down Dynamic Programming
The second solution is a recursive solution that uses memoization. This solution is more
efficient than the first solution because it avoids recomputing the same values. The time
complexity of this solution is O(n), and the space complexity is O(n).

### Solution 3: Iterative - Bottom-Up Dynamic Programming
The third solution is an iterative solution that uses bottom-up dynamic programming. This
solution is the most efficient because it avoids recursion and memoization. The time
complexity of this solution is O(n), and the space complexity is O(1).


## Similar Problems on Different Platforms
- [LeetCode - Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

