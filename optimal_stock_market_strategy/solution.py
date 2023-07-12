from math import inf
from typing import List


class OptimalStockMarketStrategy:
    def top_down(self, prices: List[int]) -> int:
        stock_cache = {}
        def get_max_profit(day: int, stock_on_hand: int) -> int:
            if day == len(prices):
                return 0

            if (day, stock_on_hand) not in stock_cache:
                do_nothing_today = get_max_profit(day + 1, stock_on_hand)

                if stock_on_hand:
                    involve_in_transaction = get_max_profit(day + 1, stock_on_hand=0) + prices[day]
                else:
                    involve_in_transaction = get_max_profit(day + 1, stock_on_hand=1) - prices[day]
                
                stock_cache[(day, stock_on_hand)] = max(do_nothing_today, involve_in_transaction)

            return stock_cache[(day, stock_on_hand)]
        
        return get_max_profit(0, 0)
    
    def bottom_up(self, prices: List[int]) -> int:
        cash_without_stock = 0
        cash_with_stock = -inf

        for price in prices:
            buy_new_stock = cash_without_stock - price
            avoid_new_stock = cash_without_stock

            sell_stock = cash_with_stock + price
            hold_on_to_stock = cash_with_stock

            cash_without_stock = max(avoid_new_stock, sell_stock)
            cash_with_stock = max(hold_on_to_stock, buy_new_stock)
        
        return cash_without_stock

    
if __name__ == "__main__":
    solution = OptimalStockMarketStrategy()
    # Testing top down solution
    print(solution.top_down([2, 5, 1]))
    print(solution.top_down([2, 5, 1, 3]))

    # Testing bottom up solution
    print(solution.bottom_up([2, 5, 1]))
    print(solution.bottom_up([2, 5, 1, 3]))



