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
            O(n), where n is the length of s2.
        """
        # Initialize the 1D table
        m = len(self.s1)
        n = len(self.s2)
        dp: List[int]= [0] * (n + 1)
        
        max_length = 0  # Length of the longest common substring
        end_index_s1 = 0  # Ending index of the longest common substring in s1
        

        # Fill the DP table
        for i in range(1, m + 1): 
            current:List = [0] * (n + 1) #Creates a new list current of size n+1 initialized with 0. This list is used to store the current row of the DP table.
            for j in range(1, n + 1): 
                if self.s1[i - 1] == self.s2[j - 1]: # Checks if the characters at positions i-1 in s1 and j-1 in s2 are equal.
                    current[j] = dp[j - 1] + 1 # Sets current[j] to the length of the longest common substring ending at these positions (dp[j-1] + 1).
                    
                    temp: int = max_length
                    max_length = max(max_length, current[j]) # Updates max_length if a longer common substring is found.
                    if max_length > temp:
                        #Updates end index to the current position i in s1 if a nex max was found.
                        end_index_s1 = i
                        
                else:
                    current[j] = 0
            dp = current # Updates the dp list to be the current list. Shifts the previous row to the current row for the next iteration -> assuring O(n) space complexity

        # Calculate 1-based start positions
        start_index_s1 = end_index_s1 - max_length + 1
       
        return f"{start_index_s1} {end_index_s1}"





