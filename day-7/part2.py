# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 2
DAY = 7
YEAR = 2024

# The expected result from the test input, if using a test input
TEST_RESULT = 11387

ops = {'+': lambda x : [x[0] + x[1]], '*': lambda x : [x[0] * x[1]], '||': lambda x : [int(str(x[0]) + str(x[1]))]}

def test(target, ns):
    if len(ns) == 1:
        return ns[0] == target
     
    for op in ops:
        f = ops[op]
        if test(target, f(ns[:2]) + ns[2:]):
            return True
    return False

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    
    cases = []
    for line in lines:
        target, ns = line.split(": ")
        cases.append((int(target), list(map(int, ns.split()))))
    
    total = 0
    for case in cases:
        if test(case[0], case[1]):
            total += case[0]
    
    return total

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
