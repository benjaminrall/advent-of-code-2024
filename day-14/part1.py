# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 1
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

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        robots = [[parse(s) for s in line.strip().split()] for line in f.readlines()]
    quads = [0, 0, 0, 0]
    for p, v in robots:
        res = p + 100 * v
        x, y = (res.real % WIDTH, res.imag % HEIGHT)

        # print("\nNEW ROBOT")
        # print(x, y)
        # print(WIDTH // 2, HEIGHT // 2)
        if x < WIDTH // 2:
            if y < HEIGHT // 2:
                quads[0] += 1
            elif y > HEIGHT // 2:
                quads[1] += 1
        elif x > WIDTH // 2:
            if y < HEIGHT // 2:
                quads[2] += 1
            elif y > HEIGHT // 2:
                quads[3] += 1
        # print(quads)
    # print(quads)
    return quads[0] * quads[1] * quads[2] * quads[3]

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
