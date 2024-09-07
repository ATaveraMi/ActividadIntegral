from readFile import read_file
from typing import List

class SubstringFinder:
    def __init__(self, s1: str = "files/transmission1.txt", s2: str = "files/transmission2.txt"):
        
        self.s1:str = read_file(s1)
        self.s2:str = read_file(s2)

    def longest_common_substring(self) -> str:
        """
        Finds the longest common substring between the initialized strings using dynamic programming.

        Returns:
            tuple: A tuple containing the longest common substring, and its 1-based start and end positions in s1 and s2.

        Time Complexity:
            O(n * m), where n is the length of s1 and m is the length of s2.
            This is because the algorithm fills a 2D DP table of size (n+1) x (m+1).

        Space Complexity:
            O(n * m), where n is the length of s1 and m is the length of s2.
            This is due to the space required to store the DP table.
        """
        # Initialize the DP table
        dp: List[int]= [[0] * (len(self.s2) + 1) for _ in range(len(self.s1) + 1)]
        
        max_length = 0  # Length of the longest common substring
        end_index_s1 = 0  # Ending index of the longest common substring in s1
        end_index_s2 = 0  # Ending index of the longest common substring in s2

        # Fill the DP table
        for i in range(1, len(self.s1) + 1):
            for j in range(1, len(self.s2) + 1):
                if self.s1[i - 1] == self.s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    if dp[i][j] > max_length:
                        max_length = dp[i][j]
                        end_index_s1 = i
                        
                else:
                    dp[i][j] = 0

        # Calculate 1-based start positions
        start_index_s1 = end_index_s1 - max_length + 1
       
        return f"{start_index_s1} {end_index_s1}"





