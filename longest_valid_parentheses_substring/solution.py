class LongestValidParenthesisSubstring:
    @staticmethod
    def bottom_up(string: str) -> int:
        longest_valid_parenthesis_length = 0
        longest_ending_at = [0] * len(string)

        for index, char in enumerate(string):
            if char == "(" or index == 0:
                continue

            if (
                string[index - 1] == "("
            ):  # we are making a simple valid parenthesis where the ( is right before )
                longest_ending_at[index] = 2

                # Try to combine it with a previous substring
                if index - 1 > 0:
                    longest_ending_at[index] += longest_ending_at[index - 2]

                longest_valid_parenthesis_length = max(
                    longest_valid_parenthesis_length, longest_ending_at[index]
                )
                continue

            # Get the length of the substring ending at right before the index
            prev_substring_length = longest_ending_at[index - 1]

            # we are trying to sandwich it, so find the opening match
            index_of_match = index - prev_substring_length - 1
            if index_of_match >= 0 and string[index_of_match] == "(":
                longest_ending_at[index] = longest_ending_at[index - 1] + 2

                # if we succeedes in making the sandwich, try and combine it with another substring before
                if index_of_match > 0:
                    longest_ending_at[index] += longest_ending_at[index_of_match - 1]

            longest_valid_parenthesis_length = max(
                longest_valid_parenthesis_length, longest_ending_at[index]
            )

        return longest_valid_parenthesis_length


if __name__ == "__main__":
    solution = LongestValidParenthesisSubstring()

    # print(solution.bottom_up('()()()((()))'))
    print(solution.bottom_up("(()))())("))
