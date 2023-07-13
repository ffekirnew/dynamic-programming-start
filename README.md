# Dynamic Programming Start
This github repository is for the study of dynamic programming through the book `Programming Interview Problems: Dynamic Programming` by <b>Leonardo Rossi</b> and beyond. The book contains 25 problems and their solutions. The book also provides the solutions in python if you wanted to check the original solutions. It also goes in deeper in explaining them (problems and solutions). In this repository, though, I will also link Leetcode problems that are similar to the problems in the book and can be easily solved with a copy-paste afterwards or a little bit of modification. I will also provide my own solutions to the problems and will try to provide as many solutions as possible.

### Table of Contents
- [Dynamic Programming Start](#dynamic-programming-start)
    - [Table of Contents](#table-of-contents)
    - [Problems Covered](#problems-covered)
    - [Usage](#usage)
    - [Contribution](#contribution)
    - [References](#references)
    - [Author](#author)
    - [License](#license)

## Problems Covered
- [x] [Problem 1: Fibonacci Numbers](the_fibonacci_sequence)
- [X] [Problem 2: Optimal Stock Market Strategy](optimal_stock_market_strategy)
- [X] [Problem 3: Change Making](change_making)
- [ ] [Problem 4: Number of Expressions with a target Result](number_of_expressions_with_a_target_result)
- [ ] [Problem 5: Partitioning a set into equal-sum parts](partitioning_a_set_into_equal_sum_parts)
- [ ] [Problem 6: Splitting a string without spaces into words](splitting_a_string_without_spaces_into_words)
- [ ] [Problem 7: The number of binary search trees](the_number_of_binary_search_trees)
- [ ] [Problem 8: The maximum-sum subarray](the_maximum_sum_subarray)
- [ ] [Problem 9: The maximum-product subarray](the_maximum_product_subarray)
- [ ] [Problem 10: Shortest pair of subarrays with target sum](shortest_pair_of_subarrays_with_target_sum)
- [X] [Problem 11: Longest palindromic substring](longest_palindromic_substring)
- [X] [Problem 12: Longest valid parentheses substring](longest_valid_parentheses_substring)
- [X] [Problem 13: Longest increasing subsequence](longest_increasing_subsequence)
- [X] [Problem 14: Longest arithmetic subsequence](longest_arithmetic_subsequence)
- [ ] [Problem 15: Dealing the best hand of cards](dealing_the_best_hand_of_cards)
- [ ] [Problem 16: Number of ways to climb stairs](number_of_ways_to_climb_stairs)
- [ ] [Problem 17: Number of paths through maze](number_of_paths_through_maze)
- [ ] [Problem 18: Maximum-score path through maze](maximum_score_path_through_maze)
- [ ] [Problem 19: Subarray sum](subarray_sum)
- [ ] [Problem 20: Submatrix sum](submatrix_sum)
- [ ] [Problem 21: Largest square submatrix of ones](largest_square_submatrix_of_ones)
- [ ] [Problem 22: Largest rectangle in skyline](largest_rectangle_in_skyline)
- [ ] [Problem 23: Largest submatrix of ones](largest_submatrix_of_ones)
- [ ] [Problem 24: Interleaved strings](interleaved_strings)
- [ ] [Problem 25: Regular expression matching](regular_expression_matching)

## Usage
Each problem is contained in a folder with the same name as the problem. The folder contains a `README.md` file and a `solution.py` file. The `README.md` file contains the problem description and the solution description(s). The solution file contains a class with the same name as the problem and consequent class methods for different solutions that all receive the input and return the output. The input and output are described in the problem description.

A typical problem folder looks like this, sut some of them might have a unittest file too:
```sh
.
├── problem_name
│   ├── README.md
│   └── solution.py
```

A typical `README.md` file looks like this:
```markdown
# Problem Name
## Problem description
    ...
## Solutions
    ...
## Leetcode
    ...
```


And a typical solution file looks like this:
```python
class ProblemName:
    def solution_1(self, input):
        # Solution 1
        return output

    def solution_2(self, input):
        # Solution 2
        return output
```

## Contribution
If you want to contribute to this repository, you can fork this repository and create a pull request with your solution. The solution must be in the `solution.py` file and the problem description must be in the `README.md` file. The solution must be in the same format as the other solutions. If you would like me to attempt a problem, you can create an issue with the problem name and description.

## References
- [Programming Interview Problems: Dynamic Programming](https://www.amazon.com/Programming-Interview-Problems-Dynamic-solutions-ebook/dp/B08RRQWV21) ©️ 2020 <b>Leonardo Rossi</b>.

The first 25 problems in this repository are from the book. The solutions are mine. But, of course, might ocassionally be very similar to the ones on the book, since we are both going for many and efficient algorithms and there are only so many of those for a particular problem.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
