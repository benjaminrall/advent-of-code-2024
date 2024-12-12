# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 2
DAY = 10
YEAR = 2024

# The expected result from the test input, if using a test input
TEST_RESULT = 81

grid = {}
neighbours = lambda x : [x + 1, x - 1, x + 1j, x - 1j]

def search(start, value, path, paths):
    if value == 9:
        paths.add(tuple(path))
        return
    
    total = 0
    for neighbour in neighbours(start):
        if neighbour not in grid:
            continue

        n = grid[neighbour]
        if n == value + 1:
            search(neighbour, value + 1, path + [neighbour], paths)
    return total

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    global grid
    with open(filename) as f:
        grid = {row + col * 1j: int(e) for row, line in enumerate(f.readlines()) for col, e in enumerate(line.strip())}
    
    starts = [pos for pos in grid if grid[pos] == 0]
    
    total = 0
    for start in starts:
        visited = set()
        search(start, 0, [], visited)
        print(len(visited))
        total += len(visited)

    return total

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
