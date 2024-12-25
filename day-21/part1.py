# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict
import heapq

# Placeholders to be filled when copying the template
PART = 1
DAY = 21
YEAR = 2024

# The expected result from the test input, if using a test input
TEST_RESULT = 126384

NUMPAD = {
    '0': 3 + 1j,
    '1': 2 + 0j,
    '4': 1 + 0j,
    '7': 0 + 0j,
    '8': 1j,
    '5': 1 + 1j,
    '2': 2 + 1j,
    '9': 2j,
    '6': 1 + 2j,
    '3': 2 + 2j,
    'A': 3 + 2j
}
NUMPAD_POS = {
    0, 
    1, 
    2,
    1j,
    1 + 1j,
    2 + 1j,
    3 + 1j,
    2j,
    1 + 2j,
    2 + 2j,
    3 + 2j
}

DIRPAD = {
    '^': 1j,
    'A': 2j,
    '<': 1,
    'v': 1 + 1j,
    '>': 1 + 2j,
}
DIRPAD_POS = {
    1j,
    2j,
    1 + 0j,
    1 + 1j,
    1 + 2j,
}
INV_DIRPAD = {
    1j: -1,
    2j: 0,
    1: -1j,
    1 + 1j: 1,
    1 + 2j: 1j,
}

def path(p1, p2):
    out = ''
    # 0 -> 2,  3 + 1j -> 2 + 1j
    v = int(p2.real - p1.real)
    if v > 0:
        for _ in range(v):
            out += '^'
    else:
        for _ in range(-v):
            out += 'v'
    # A -> 0, 3 + 2j -> 3 + 1j
    h = int(p1.imag - p2.imag)
    if h > 0:
        for _ in range(h):
            out += '>'
    else:
        for _ in range(-h):
            out += '<'
    return out

# def direct_neighbours(current):
#     yield 1, current - 1j
#     yield 1, current + 1
#     yield 1, current + 1j
#     yield 1, current - 1

# def get_valid_neighbours(valid, current):
#     for n in direct_neighbours(current):
#         if n[1] in valid:
#             yield n

def activate(node):
    new_node = [n for n in node]
    for i in range(len(node) - 2, 0, -1):
        d = INV_DIRPAD[node[i]]
        new_node[i - 1] += d
        if d != 0:
            break
    return new_node

def valid(node):
    return node[0] in NUMPAD_POS and node[1] in DIRPAD_POS and node[2] in DIRPAD_POS

def dir_neighbours(pos):
    yield pos + 1j
    yield pos - 1j
    yield pos + 1
    yield pos - 1

def get_neighbours(node):
    node = list(node)
    if node[-1]:
        node = activate(node)
        node[-1] = False
    neighbours = []
    for neighbour in dir_neighbours(node[-2]):
        if neighbour not in DIRPAD_POS:
            continue
        neighbours.append((*node[:-2], neighbour, False))
    activated_node = activate(node)
    if valid(activated_node):
        node[-1] = True
        neighbours.append(tuple(node))
    return neighbours

def hash(node):
    h = []
    for e in node[:-1]:
        h.append(e.real)
        h.append(e.imag)
    h.append(int(node[-1]))
    return h


def dijkstra(source: int = 0, target: int | None = None) -> tuple[list[float], list[int]]:
    # Graph is an adjacency list, weight is a weight matrix
    prec = defaultdict(lambda : None)
    black = defaultdict(lambda : False)
    dist = defaultdict(lambda : float('inf'))
    dist[source] = 0
    heap = [(0, hash(source), source)]
    while heap:
        dist_node, _, node = heapq.heappop(heap) # Closest node from source
        if not black[node]:
            black[node] = True
            if node == target:
                return dist_node
            # print(node, get_neighbours(node))
            for neighbor in get_neighbours(node):
                dist_neighbor = dist_node + 1
                if dist_neighbor < dist[neighbor]:
                    dist[neighbor] = dist_neighbor
                    prec[neighbor] = node
                    heapq.heappush(heap, (dist_neighbor, hash(neighbor), neighbor))
    return None


DIRS = {1j: '<', -1j: '>', 1: '^', -1: 'v', 2j: '<<', -2j: '>>', 2: '^^', -2: 'vv'}
def path(start, target):
    d = dijkstra(start, target)
    return d

def process(code):
    start = (NUMPAD['A'], DIRPAD['A'], DIRPAD['A'], False)
    paths = []
    for c in code:
        target = (NUMPAD[c], DIRPAD['A'], DIRPAD['A'], True)
        paths.append(path(start, target))
        start = target
    return sum(paths) * int(code[:-1])

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    return sum([process(code) for code in lines])

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
