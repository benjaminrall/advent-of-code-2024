# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 2
DAY = 15
YEAR = 2024

# The expected result from the test input, if using a test input
TEST_RESULT = 9021

MOVES_MAP = {'<': -1j, '>': 1j, '^': -1, 'v': 1}

def can_move_box(box, boxes, box_map, walls, move):
    np1 = box + move
    np2 = box_map[box] + move
    if np1 in walls or np2 in walls:
        return False
    two_boxes = np2 in boxes and (np1 not in boxes or np2 != box_map[np1])
    if np1 in boxes:
        if not can_move_box(np1, boxes, box_map, walls, move):
            return False
    if two_boxes:
        if not can_move_box(np2, boxes, box_map, walls, move):
            return False
    return True

def move_box(box, boxes, box_map, walls, move, moved):
    if box in moved:
        return
    np1 = box + move
    np2 = box_map[box] + move
    two_boxes = np2 in boxes and (np1 not in boxes or np2 != box_map[np1])
    if np1 in boxes:
        move_box(np1, boxes, box_map, walls, move, moved)
    if two_boxes:
        move_box(np2, boxes, box_map, walls, move, moved)
    boxes.add(np1)
    boxes.add(np2)
    boxes.remove(box)
    boxes.remove(box_map[box])
    box_map[np1] = np2
    box_map[np2] = np1
    moved.add(box)
    moved.add(box_map[box])

def simulate(robot, boxes, box_map, walls, move):
    next_pos = robot + move
    if next_pos in walls:
        return robot
    if next_pos not in boxes:
        return next_pos
    
    # move boxes horizontally
    if move.imag != 0:
        next_box_pos = next_pos + move
        while next_box_pos in boxes:
            next_box_pos += move
        if next_box_pos in walls:
            return robot
        boxes.remove(next_pos)
        boxes.add(next_box_pos)
        while next_box_pos != next_pos:
            box_map[next_box_pos] = next_box_pos - move
            box_map[next_box_pos - move] = next_box_pos
            next_box_pos -= 2 * move
        return next_pos

    # move boxes vertically
    if not can_move_box(next_pos, boxes, box_map, walls, move):
        return robot
    move_box(next_pos, boxes, box_map, walls, move, set())
    return next_pos
    


# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = f.read().strip().split('\n\n')
    
    grid = lines[0].split('\n')
    robot = None
    boxes = set()
    box_map = {}
    walls = set()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '#':
                walls.add(row + col * 2j)
                walls.add(row + col * 2j + 1j)
            elif grid[row][col] == 'O':
                b1 = row + col * 2j
                b2 = row + col * 2j + 1j
                boxes.add(b1)
                boxes.add(b2)
                box_map[b1] = b2
                box_map[b2] = b1
            elif grid[row][col] == '@':
                robot = row + col * 2j

    moves = [MOVES_MAP[c] for c in lines[1] if c in MOVES_MAP]
    
    def display():
        for row in range(len(grid)):
            for col in range(len(grid[0]) * 2):
                pos = row + col * 1j
                if pos in boxes:
                    print("O", end="")
                elif pos in walls:
                    print("#", end="")
                elif pos == robot:
                    print("@", end="")
                else:
                    print(".", end="")
            print()

    display()
    for move in moves:
        robot = simulate(robot, boxes, box_map, walls, move)
    display()

    total = 0
    while len(boxes) > 0:
        box = boxes.pop()
        box2 = box_map[box]
        boxes.remove(box2)
        box = box if box.imag < box2.imag else box2
        total += box.real * 100 + box.imag

    return int(total)

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
