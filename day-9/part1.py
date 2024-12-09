# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 1
DAY = 9
YEAR = 2024

# The expected result from the test input, if using a test input
TEST_RESULT = 1928

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        data = [list(map(int, line.strip())) for line in f.readlines()][0]
    
    disk = []
    empties = []
    empty = False
    id = 0
    i = 0
    L = 0
    for digit in data:
        for _ in range(digit):
            if not empty:
                disk.append(id)
                L += 1
            else:
                disk.append(-1)
                empties.append(i)
            i += 1
        if not empty:
            id += 1
        empty = not empty


    while len(disk) > L:
        next_element = disk.pop()
        if next_element != -1:
            next_empty = empties[0]
            disk[next_empty] = next_element
            empties = empties[1:]
        
    return sum([i * j for i,j in enumerate(disk)])

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
