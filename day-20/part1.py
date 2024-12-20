# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict
import heapq

# Placeholders to be filled when copying the template
PART = 1
DAY = 20
YEAR = 2024

# The expected result from the test input, if using a test input
TEST_RESULT = -1

def direct_neighbours(current):
    yield current + 1
    yield current - 1
    yield current + 1j
    yield current - 1j

def cheat_neighbours(valid, current):
    for i in range(-2, 3):
        for j in range(-2, 3):
            if i != 0 and j != 0: continue
            offset = i + j * 1j
            n = current[0] + offset
            if n in valid:
                yield (n, 1)

def get_valid_neighbours(valid, current):
    for n in direct_neighbours(current[0]):
        if n in valid:
            yield 1, (n, current[1])
    if not current[1]:
        for n in cheat_neighbours(valid, current):
            yield 2, n


def dijkstra(grid, source: int = 0, target: int | None = None, excluded: set = set()) -> tuple[list[float], list[int]]:
    # Graph is an adjacency list, weight is a weight matrix
    prec = defaultdict(lambda : None)
    black = defaultdict(lambda : False)
    dist = defaultdict(lambda : float('inf'))
    dist[source] = 0
    heap = [(0, source[0].real, source[0].imag, source)]
    while heap:
        dist_node, _, _ , node = heapq.heappop(heap) # Closest node from source
        if not black[node]:
            black[node] = True
            if node == target:
                return dist_node, prec
            for d, neighbor in get_valid_neighbours(grid, node):
                if (node, neighbor) in excluded:
                    continue
                dist_neighbor = dist_node + d
                if dist_neighbor < dist[neighbor]:
                    dist[neighbor] = dist_neighbor
                    prec[neighbor] = node
                    heapq.heappush(heap, (dist_neighbor, neighbor[0].real, neighbor[0].imag, neighbor))
    return None

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    
    positions = set()
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c != '#':
                positions.add(i + j * 1j)
            if c == 'S':
                start = i + j * 1j
            if c == 'E':
                end = i + j * 1j
    od = dijkstra(positions, (start, 0), (end, 0))[0]
    
    THRESHOLD = 100
    excluded = set()
    count = 0
    while True:
        nd, prec = dijkstra(positions, (start, 0), (end, 1), excluded)
        cheat = None
        p = (end, 1)
        while p:
            np = prec[p]
            if np[1] == 0:
                cheat = (np, p)
                break
            p = np
        if od - nd < THRESHOLD:
            break
        print(od - nd, end="\r")
        excluded.add(cheat)
        count += 1
    return count

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
