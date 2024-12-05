# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 1
DAY = 4
YEAR = 2024

# The expected result from the test input, if using a test input
TEST_RESULT = 18

LETTERS = 'XMAS'

def search_horizontal(grid, y, x, dir):
    for i in range(0, dir * 4, dir):
        xi = x + i
        if xi < 0 or xi >= grid.shape[1]:
            return False
        if grid[y, xi] != np.abs(i):
            return False
    return True

def search_vertical(grid, y, x, dir):
    for i in range(0, dir * 4, dir):
        yi = i + y
        if yi < 0 or yi >= grid.shape[0]:
            return False
        if grid[yi, x] != np.abs(i) :
            return False
    return True

def search_diagonal_1(grid, y, x, dir):
    for i in range(0, dir * 4, dir):
        yi = i + y
        xi = i + x
        if xi < 0 or xi >= grid.shape[1]:
            return False
        if yi < 0 or yi >= grid.shape[0]:
            return False
        if grid[yi, xi] != np.abs(i):
            return False
    return True

def search_diagonal_2(grid, y, x, dir):
    for i in range(0, dir * 4, dir):
        yi = i + y
        xi = x - i
        if xi < 0 or xi >= grid.shape[1]:
            return False
        if yi < 0 or yi >= grid.shape[0]:
            return False
        if grid[yi, xi] != np.abs(i):
            return False
    return True


# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = [[LETTERS.find(c) for c in line.strip()] for line in f.readlines()]
    
    grid = np.array(lines)
    print(grid)
    found = 0
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            if grid[y, x] != 0:
                continue
            found_e = 0
            if search_horizontal(grid, y, x, 1):
                # print("h1")
                found_e += 1
            if search_horizontal(grid, y, x, -1):
                # print("h-1")
                found_e += 1
            if search_vertical(grid, y, x, 1):
                # print("v1")
                found_e += 1
            if search_vertical(grid, y, x, -1):
                # print("v-1")
                found_e += 1
            if search_diagonal_1(grid, y, x, 1):
                # print("a")
                found_e += 1
            if search_diagonal_1(grid, y, x, -1):
                # print("b")
                found_e += 1
            if search_diagonal_2(grid, y, x, 1):
                # print("c")
                found_e += 1
            if search_diagonal_2(grid, y, x, -1):
                # print("d")
                found_e += 1
            found += found_e
            # print(found_e)
            # exit()

    return found

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
