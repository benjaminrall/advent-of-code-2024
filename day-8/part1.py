# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict
from itertools import combinations

# Placeholders to be filled when copying the template
PART = 1
DAY = 8
YEAR = 2024

# The expected result from the test input, if using a test input
TEST_RESULT = 4

def antinode(positions, bounds):
    total = set()
    for c in combinations(positions, 2):
        a, b = c
        m = (a[0] - b[0], a[1] - b[1])

        p1 = (a[0] + m[0], a[1] + m[1])
        p2 = (b[0] - m[0], b[1] - m[1])
        if p1[0] >= 0 and p1[0] < bounds[0] and p1[1] >= 0 and p1[1] < bounds[1]:
            total.add(p1)
        if p2[0] >= 0 and p2[0] < bounds[0] and p2[1] >= 0 and p2[1] < bounds[1]:
            total.add(p2)
    return total

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    
    frequencies = set()
    positions = defaultdict(lambda : [])
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char != '.':
                frequencies.add(char)
                positions[char].append((i, j))

    bounds = (len(lines), len(lines[0]))
    total = set()
    for f in frequencies:
        total |= antinode(positions[f], bounds)
    print(total)
    return len(total)

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
