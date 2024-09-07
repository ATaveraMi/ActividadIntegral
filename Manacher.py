from readFile import read_file
from typing import List

class Manacher:
    def manacher(self, transmission: str)->str:
        """Finds the longest palindromic substring within the given transmission file using Manacher's algorithm.

        Manacher's algorithm is an efficient method to find the longest palindromic substring in linear time.
        The function reads the content of the transmission file and processes it to identify the longest palindrome.

        Time Complexity:
            O(n), where n is the length of the content in the transmission file.
            The algorithm runs in linear time due to the way it expands around potential palindrome centers.

        Space Complexity:
             O(n), where n is the length of the transmission.
             Additional space is used for the 'palindrome' list, which stores the radius of the palindrome around each character.

        Args:
            transmission (str): The path to the text file containing the transmission data.

        Returns:
            str: A string representing the starting and ending indices (1-based indexing) of the longest palindromic substring in the transmission.
        """
        self.transmission: str = read_file(transmission)
        
        # Create a new list to store the maximum palindromic length at each index
        palindrome: List[int] = [0] * len(self.transmission)
        
        center: int = 0
        right: int = 0
        
        for idx in range(len(self.transmission)):
            mirror: int = 2 * center - idx
            
            # If idx is within the right boundary, we can use the mirrored value
            if idx < right:
                palindrome[idx] = min(right - idx, palindrome[mirror])
            
            # Expand around the current center idx
            while (idx + palindrome[idx] + 1 < len(self.transmission)) and (idx - palindrome[idx] - 1 >= 0) and (self.transmission[idx + palindrome[idx] + 1] == self.transmission[idx - palindrome[idx] - 1]):
                palindrome[idx] += 1
            
            # Update center and right boundary if the palindrome expands beyond the right boundary
            if idx + palindrome[idx] > right:
                center = idx
                right = idx + palindrome[idx]
        
        # Find the longest palindrome in the list
        max_length = max(palindrome)
        center_index = palindrome.index(max_length)
        
        # Calculate the starting and ending indices of the longest palindromic substring
        start = center_index - max_length +1
        end = center_index + max_length +1
        

        
        
        return f"{start} {end}"
