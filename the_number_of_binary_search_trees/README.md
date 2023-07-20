# 7. The Number of Binary Search Trees
## Problem Statement
Given an integer `n`, return the number of structurally unique binary search trees that store values `1` to `n`.

### Input Format
An integer `n`.

### Output Format
An integer representing the number of structurally unique binary search trees that store values `1` to `n`.

## Examples
### Example 1
```
Input:
3

Output:
5
```

### Example 2
```
Input:
4

Output:
14
```

## Constraints
* `1 <= n <= 19`

## Solutions
### Solution 1: Top-Down Dynamic Programming (Time Complexity: O(n<sup>2</sup>), Space Complexity: O(n))
To work on this problem, we first need to understand that whatever the number values we thin for the nodes in the tree, the number of unique binary search trees is the same. For example, the number of unique binary search trees with 3 nodes: [1, 2, 3] is the same as a BST of 3 nodes but the nodes are [500, 900, 1000]. This is because the number of unique binary search trees is only dependent on the number of nodes in the tree, not the values of the nodes.
1         1          2          3          3
 \         \        / \        /          /
  2         3      1   3      1          2
   \       /                   \        /
    3     2                     2      1

500      500        900       1000        1000
 \         \        / \        /          /
  900      1000  500   1000   500       900
   \       /                   \        /
    1000  900                   900    500

Both 5 ways. So now what matters is what the root is. And that affects the final number in such a way that what we choose as the root determines what we can have in the children. So if we pick the smallest number as the root, then all the other nodes will go to it's right and that's the way, we can solve a smaller problem concerning those new nodes only until we get down to zero. If we pick a bit centeral number as the root, then some will go to left, some will go to right. Then we can solve the smaller problem have the product of the two. And we can do this for all the numbers and add them up to get the final answer.

### Solution 2: Bottom-Up Dynamic Programming (Time Complexity: O(n<sup>2</sup>), Space Complexity: O(n))
This is just rewriting the top-down solution as a bottom-up solution. The idea is the same, but the implementation is different.

## LeetCode
- [96. Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees)
- [95. Unique Binary Search Trees II](https://leetcode.com/problems/unique-binary-search-trees-ii)