# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict
import heapq

# Placeholders to be filled when copying the template
PART = 1
DAY = 18
YEAR = 2024


def get_neighbours(current):
    yield current + 1
    yield current - 1
    yield current + 1j
    yield current - 1j

def get_valid_neighbours(valid, current):
    for n in get_neighbours(current):
        if n.real >= 0 and n.real <= SIZE and n.imag >= 0 and n.imag <= SIZE and valid[n]:
            yield n

def dijkstra(grid, source: int = 0, target: int | None = None) -> tuple[list[float], list[int]]:
    # Graph is an adjacency list, weight is a weight matrix
    prec = defaultdict(lambda : None)
    black = defaultdict(lambda : False)
    dist = defaultdict(lambda : float('inf'))
    dist[source] = 0
    heap = [(0, source.real, source.imag, source)]
    while heap:
        dist_node, _, _ , node= heapq.heappop(heap) # Closest node from source
        if not black[node]:
            black[node] = True
            if node == target:
                return dist_node
            for neighbor in get_valid_neighbours(grid, node):
                dist_neighbor = dist_node + 1
                # print(node, neighbor, weight[(node, neighbor)], dist_node, dist_neighbor)
                if dist_neighbor < dist[neighbor]:
                    dist[neighbor] = dist_neighbor
                    prec[neighbor] = node
                    
                    heapq.heappush(heap, (dist_neighbor, neighbor.real, neighbor.imag, neighbor))
    return dist, prec        

# The expected result from the test input, if using a test input
TEST_RESULT = -1

SIZE = 70
BYTES = 1024

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    # print(lines)

    valid = defaultdict(lambda : True)
    for coord in lines[:BYTES]:
        y, x = list(map(int, coord.split(','))) 
        valid[y + x * 1j] = False

    return dijkstra(valid, 0, SIZE + SIZE * 1j)

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
