# Useful imports
import math
import numpy as np
from functools import cache
from itertools import combinations
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 1
DAY = 23
YEAR = 2024

# The expected result from the test input, if using a test input
TEST_RESULT = 7

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    graph = defaultdict(set)
    nodes = set()
    for line in lines:
        a, b = line.split('-')
        graph[a].add(b)
        graph[b].add(a)
        nodes.add(a)
        nodes.add(b)

    triples = set()
    for node in nodes:
        for n1, n2 in combinations(graph[node], 2):
            if n1 in graph[n2]:
                triples.add(tuple(sorted([node, n1, n2])))
    total = 0
    for triple in triples:
        for n in triple:
            if n[0] == 't':
                total += 1
                break

    return total

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
