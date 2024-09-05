import pytest
from LongestPrexixSuffix import LPS  

# Create an instance of the LPS class
lps_instance = LPS()

def test_find_pattern_in_transmission_case1():
    assert lps_instance.find_pattern_in_transmission("transmission1.txt", "mcode1.txt") == True 

def test_find_pattern_in_transmission_case2():
    assert lps_instance.find_pattern_in_transmission("transmission1.txt", "mcode2.txt") == True  
def test_find_pattern_in_transmission_case3():
    assert lps_instance.find_pattern_in_transmission("transmission1.txt", "mcode3.txt") == False  

def test_find_pattern_in_transmission_case4():
    assert lps_instance.find_pattern_in_transmission("transmission2.txt", "mcode1.txt") == False  

def test_find_pattern_in_transmission_case5():
    assert lps_instance.find_pattern_in_transmission("transmission2.txt", "mcode2.txt") == False  

def test_find_pattern_in_transmission_case6():
    assert lps_instance.find_pattern_in_transmission("transmission2.txt", "mcode3.txt") == True  

if __name__ == "__main__":
    
    pytest.main()