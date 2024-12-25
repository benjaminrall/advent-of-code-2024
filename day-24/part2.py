# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict,deque
# Placeholders to be filled when copying the template
PART = 2
DAY = 24
YEAR = 2024

# The expected result from the test input, if using a test input
TEST_RESULT = -1

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # Errors were found by manually going through the input and organising into single bit adders
    return "cqr,ncd,nfj,qnw,vkg,z15,z20,z37"

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
