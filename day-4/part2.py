# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 2
DAY = 4
YEAR = 2024

# The expected result from the test input, if using a test input
TEST_RESULT = 9

LETTERS = 'XMAS'

def check_1(grid, y, x):
    i = [[y - 1, x - 1], [y + 1, x - 1], [y - 1, x + 1], [y + 1, x + 1]]

    if grid[*i[0]] == 1 and grid[*i[1]] == 1 and grid[*i[2]] == 3 and grid[*i[3]] == 3:
        return True

def check_2(grid, y, x):
    i = [[y - 1, x - 1], [y - 1, x + 1], [y + 1, x - 1], [y + 1, x + 1]]

    if grid[*i[0]] == 1 and grid[*i[1]] == 1 and grid[*i[2]] == 3 and grid[*i[3]] == 3:
        return True
    
def check_3(grid, y, x):
    i = [[y - 1, x + 1], [y + 1, x + 1], [y - 1, x - 1], [y + 1, x - 1]]

    if grid[*i[0]] == 1 and grid[*i[1]] == 1 and grid[*i[2]] == 3 and grid[*i[3]] == 3:
        return True
    
def check_4(grid, y, x):
    i = [[y + 1, x - 1], [y + 1, x + 1], [y - 1, x - 1], [y - 1, x + 1]]

    if grid[*i[0]] == 1 and grid[*i[1]] == 1 and grid[*i[2]] == 3 and grid[*i[3]] == 3:
        return True

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = [[LETTERS.find(c) for c in line.strip()] for line in f.readlines()]
    
    grid = np.array(lines)
    print(grid)
    found = 0
    for y in range(1, grid.shape[0] - 1):
        for x in range(1, grid.shape[1] - 1):
            if grid[y, x] != 2:
                continue
            if check_1(grid, y, x):
                found += 1
            if check_2(grid, y, x):
                found += 1
            if check_3(grid, y, x):
                found += 1
            if check_4(grid, y, x):
                found += 1

    return found

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
