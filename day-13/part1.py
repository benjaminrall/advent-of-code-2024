# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict
import scipy
import scipy.optimize

# Placeholders to be filled when copying the template
PART = 1
DAY = 13
YEAR = 2024

# The expected result from the test input, if using a test input
TEST_RESULT = 480

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = [case.split('\n') for case in f.read().split('\n\n')]
    
    total = 0
    for case in lines:
        case = [case[i].split(': ')[1] for i in range(3)]
        p, q = list(map(lambda x : int(x[1:]), case[0].split(', ')))
        r, s = list(map(lambda x : int(x[1:]), case[1].split(', ')))
        x, y = list(map(lambda x : int(x[2:]), case[2].split(', ')))
        res = scipy.optimize.linprog([3, 1], A_eq=[[p, r], [q, s]], b_eq=[x, y], integrality=[1, 1])
        if res.success:
            total += res.fun

    return int(total)

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
