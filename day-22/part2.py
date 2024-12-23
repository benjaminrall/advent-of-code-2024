# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict
from tqdm import tqdm

# Placeholders to be filled when copying the template
PART = 2
DAY = 22
YEAR = 2024

# The expected result from the test input, if using a test input
TEST_RESULT = 23

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

    N = 2000

    sequence_maps = []
    all_sequences = set()
    for start in tqdm(lines):
        sequences = set()
        history = [None for _ in range(N)]
        history[-1] = (start, start % 10)
        sequence_map = defaultdict(int)
        changes = []
        for i in range(N):
            n, p = history[i - 1]
            new_n = sim(n)
            new_p = new_n % 10
            history[i] = (new_n, new_p)
            change = new_p - p
            changes.append(change)
            if len(changes) >= 4:
                sequence = tuple(changes[-4:])
                if sequence not in sequences:
                    sequences.add(sequence)
                    sequence_map[sequence] = new_p
        sequence_maps.append(sequence_map)
        all_sequences.update(sequences)

    best = 0
    for sequence in tqdm(all_sequences):
        total = 0
        for m in sequence_maps:
            total += m[sequence]
        best = max(total, best)
    return best

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
