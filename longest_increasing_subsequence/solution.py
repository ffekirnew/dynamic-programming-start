from typing import List


class LongestIncreasingSubsequence:
    @staticmethod
    def bottom_up(sequence: List[int]) -> int:
        longest_ending_at = [1 for index in range(len(sequence))]

        for index in range(len(sequence)):
            for other_number_index in range(0, index):
                if sequence[index] > sequence[other_number_index]:
                    longest_ending_at[index] = max(
                        longest_ending_at[index],
                        longest_ending_at[other_number_index] + 1,
                    )

        return max(longest_ending_at)


if __name__ == "__main__":
    solution = LongestIncreasingSubsequence()

    print(solution.bottom_up([3, 6, 9, 12]))
    print(solution.bottom_up([9, 4, 7, 2, 10]))
