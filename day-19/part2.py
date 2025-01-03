# Useful imports
import math
import numpy as np
from functools import cache

# Placeholders to be filled when copying the template
PART = 2
DAY = 19
YEAR = 2024

# The expected result from the test input, if using a test input
TEST_RESULT = 16



# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    patterns = lines[0].split(', ')
    total = 0

    
    @cache
    def possible(target: str):
        if len(target) == 0:
            return 1
        
        total = 0
        for pattern in patterns:
            if target.startswith(pattern):
                total += possible(target[len(pattern):])
 
        return total


    for i, case in enumerate(lines[2:]):
        total += possible(case)
        print(f"Completed case {i + 1}/{len(lines[2:])}")

    return total

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
