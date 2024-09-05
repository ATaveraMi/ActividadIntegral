<em> # Actividad Integreal</em>

## Overview

**ActividadIntegral** is a project that includes a pattern matching algorithm implemented using the Knuth-Morris-Pratt (KMP) algorithm. The main functionalities of the project are encapsulated in the `LPS` class, which provides methods for reading files, calculating the Longest Prefix Suffix (LPS) array, and finding patterns within transmission data.

## Features

- **File Reading**: Reads content from files to be used for pattern matching.
- **LPS Calculation**: Computes the Longest Prefix Suffix (LPS) array used in KMP algorithm.
- **Pattern Matching**: Finds whether a pattern (mcode) exists in a given transmission file using the KMP algorithm.

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

1. **Run the Script**:

    Ensure you have your `transmission` and `mcode` text files ready. You can use the `find_pattern_in_transmission` method from the `LPS` class to check if the content of `mcode` is present in `transmission`.

    ```python
    from LongestPrexixSuffix import LPS
    
    lps_instance = LPS()
    result = lps_instance.find_pattern_in_transmission("transmission.txt", "mcode.txt")
    print(result)  # Output: True or False
    ```

2. **Example Test Cases**:

    - `test_lps.py` includes example test cases to verify the functionality of the KMP pattern matching implementation.

