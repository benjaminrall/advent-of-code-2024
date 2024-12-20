# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict
import heapq

# Placeholders to be filled when copying the template
PART = 2
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
    for i in range(-20, 21):
        for j in range(-20, 21):
            d = abs(i) + abs(j)
            if d > 20:
                continue
            offset = i + j * 1j
            n = current + offset
            if n in valid:
                yield d, n

def get_valid_neighbours(valid, current):
    for n in direct_neighbours(current):
        if n in valid:
            yield n


def dijkstra(grid, source: int = 0, target: int | None = None) -> tuple[list[float], list[int]]:
    # Graph is an adjacency list, weight is a weight matrix
    prec = defaultdict(lambda : None)
    black = defaultdict(lambda : False)
    dist = defaultdict(lambda : float('inf'))
    dist[source] = 0
    heap = [(0, source.real, source.imag, source)]
    while heap:
        dist_node, _, _ , node = heapq.heappop(heap) # Closest node from source
        if not black[node]:
            black[node] = True
            if node == target:
                return dist
            for neighbor in get_valid_neighbours(grid, node):
                dist_neighbor = dist_node + 1
                if dist_neighbor < dist[neighbor]:
                    dist[neighbor] = dist_neighbor
                    prec[neighbor] = node
                    heapq.heappush(heap, (dist_neighbor, neighbor.real, neighbor.imag, neighbor))
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
    dists = dijkstra(positions, end, start)
    total = 0
    THRESHOLD = 100

    for pos in positions:
        od = dists[pos]
        for d, neighbour in cheat_neighbours(positions, pos):
            nd = dists[neighbour]
            saved = od - (d + nd)
            if saved >= THRESHOLD:
                total += 1

    return total
    

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
