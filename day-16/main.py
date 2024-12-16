# Useful imports
import pyaoc
import math
import numpy as np
from functools import cache
from collections import defaultdict
import heapq

import sys
sys.setrecursionlimit(100000)

# Placeholders to be filled when copying the template
PART = 1
DAY = 16
YEAR = 2024

# The expected result from the test input, if using a test input
TEST_RESULT = 7036

DIRS = [-1, 1j, 1, -1j]

def get_neighbours(current):
    cdir = DIRS[current[1]]
    for i, dir in enumerate([cdir * 1j, cdir, cdir * -1j]):
        i = (current[1] - 1 + i) % 4
        cost = 1 if current[1] == i else 1001
        yield (current[0] + dir, i), cost

def dijkstra(graph: list[list[int]], weight: list[list[float]], source: int = 0, target: int | None = None) -> tuple[list[float], list[int]]:
    # Graph is an adjacency list, weight is a weight matrix
    n = len(graph)
    prec = defaultdict(lambda : None)
    black = defaultdict(lambda : False)
    dist = defaultdict(lambda : float('inf'))
    dist[source] = 0
    heap = [(0, source[0].real, source[0].imag, source)]
    while heap:
        dist_node, _, _ , node= heapq.heappop(heap) # Closest node from source
        if not black[node]:
            black[node] = True
            if node[0] == target:
                return dist_node
            for neighbor in graph[node]:
                dist_neighbor = dist_node + weight[(node, neighbor)]
                print(node, neighbor, weight[(node, neighbor)], dist_node, dist_neighbor)
                if dist_neighbor < dist[neighbor]:
                    dist[neighbor] = dist_neighbor
                    prec[neighbor] = node
                    
                    heapq.heappush(heap, (dist_neighbor, neighbor[0].real, neighbor[0].imag, neighbor))
    return dist, prec        


def construct(neighbours, dists, grid, visited, current):
    
    visited.add(current)
    # print(f"\nCURRENT: {current}")
    for neighbour, dist in get_neighbours(current):
        # print(f"NEIGHBOUR {neighbour}")
        if neighbour[0] not in grid or neighbour[0] in visited:
            continue
        neighbours[current].add(neighbour)
        dists[(current, neighbour)] = dist
        dists[(neighbour, current)] = dist
        construct(neighbours, dists, grid, visited, neighbour)

def to_tup(n):
    return (n.real, n.imag)

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    grid = set()
    start = None
    end = None
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c != '#':
                grid.add(i + 1j * j)
            if c == 'S':
                start = i + 1j * j
            if c == 'E':
                end = i + 1j * j
    
    neighbours = defaultdict(set)
    dists = {}
    start = (start, 1)
    construct(neighbours, dists, grid, set(), start)

    return dijkstra(neighbours, dists, start, end)

# Attempt to submit the current solve method
pyaoc.submit(
    solve, PART, DAY, YEAR, 
    test_result=TEST_RESULT,
    test=True
)