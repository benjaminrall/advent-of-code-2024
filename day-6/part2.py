# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 2
DAY = 6
YEAR = 2024

# The expected result from the test input, if using a test input
TEST_RESULT = 6

def test(grid, start):
    pos = start
    dir = -1
    seen = set()
    while pos in grid and (pos, dir) not in seen:
        seen |= {(pos, dir)}
        if grid.get(pos + dir) == "#":
            dir *= -1j
        else:
            pos += dir
    return {p for p, _ in seen}, (pos, dir) in seen

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = np.array([line.strip() for line in f.readlines()])

    grid = {}
    for y, row in enumerate(lines):
        for x, element in enumerate(row):
            grid[y + x*1j] = element
            if element == '^':
                start = y + x*1j

    path, _ = test(grid, start)
    total = 0
    for candidate in path:
        if test(grid | {candidate: '#'}, start)[1]:
            total += 1

    return total

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
