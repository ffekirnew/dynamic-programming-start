# 2. Optimal stock market strategy

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

### Solution 1: Memoization (Recursive) - Top-Down Dynamic Programming

The time complexity of this solution is O(n), and the space complexity is O(n). The intuition is a stock can be bought, sold or left untouched on any given day. We have a list of prices on different days for the given stock. Choose to do all three actions on each day - play out every scenario - then decide which one gives the maximum profit.

### Solution 2: Iterative - Bottom-Up Dynamic Programming

The third solution is an iterative solution that uses bottom-up dynamic programming. This
solution is the most efficient because it avoids recursion and memoization. The time
complexity of this solution is O(n), and the space complexity is O(1). The appraoch here is to keep track of out states in variables and update them as we iterate through the list of prices. We keep track of our money on hand with stock and with out stock and update them as we iterate through the list of prices.

## Similar Problems on Different Platforms

- [LeetCode - Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
