# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 1
DAY = 6
YEAR = 2024

# The expected result from the test input, if using a test input
TEST_RESULT = 41
charmap = {'.': 0, '#': 1, '^': 2}
next_dir = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}


def get_slice(grid, row, col, dir) -> np.ndarray:
    if dir[0] != 0:
        return grid[row::dir[0], col]
    if dir[1] != 0:
        return grid[row, col::dir[1]]
    print("CRITICAL ERROR")
    return None

def set_slice(c, row, col, nr, nc, dir) -> np.ndarray:
    # print(dir, row, col, nr, nc)
    if dir[0] != 0:
        c[row+1:nr+1+dir[0]:dir[0], col+1] = 1
    if dir[1] != 0:
        c[row+1, col+1:nc+1+dir[1]:dir[1]] = 1

def get_new_pos(grid, row, col, dir):
    s = get_slice(grid, row, col, dir)
    indices = np.where(s == 1)[0]
    if indices.size == 0:
        indices = np.where(s == 0)[0]
        row = row + (dir[0] * (indices[-1]))
        col = col + (dir[1] * (indices[-1]))
        return True, row, col
    row = row + (dir[0] * (indices[0] - 1))
    col = col + (dir[1] * (indices[0] - 1))
    return False, row, col

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        grid = np.array([[charmap[c] for c in line.strip()] for line in f.readlines()])
    row, col = np.where(grid == 2)
    row = row[0]
    col = col[0]
    
    covered = np.zeros((grid.shape[0] + 2, grid.shape[1] + 2), dtype=int)
    direction = (-1, 0)
    done = False
    while not done:
        # print(row, col)
        done, nr, nc = get_new_pos(grid, row, col, direction)
        # print(nr, nc)
        set_slice(covered, row, col, nr, nc, direction)
        row = nr
        col = nc
        direction = next_dir[direction]
        print(covered)

    return np.sum(covered)

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
