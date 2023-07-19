class NumberOfWaysToClimbStairs:
    @staticmethod
    def top_down(n: int) -> int:
        if n <= 0:
            return 0
        if n < 2:
            return 1

        memo = {}

        def dp(n: int):
            if n <= 0:
                return n == 0

            if n not in memo:
                memo[n] = dp(n - 1) + dp(n - 2)
            
            return memo[n]
        
        return dp(n)
    
    @staticmethod
    def bottom_up(n: int) -> int:
        if n <= 0:
            return 0
        if n < 2:
            return 1

        ways = [0] * (n + 1)
        ways[0] = ways[1] = 1

        for i in range(2, n + 1):
            ways[i] = ways[i - 1] + ways[i - 2]
        
        return ways[n]
    