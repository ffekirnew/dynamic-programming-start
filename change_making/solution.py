from typing import List


class ChangeMaking:
    def top_down(self, coins: List[int], target: int) -> List[int]:
        cache = {0: []}
        def dp(target):
            if target < 0:
                return

            if target not in cache:
                optimal_change = None
                for coin in coins:
                    partial_result = dp(target - coin) # solve the subproblem here

                    if partial_result == None:
                        continue

                    possible_solution = partial_result + [coin]
                    if not optimal_change or len(optimal_change) > len(possible_solution):
                        optimal_change = possible_solution
                
                cache[target] = optimal_change
            
            return cache[target]

        return dp(target)

    def bottom_up(self, coins: List[int], target: int) -> List[int]:
        optimal_changes = {coin: [coin] for coin in coins}
        for money_point in range(1, target + 1):
            for coin in coins:
                if money_point > coin:
                    change_using_coin = optimal_changes[coin] + optimal_changes[money_point - coin]

                    if money_point not in optimal_changes or len(optimal_changes[money_point]) > len(change_using_coin):
                        optimal_changes[money_point] = change_using_coin

        return optimal_changes[target]


if __name__ == "__main__":
    solution = ChangeMaking()

    print(solution.top_down([1, 2, 5], 9))
    print(solution.bottom_up([1, 2, 5], 9))
