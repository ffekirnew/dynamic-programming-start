class NumberOfBinarySearchTreens:
    @staticmethod
    def top_down(n: int) -> int:
        memo = {0: 1}

        def dp(n: int) -> int:
            if n not in memo:
                memo[n] = 0
                for i in range(n):
                    memo[n] += dp(i) * dp(n - i - 1)

            return memo[n]

        return dp(n)

    @staticmethod
    def bottom_up(n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]

        return dp[-1]
