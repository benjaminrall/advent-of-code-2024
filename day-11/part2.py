# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 2
DAY = 11
YEAR = 2024

# The expected result from the test input, if using a test input
TEST_RESULT = None

mappings = {}

@cache
def blink(stone):
    if stone == '0':
        return ['1']
    if len(stone) % 2 == 0:
        return [str(int(stone[:len(stone) // 2])), str(int(stone[len(stone) // 2:]))]
    return [str(int(stone) * 2024)]
    

def blink_stones(stone_counts):
    new_stone_counts = defaultdict(int)
    for stone in stone_counts:
        if stone not in mappings:
            mappings[stone] = blink(stone)
        c = stone_counts[stone]
        for res in mappings[stone]:
            new_stone_counts[res] += c
    return new_stone_counts

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        stones = [line.strip() for line in f.readlines()][0].split()
    stone_counts = defaultdict(int)

    for stone in stones:
        stone_counts[stone] += 1
    print(stone_counts)

    for i in range(75):
        stone_counts = blink_stones(stone_counts)

    return sum([stone_counts[key] for key in stone_counts])

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
