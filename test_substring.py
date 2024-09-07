import pytest
from SubstringFinder import SubstringFinder 

# Create an instance of the LPS class
substring_instance = SubstringFinder("files/transmission1.txt", "files/transmission2.txt")

def test_find_lcs():
    assert substring_instance.longest_common_substring() == "1 69" 


if __name__ == "__main__":
    
    pytest.main()