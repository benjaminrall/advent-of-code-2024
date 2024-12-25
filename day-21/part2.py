# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict
import heapq

# Placeholders to be filled when copying the template
PART = 2
DAY = 21
YEAR = 2024

# The expected result from the test input, if using a test input
TEST_RESULT = 0


NUMPAD = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    [' ', '0', 'A'],
]

DIRPAD = [
    [' ', '^', 'A'],
    ['<', 'v', '>']
]

def get_index(keypad, char):
    for y, row in enumerate(keypad):
        for x, c in enumerate(row):
            if c == char:
                return (x, y)
    assert False

def path(keypad, sx, sy, ex, ey, p=""):
    if sx == ex and sy == ey:
        yield p + 'A'
    if ex < sx and keypad[sy][sx - 1] != ' ':
        yield from path(keypad, sx - 1, sy, ex, ey, p + '<')
    if ey < sy and keypad[sy - 1][sx] != ' ':
        yield from path(keypad, sx, sy - 1, ex, ey, p + '^')
    if ey > sy and keypad[sy + 1][sx] != ' ':
        yield from path(keypad, sx, sy + 1, ex, ey, p + 'v')
    if ex > sx and keypad[sy][sx + 1] != ' ':
        yield from path(keypad, sx + 1, sy, ex, ey, p + '>')

def path_value(path):
    turns = 0
    for n1, n2 in zip('A' + path, path):
        if n1 != n2:
            turns += 1
    return turns

def dist(keypad, start, end):
    sx, sy = get_index(keypad, start)
    ex, ey = get_index(keypad, end)
    return min(path(keypad, sx, sy, ex, ey), key = path_value)

@cache
def count(code, depth):
    if depth > 25:
        return len(code)
    total = 0
    for start, end in zip('A' + code, code):
        total += count(dist(DIRPAD if depth else NUMPAD, start, end), depth + 1)
    return total

def process(code):
    return count(code, 0) * int(code[:3])

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    return sum([process(code) for code in lines])

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
