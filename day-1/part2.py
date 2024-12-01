# Useful imports
import math
import numpy as np
from functools import cache
from collections import Counter

# Placeholders to be filled when copying the template
PART = 2
DAY = 1
YEAR = 2024

# The expected result from the test input, if using a test input
TEST_RESULT = 31

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        lines = [line.strip().split() for line in f.readlines()]
    
    l1 = [int(line[0]) for line in lines]
    l2 = [int(line[1]) for line in lines]

    l1.sort()
    c = Counter(l2)

    total = 0
    for e in l1:
        total += e * c[e]

    # --- SOLUTION CODE ---
    return total

if __name__ == "__main__":	
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
