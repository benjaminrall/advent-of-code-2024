# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 1
DAY = 15
YEAR = 2024

# The expected result from the test input, if using a test input
TEST_RESULT = 2028

MOVES_MAP = {'<': -1j, '>': 1j, '^': -1, 'v': 1}

def simulate(robot, boxes, walls, move):
    next_pos = robot + move
    if next_pos in walls:
        return robot
    if next_pos not in boxes:
        return next_pos
    # move boxes
    next_box_pos = next_pos + move
    while next_box_pos in boxes:
        next_box_pos += move
    if next_box_pos in walls:
        return robot
    boxes.remove(next_pos)
    boxes.add(next_box_pos)
    return next_pos

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = f.read().strip().split('\n\n')
    
    grid = lines[0].split('\n')
    robot = None
    boxes = set()
    walls = set()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '#':
                walls.add(row + col * 1j)
            elif grid[row][col] == 'O':
                boxes.add(row + col * 1j)
            elif grid[row][col] == '@':
                robot = row + col * 1j

    moves = [MOVES_MAP[c] for c in lines[1] if c in MOVES_MAP]
    
    for move in moves:
        robot = simulate(robot, boxes, walls, move)

    # for row in range(len(grid)):
    #     for col in range(len(grid[0])):
    #         pos = row + col * 1j
    #         if pos in boxes:
    #             print("O", end="")
    #         elif pos in walls:
    #             print("#", end="")
    #         elif pos == robot:
    #             print("@", end="")
    #         else:
    #             print(".", end="")

    return int(sum([100 * box.real + box.imag for box in boxes]))

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
