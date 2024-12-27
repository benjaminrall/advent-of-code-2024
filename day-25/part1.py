# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 1
DAY = 25
YEAR = 2024

# The expected result from the test input, if using a test input
TEST_RESULT = 3

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        schems = f.read().strip().split('\n\n')
    print(schems)
    locks = set()
    keys = set()

    for schem in schems:
        res = []
        data = schem.split('\n')
        for column in zip(*data):
            res.append(len(column) - sum(c == '.' for c in column) - 1)
        if data[0][0] == '.':
            keys.add(tuple(res))
        else:
            locks.add(tuple(res))
    
    total = 0
    for lock in locks:
        for key in keys:
            valid = True
            for x, y in zip(lock, key):
                if x + y >= 6:
                    valid = False
                    break
            if valid:
                total += 1

    return total

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
