class FibonaccciSequence:
    def brute_force(self, n: int) -> int:
        if n in [0, 1]:
            return 1
        return self.brute_force(n - 1) + self.brute_force(n - 2)

    def top_down(self, n: int) -> int:
        fibonacci_cache = {0: 1, 1: 1}
        def fibonacci(n: int) -> int:
            if n not in fibonacci_cache:
                fibonacci_cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

            return fibonacci_cache[n]

        return fibonacci(n)

    def bottom_up(self, n: int) -> int:
        if n in [0, 1]:
            return 1

        first_number, second_number = 1, 1
        for index in range(3, n):
            first_number, second_number = second_number, first_number + second_number

        return first_number + second_number


if __name__ == "__main__":
    solution = FibonaccciSequence()
    print(solution.brute_force(5))
    print(solution.top_down(5))
    print(solution.bottom_up(5))
