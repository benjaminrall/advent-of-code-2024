# Useful imports
import pyaoc
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
        # pos x raycast
        lengths1 = 0
        lengths2 = 0
        previous1 = None
        previous2 = None
        for i in range(0, shape[0]):
            for j in range(0, shape[1]):
                if (i, j) in region:
                    if j != previous1:
                        lengths1 += 1
                        previous1 = j
                    break
            for j in range(shape[1] - 1, -1, -1):
                if (i, j) in region:
                    if j != previous2:
                        lengths2 += 1
                        previous2 = j
                    break
        lengths3 = 0
        lengths4 = 0
        previous3 = None
        previous4 = None
        for i in range(0, shape[1]):
            for j in range(0, shape[0]):
                if (j, i) in region:
                    if j != previous3:
                        lengths3 += 1
                        previous3 = j
                    break
            for j in range(shape[0] - 1, -1, -1):
                if (j, i) in region:
                    if j != previous4:
                        lengths4 += 1
                        previous4 = j
                    break
        print(lengths1, lengths2, lengths3, lengths4)
        total += area * (lengths1 + lengths2 + lengths3 + lengths4)
            

    return total

# Attempt to submit the current solve method
pyaoc.submit(
    solve, PART, DAY, YEAR, 
    test_result=TEST_RESULT,
    test=True
)