# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 2
DAY = 9
YEAR = 2024

# The expected result from the test input, if using a test input
TEST_RESULT = 2858

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        data = [list(map(int, line.strip())) for line in f.readlines()][0]
    
    disk = []
    parts = []
    gaps = []
    empty = False
    id = 0
    i = 0
    L = 0
    for digit in data:
        for j in range(digit):
            if not empty:
                disk.append(id)
                L += 1
                if j == 0:
                    parts.append((i, digit, id))
            else:
                disk.append(-1)
                if j == 0:
                    gaps.append((i, digit))
            i += 1
        if not empty:
            id += 1
        empty = not empty

    for part in parts[::-1]:
        for i, gap in enumerate(gaps):
            if gap[0] < part[0] and part[1] <= gap[1]:
                for j in range(gap[0], gap[0] + part[1]):
                    disk[j] = part[2]
                for j in range(part[0], part[0] + part[1]):
                    disk[j] = -1
                if gap[1] == part[1]:
                    gaps.remove(gap)
                else:
                    gaps[i] = (gap[0] + part[1], gap[1] - part[1])
                break

    return sum([i * j for i,j in enumerate(disk) if j != -1])  

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
