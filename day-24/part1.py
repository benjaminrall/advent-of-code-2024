# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict,deque
# Placeholders to be filled when copying the template
PART = 1
DAY = 24
YEAR = 2024

# The expected result from the test input, if using a test input
TEST_RESULT = 2024

def execute(a, op, b):
    if op == 'AND':
        return a & b
    if op == 'OR':
        return a | b
    if op == 'XOR':
        return 1 if a != b else 0


# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        inits, instructions = f.read().split('\n\n')
    base_values = {}
    for init in inits.split('\n'):
        l, n = init.split(': ')
        base_values[l] = int(n)

    bits = set()
    values = {}
    for instruction in instructions.strip().split('\n'):
        a, op, b, _, res = instruction.split(' ')
        values[res] = [a, op, b]
        if res[0] == 'z':
            bits.add(res)

    @cache
    def evaluate(target):
        if target in base_values:
            return base_values[target]
        a, op, b = values[target]
        return execute(evaluate(a), op, evaluate(b))
    
    out = 0
    for bit in reversed(sorted(bits)):
        out <<= 1
        out |= evaluate(bit)

    return out

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
