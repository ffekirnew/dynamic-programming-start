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
                if is_palindrome(i, j) and j - i + 1 > longest[1] - longest[0] + 1:
                    longest = (i, j)
        
        return string[longest[0] : longest[1] + 1]
    
    @staticmethod
    def top_down():
        pass



if __name__ == "__main__":
    solution = LongestPalindromicSubstring()

    print(solution.brute_force("forgeeksskeegfor"))