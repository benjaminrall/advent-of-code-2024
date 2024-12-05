# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 1
DAY = 3
YEAR = 2024

# The expected result from the test input, if using a test input
TEST_RESULT = 161

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        line = ''.join([line.strip() for line in f.readlines()])
    
    total = 0
    i = 0
    while (ci_start := line.find('mul(', i)) != -1:
        i = ci_start + 4
        if (ci_end := line.find(')', ci_start)) == -1:
            break
        candidate = line[ci_start+4:ci_end].split(',')
        if len(candidate) != 2:
            continue
        try:
            if candidate[0].strip() != candidate[0]:
                continue
            if candidate[1].strip() != candidate[1]:
                continue
            result = int(candidate[0]) * int(candidate[1])
        except:
            continue
        print(line[ci_start:ci_end+1])
        total += result

    return total

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
