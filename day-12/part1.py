# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 1
DAY = 12
YEAR = 2024

# The expected result from the test input, if using a test input
TEST_RESULT = 1930

def neighbours(row, col, shape):
    if row > 0:
        yield (row - 1, col)
    if col > 0:
        yield(row, col - 1)
    if row < shape[0] - 1:
        yield (row + 1, col)
    if col < shape[1] - 1:
        yield (row, col + 1)
    

def dfs(visited, group, grid, target, row, col, shape):
    group.add((row, col))
    for nr, nc in neighbours(row, col, shape):
        if grid[nr][nc] != target:
            continue
        if (nr, nc) in visited:
            continue
        visited.add((nr, nc))
        dfs(visited, group, grid, target, nr, nc, shape)

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = [[c for c in line.strip()] for line in f.readlines()]
    print(lines)
    shape = (len(lines), len(lines[0]))

    visited = set()
    regions = []
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if (row, col) in visited:
                continue
            region = set()
            dfs(visited, region, lines, lines[row][col], row, col, shape)
            regions.append(region)
    # print(regions)
    # print(len(regions))
    total = 0
    for region in regions:
        area = len(region)
        perimeter = 0
        for thing in region:
            p = 4
            for neighbour in neighbours(thing[0], thing[1], shape):
                if neighbour in region:
                    p -= 1
            perimeter += p
        total += area * perimeter

    return total

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
