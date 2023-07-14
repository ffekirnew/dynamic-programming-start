from collections import defaultdict, deque
from typing import List


class SplittingAStringWithoutSpacesIntoWords:
    @staticmethod
    def top_down(sentence: str, dictionary: List[str]) -> bool:
        memo = {}

        def dp(starting_index: int, index: int):
            if index == len(sentence):
                return starting_index == index

            if (starting_index, index) not in memo:
                memo[(starting_index, index)] = False

                for word in dictionary:
                    if word == sentence[starting_index: index + 1]:
                        memo[(starting_index, index)] |= dp(
                            index + 1, index + 1)

                memo[(starting_index, index)] |= dp(starting_index, index + 1)

            return memo[(starting_index, index)]

        return dp(0, 0)
