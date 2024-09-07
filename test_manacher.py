import pytest
from Manacher import Manacher 

# Create an instance of the LPS class
manacher_instance = Manacher()

def test_longest_palindrome_case1():
    assert manacher_instance.manacher("files/transmission1.txt") == "624 662" 
def test_longest_palindrome_case2():
    assert manacher_instance.manacher("files/transmission2.txt") == "1 7" 
    


if __name__ == "__main__":
    
    pytest.main()