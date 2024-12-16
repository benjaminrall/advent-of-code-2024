# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 2
DAY = 12
YEAR = 2024

# The expected result from the test input, if using a test input
TEST_RESULT = 1206

def neighbours(row, col, shape):
    if row > 0:
        yield (row - 1, col)
    if col > 0:
        yield(row, col - 1)
    if row < shape[0] - 1:
        yield (row + 1, col)
    if col < shape[1] - 1:
        yield (row, col + 1)

def neighbours2(row, col):
    yield (row - 1, col)
    yield(row, col - 1)
    yield (row + 1, col)
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

def dfs2(fences: set, res: set, fence):
    res.add(fence)
    for neighbour in neighbours2(fence[0][0], fence[0][1]):
        if (neighbour, fence[1]) in fences and (neighbour, fence[1]) not in res:
            dfs2(fences, res, (neighbour, fence[1]))

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = [[c for c in line.strip()] for line in f.readlines()]
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

    total = 0
    for region in regions:
        area = len(region)
        fences = set()
        for thing in region:
            for i, neighbour in enumerate(neighbours2(thing[0], thing[1])):
                if neighbour not in region:
                    fences.add((neighbour, i))

        total_lengths = 0
        while len(fences)> 0:
            total_lengths += 1
            lengths = set()
            dfs2(fences, lengths, fences.pop())
            for length in lengths:
                if length in fences:
                    fences.remove(length)

        total += area * total_lengths
            

    return total

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
