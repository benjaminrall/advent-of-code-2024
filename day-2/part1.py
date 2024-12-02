# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 1
DAY = 2
YEAR = 2024

# The expected result from the test input, if using a test input
TEST_RESULT = 2

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    print(lines)

    safe = 0
    for line in lines:
        ns = [int(n) for n in line.split()]
        increasing = np.sign(ns[0] - ns[-1])
        valid = True
        print(ns)
        for i in range(len(ns) - 1):
            d = (ns[i] - ns[i + 1]) * increasing
            print(d)
            if d < 1 or d > 3:
                valid = False
                break
        if valid:
            safe += 1

    return safe

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
