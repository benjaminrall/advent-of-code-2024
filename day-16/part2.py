# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict
import heapq


# Placeholders to be filled when copying the template
PART = 2
DAY = 16
YEAR = 2024

# The expected result from the test input, if using a test input
TEST_RESULT = 45

DIRS = [-1, 1j, 1, -1j]

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

def get_neighbours(grid, current):
    cdir = DIRS[current[1]]
    for i, dir in enumerate([cdir * 1j, cdir, cdir * -1j]):
        i = (current[1] - 1 + i) % 4
        cost = 1 if current[1] == i else 1001
        neighbour = current[0] + dir
        if neighbour in grid:
            yield (neighbour, i), cost

def dijkstra(grid, source: int = 0, target: int | None = None) -> tuple[list[float], list[int]]:
    prec = defaultdict(lambda : [])
    black = defaultdict(lambda : False)
    dist = defaultdict(lambda : float('inf'))
    dist[source] = 0
    heap = [(0, source[0].real, source[0].imag, source)]
    while heap:
        dist_node, _, _ , node= heapq.heappop(heap) # Closest node from source
        if not black[node]:
            black[node] = True
            if node[0] == target:
                return dist, prec, node
            for neighbor, w in get_neighbours(grid, node):
                dist_neighbor = dist_node + w
                # print(node, neighbor, weight[(node, neighbor)], dist_node, dist_neighbor)
                if dist_neighbor <= dist[neighbor]:
                    dist[neighbor] = dist_neighbor
                    prec[neighbor].append(node)
                    
                    heapq.heappush(heap, (dist_neighbor, neighbor[0].real, neighbor[0].imag, neighbor))
    return dist, prec        


def backtrack(prec, current, target, visited):
    visited.add(current[0])
    if current == target:
        return
    for p in prec[current]:
        backtrack(prec, p, target, visited)

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
    # construct(neighbours, dists, grid, set(), start)

    dist, prec, end = dijkstra(grid, start, end)

    visited = set()
    backtrack(prec, end, start, visited)
    return len(visited)

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
