from readFile import read_file
from typing import List

class Manacher:
    def manacher(self, transmission: str)->str:
        """_summary_

        Args:
            transmission (str): _description_

        Returns:
            _type_: _description_
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
# Assuming the transmission file is named 'transmission.txt'
manacher_solver = Manacher()
index = manacher_solver.manacher('transmission1.txt')

# Output will display the indices and you can use them to extract the substring if needed
print(f"{index}")
