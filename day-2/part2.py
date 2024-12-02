# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict
from itertools import combinations

# Placeholders to be filled when copying the template
PART = 2
DAY = 2
YEAR = 2024

# The expected result from the test input, if using a test input
TEST_RESULT = 4

def safe(ns):
    increasing = np.sign(ns[0] - ns[-1])
    valid = True
    for i in range(len(ns) - 1):
        d = (ns[i] - ns[i + 1]) * increasing
        if d < 1 or d > 3:
            valid = False
            break
    return valid

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    total = 0
    for line in lines:
        ns_full = [int(n) for n in line.split()]
        for ns in combinations(ns_full, len(ns_full) - 1):
            if safe(ns):
                total += 1
                break

    return total

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
