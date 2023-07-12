# 1. The Fibonacci sequence

## Problem Statement
Return the n-th number in the Fibonacci sequence. The first two numbers in the Fibonacci
sequence are equal to 1; any other number is equal to the sum of the preceding two numbers.

The Fibonacci sequence is defined as follows:
```
F(0) = 1
F(1) = 1
F(n) = F(n-1) + F(n-2)
```

### Input Format
The input consists of a single integer n.

### Output Format
The output should be a single integer, the n-th number in the Fibonacci sequence.

### Example
```
Input:
5

Output:
8
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

