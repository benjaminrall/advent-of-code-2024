# Useful imports
import math
import numpy as np
from functools import cache
from itertools import combinations
from collections import defaultdict
from tqdm import tqdm
import networkx as nx

# Placeholders to be filled when copying the template
PART = 2
DAY = 23
YEAR = 2024

# The expected result from the test input, if using a test input
TEST_RESULT = "co,de,ka,ta"

def connected(graph, nodes):
    for i in range(len(nodes)):
        n1 = nodes[i]
        for n2 in nodes[:i] + nodes[i + 1:]:
            if n2 not in graph[n1]:
                return False
    return True

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    graph = nx.Graph()
    for line in lines:
        a, b = line.split('-')
        graph.add_edge(a, b)
  
    return ','.join(sorted(max(nx.find_cliques(graph), key=len)))
    

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
