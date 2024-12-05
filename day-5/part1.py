# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 1
DAY = 5
YEAR = 2024

# The expected result from the test input, if using a test input
TEST_RESULT = 143


def valid_n(case, rulesets, i, n):
    if n not in rulesets:
        return True
    for r in rulesets[n]:
        if r in case[:i]:
            return False
    return True

def valid(case, rulesets):
    for i, n in enumerate(case):
        if not valid_n(case, rulesets, i, n):
            return False
    return True


# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    
    rules = []
    cases = []
    active = rules
    for line in lines:
        if line == '':
            active = cases
            continue
        active.append(line)
    
    rulesets = defaultdict(set)

    for rule in rules:
        a, b = map(int, rule.split('|'))
        rulesets[a].add(b)
    
    total = 0

    cases = [list(map(int, case.split(','))) for case in cases]
    for case in cases:
        if valid(case, rulesets):
            total += case[len(case) // 2]

    return total

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
