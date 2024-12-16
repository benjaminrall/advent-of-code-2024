# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 2
DAY = 14
YEAR = 2024

# The expected result from the test input, if using a test input
TEST_RESULT = -1

WIDTH = 101
HEIGHT = 103

def parse(s):
    s = s.split('=')[1]
    y, x = s.split(',')
    return int(y) + int(x) * 1j

def gen_tree():
    tree = [[False for _ in range(WIDTH)] for _ in range(HEIGHT)]
    tree = set()
    for row in range(HEIGHT - 1):
        for col in range(WIDTH // 2 - row, WIDTH // 2 + row + 1):
            tree.add(col + row * 1j)
    tree.add(WIDTH // 2 + (HEIGHT - 1) * 1j)
    return tree

def is_tree(robots):
    tree = gen_tree()
    for pos, v in robots:
        if pos not in tree:
            return False
    return True

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        robots = [[parse(s) for s in line.strip().split()] for line in f.readlines()]
    quads = [0, 0, 0, 0]
    i = 0
    while True:
        for j in range(len(robots)):
            robots[j][0] += robots[j][1]
            robots[j][0] = robots[j][0].real % WIDTH + (robots[j][0].imag % HEIGHT) * 1j
        i += 1
        
        exists = set()
        for pos, _ in robots:
            exists.add(pos)
        for row in range(HEIGHT):
            for col in range(WIDTH):
                if row + col * 1j in exists:
                    print("#", end="")
                else:
                    print(" ", end="")
            print()
        x = input("Continue? ").lower().startswith("y")
        if x:
            return i

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
