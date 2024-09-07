# String Matching Algorithms

## Overview

**String Matching Algorithms** is a project that includes several string matching and substring finding algorithms, implemented to enhance pattern matching capabilities. The main functionalities of the project are encapsulated in various classes, each focusing on a specific algorithm such as the Knuth-Morris-Pratt (KMP) algorithm, the Manacher's algorithm, and the Longest Common Substring using Dynamic Programming.

## Features

- **File Reading**: Reads content from files to be used for pattern matching and substring search.
- **LPS Calculation**: Computes the Longest Prefix Suffix (LPS) array used in the KMP algorithm.
- **Pattern Matching**: Finds whether a pattern (`mcode`) exists in a given transmission (`transmission`) file using the KMP algorithm.
- **Longest Common Substring**: Finds the longest common substring between two strings using Dynamic Programming.
- **Manacher's Algorithm**: Efficiently finds the longest palindromic substring in a given string in linear time.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/ATaveraMi/ActividadIntegral.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd ActividadIntegral
   ```

## Usage

### 1. **Run Pattern Matching with KMP Algorithm**:

Ensure you have your `transmission` and `mcode` text files ready. You can use the `find_pattern_in_transmission` method from the `LPS` class to check if the content of `mcode` is present in `transmission`.

```python
from LongestPrexixSuffix import LPS

lps_instance = LPS()
result = lps_instance.find_pattern_in_transmission("transmission.txt", "mcode.txt")
print(result)  # Output: True or False
```

### 2. **Find the Longest Common Substring**:

Use the `longest_common_substring_positions` function to find the starting positions of the longest common substring between two strings.

```python
from LongestCommonSubstring import longest_common_substring_positions

s1 = "banana" #for example
s2 = "ananas" #for example
positions = longest_common_substring_positions(s1, s2)
print(f"Starting positions of the longest common substring in s1: {positions}")
```

### 3. **Run Manacher's Algorithm**:

Use the `Manacher` class to find the longest palindromic substring in a given transmission file.

```python
from Manacher import Manacher

manacher_instance = Manacher()
longest_palindrome = manacher_instance.longest_palindromic_substring("transmission.txt")
print(f"Longest palindromic substring: {longest_palindrome}")
```

### 4. **Example Test Cases**:

- `test_lps.py` includes example test cases to verify the functionality of the KMP pattern matching implementation.
- `test_longest_common_substring.py` includes test cases to check the correctness of the longest common substring function.
- `test_manacher.py` includes test cases to verify the correctness of Manacher's algorithm for finding palindromic substrings.
