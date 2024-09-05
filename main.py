from typing import List

class FirstProblem:

    def read_file(self, filename: str) -> str:
        """
        This function reads a file and if there is one

        Returns:
            str: file content
        """
        try:
            with open(filename, 'r') as file:
                content: str = file.read().replace('\n', '')  
                return content
            
        except FileNotFoundError:
            print(f"Error: file '{filename}' not found")
            return ""
    
    def calculate_prefix_length(self, pattern: str) -> List[int]:
        """THis function returns the lps of a string

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
        transmission: str = self.read_file(transmission)
        mcode: str = self.read_file(mcode)
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
            
        
                
print(FirstProblem().find_pattern_in_transmission("transmission1.txt", "mcode1.txt"))
                
            
# transmission1 = FirstProblem().read_file('transmission1.txt')
# transmission2 = FirstProblem().read_file('transmission2.txt')
# mcode1 = FirstProblem().read_file('mcode1.txt')
# mcode2 = FirstProblem().read_file('mcode2.txt')
# mcode3 = FirstProblem().read_file('mcode3.txt')