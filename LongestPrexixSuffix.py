from typing import List
from readFile import read_file
class LPS:

    
    def calculate_prefix_length(self, pattern: str) -> List[int]:
        """THis function returns the lps of a string
        
        Time Complexity: O(n) -> iterates through the pattern once with the for loop.
        Space Complexity: O(n) -> The space used is proportional to the length of the pattern for storing the LPS array.

        Args:
            pattern (str): a string -> the pattern to be studied

        Returns:
            List[int]: The LPS of the string
        """
        if pattern == "": return []
        prefix_length_list: List[int] = [0] * len(pattern)
        prefix_length_list[0] = 0
        current_length: int = 0  # Length of the longest prefix suffix
        for idx in range(1,len(pattern)):
            #Checks to see whether we can backtrack to our last lps or if it should start from 0
            while current_length >0 and pattern[idx] != pattern[current_length]:
                current_length = prefix_length_list[current_length - 1]
                
            if pattern[idx] == pattern[current_length]:
                current_length += 1
                prefix_length_list[idx] = current_length 
            
            else: 
                prefix_length_list[idx] = 0
                  
        return  prefix_length_list
    
    def find_pattern_in_transmission(self, transmission:str, mcode:str)->bool:
        """
    This function takes two files and checks if the content of the mcode file is present within the transmission file
    using the KMP (Knuth-Morris-Pratt) pattern matching algorithm.

    Time Complexity: O(n + m)
        where m is the length of mcode and n is the length of transmission.
        The time complexity is linear with respect to the length of both the transmission and mcode files. This includes
        the time to compute the LPS (Longest Prefix Suffix) array and to perform the pattern matching.

    Space Complexity: O(m)
        where m is the length of mcode.
        The primary additional space used is for the LPS array, which has a size proportional to the length of the mcode.

    Args:
        transmission (str): The path to the file containing the text to search through.
        mcode (str): The path to the file containing the pattern to search for in the transmission.

    Returns:
        bool: True if the pattern (mcode) is found within the transmission; False otherwise.
        """
        transmission: str = read_file(transmission)
        mcode: str = read_file(mcode)
        lps: List[int] = self.calculate_prefix_length(mcode)
        
        ptr_t: int = 0 #transmission ptr
        ptr_m: int = 0 #mcode ptr
        
        while ptr_t < len(transmission):
            if transmission[ptr_t] == mcode[ptr_m]:
                ptr_t+=1
                ptr_m+=1
                
            elif ptr_m == 0:
                ptr_t +=1
                
            else:
                ptr_m = lps[ptr_m-1] 
                
            if ptr_m == len(mcode):
                    return True
                
                
        return False
            
        
  