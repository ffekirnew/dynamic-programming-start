# 3. Change-making
## Problem Statement
You are given an unlimited supply of coins of denominations x1, x2, . . . , xn, and a target
amount of money. Write an algorithm that returns a combination of coins of minimum size
that add up to the target amount of money.

### Input Format
The input consists of a single integer n, followed by a line containing n integers, the coin
denominations, and a line containing a single integer, the target amount of money.

### Output Format
The output consists of a list of integers, the denominations of the coins in the optimal
solution.

### Examples
```
Input:
3
1 3 4
6

Output:
3 3
```

## Solutions
### Solution 1: Memoization (Recursive) - Top-Down Dynamic Programming

The time complexity of this solution is O(n * v) for n is the length of the list of coin denominations and v is the target value The space complexity is again O(n * v). The space complexity is O(n * v). The intuition is that if the target is greater than a coin, we can use that coin in its change, reduce the target by the value of the coin, and repeat the process. If the target is less than a coin, we can't use that coin in its change, so we move on to the next coin. We memoize the results of the recursive calls to avoid repeating work. If after a point, the target becomes 0, we return the list we have made. If the target becomes negative, we return None. Then if there are multiple solutions, we pick the shortes one.

### Solution 2: Iterative - Bottom-Up Dynamic Programming
The time complexity of this solution is still
The approach here is to first know the optimal changes to the ammounts we can know easily. Those are, 
        you guessed it, the coin denominations we are given in the first place, i.e. we are sure if given one of
        those ammounts as a target, we can just return the coin in a list. Then we can work our way incrementally to the
        required target starting from these ammounts.
