# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 1
DAY = 22
YEAR = 2024

# The expected result from the test input, if using a test input
TEST_RESULT = 37327623

def mix(n, m):
    return n ^ m

def prune(n):
    return n % 16777216

def sim(n):
    one = prune(mix(n, n * 64))
    two = prune(mix(one, one // 32))
    three = prune(mix(two, two * 2048))
    return three

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = [int(line.strip()) for line in f.readlines()]
            
    total = 0
    for start in lines:
        for i in range(2000):
            start = sim(start)
        total += start

    return total

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
