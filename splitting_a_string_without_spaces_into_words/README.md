# 6. Splitting a String Without Spaces Into Words
## Problem Statement
Given a string containing words without spaces, and a dictionary of words determine if the input string can be split into valid words.

### Input Format
A string containing words without spaces and a set of words.

### Output Format
A boolean value indicating if the input string can be split into valid words.

## Examples
### Example 1
```
Input:
"applepie"
{"apple", "pie"}

Output:
True
```

### Example 2
```
Input:
"applepeer"
{"apple", "pie"}

Output:
False
```

## Constraints
* The input string will only contain lowercase letters.
* The dictionary will only contain lowercase letters.
* The dictionary will contain a maximum of 1000 words.
* The input string will be at most 20 characters long.

## Solution
### Solution 1: Top Down Dynamic Programming (Time Complexity: O(n^2), Space Complexity: O(n))
The idea is to use two indices. One to indicate the starting of a possible word, a second one for the end. If the substring between the two indices is a valid word in the dictionary, then we recursively check if the rest of the string can be split into valid words, effectively solving a smaller problem. If the substring is not a valid word, then we move the end index one character to the right and check again. If the end index reaches the end of the string, there could be two outcomes. If at the end the two indices are equal, it means we have processed the entire sentence by splitting it into valid words. If the two indices are not equal, it means we have reached the end of the string without being able to split it into valid words.

## Leetcode
- [139. Word Break](https://leetcode.com/problems/word-break/)
- [140. Word Break II](https://leetcode.com/problems/word-break-ii/)