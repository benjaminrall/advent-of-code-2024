# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 1
DAY = 11
YEAR = 2024

# The expected result from the test input, if using a test input
TEST_RESULT = 55312

@cache
def blink(stone):
    if stone == '0':
        return ['1']
    if len(stone) % 2 == 0:
        return [str(int(stone[:len(stone) // 2])), str(int(stone[len(stone) // 2:]))]
    return [str(int(stone) * 2024)]
    

def blink_stones(stones):
    new_stones = []
    for stone in stones:
        new_stones.extend(blink(stone))
    return new_stones

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        stones = [line.strip() for line in f.readlines()][0].split()
    
    for i in range(25):
        stones = blink_stones(stones)

    return len(stones)

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
