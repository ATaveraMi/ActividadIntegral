import pytest
from SubstringFinder import SubstringFinder 

# Create an instance of the LPS class
substring_instance = SubstringFinder("transmission1.txt", "transmission2.txt")

def test_find_pattern_in_transmission_case1():
    assert substring_instance.longest_common_substring() == "1 69" 


if __name__ == "__main__":
    
    pytest.main()