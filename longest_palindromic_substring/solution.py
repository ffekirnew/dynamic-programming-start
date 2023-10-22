class LongestPalindromicSubstring:
    @staticmethod
    def brute_force(string: str) -> str:
        def is_palindrome(starting_index, ending_index) -> bool:
            while starting_index < ending_index:
                if string[starting_index] != string[ending_index]:
                    return False

                starting_index += 1
                ending_index -= 1

            return True

        longest = (0, 0)
        for i in range(len(string)):
            for j in range(i + 1, len(string)):
                if is_palindrome(i, j) and j - i > longest[1] - longest[0]:
                    longest = (i, j)

        return string[longest[0] : longest[1] + 1]

    @staticmethod
    def dp_1(string: str) -> str:
        # The helper functions
        def palindrome_pad(s: str) -> str:
            assert "!" not in s
            return "!".join(s)

        def palindrome_unpad(padded: str) -> str:
            return padded.replace("!", "")

        string = palindrome_pad(string)
        longest_palindrome = ""

        for center in range(len(string)):
            left, right = center, center

            while left >= 0 and right < len(string) and string[left] == string[right]:
                left -= 1
                right += 1

            left += 1
            right -= 1

            possible_solution = palindrome_unpad(string[left : right + 1])

            if len(possible_solution) > len(longest_palindrome):
                longest_palindrome = possible_solution

        return longest_palindrome

    @staticmethod
    def top_down():
        pass


if __name__ == "__main__":
    solution = LongestPalindromicSubstring()

    print(solution.brute_force("forgeeksskeegfor"))
    print(solution.dp_1("forgeeksskeegfor"))
    print(solution.dp_1("aba"))
