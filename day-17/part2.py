# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 2
DAY = 17
YEAR = 2024

# The expected result from the test input, if using a test input
TEST_RESULT = 117440

class VM:
    def __init__(self, a, b, c, instructions):
        self.a = a
        self.b = b
        self.c = c
        self.outputs = []
        self.instructions = instructions
        self.pointer = 0
    
    def get_combo_operand(self, operand):
        if 0 <= operand <= 3:
            return operand
        if operand == 4:
            return self.a
        if operand == 5:
            return self.b
        if operand == 6:
            return self.c
        raise Exception("Invalid operand")

    def execute(self):
        if self.pointer >= len(self.instructions) - 1:
            return True
        opcode = self.instructions[self.pointer]
        operand = self.instructions[self.pointer + 1]
        match opcode:
            case 0:
                self.adv(operand)
            case 1:
                self.bxl(operand)
            case 2:
                self.bst(operand)
            case 3:
                self.jnz(operand)
            case 4:
                self.bxc(operand)
            case 5:
                self.out(operand)
            case 6:
                self.bdv(operand)
            case 7:
                self.cdv(operand)
        return False

    def adv(self, operand):
        self.a //= pow(2, self.get_combo_operand(operand))
        self.pointer += 2

    def bxl(self, operand):
        self.b ^= operand
        self.pointer += 2
    
    def bst(self, operand):
        self.b = self.get_combo_operand(operand) % 8
        self.pointer += 2

    def jnz(self, operand):
        if self.a == 0:
            self.pointer += 2
            return
        self.pointer = operand

    def bxc(self, operand):
        self.b ^= self.c
        self.pointer += 2
        
    def out(self, operand):
        self.outputs.append(self.get_combo_operand(operand) % 8)
        self.pointer += 2

    def bdv(self, operand):
        self.b = self.a // pow(2, self.get_combo_operand(operand))
        self.pointer += 2

    def cdv(self, operand):
        self.c = self.a // pow(2, self.get_combo_operand(operand))
        self.pointer += 2

def search(a, program, i, reverse_f):
    if i == len(program):
        return a
    valid = []
    for key in reverse_f[program[-(i + 1)]]:
        if key >= 8 << (3 * i):
            continue
        x = key & (~7)
        y = (a << 3) & 1023
        if a == -1 or x == y:
            valid.append(key)

    for n in valid:
        na = (n & 7) + (a << 3) if a > 0 else n
        res = search(na, program, i + 1, reverse_f)
        if res:
            return res

    return None

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines() if len(line.strip()) > 0]
    
    b = int(lines[1].split(': ')[1])
    c = int(lines[2].split(': ')[1])
    program = list(map(int, lines[3].split(': ')[1].split(',')))

    f = {}
    for a in range(1024):
        vm = VM(a, b, c, program)
        while not vm.execute():
            pass
        f[a] = vm.outputs[0]

    reverse_f = defaultdict(set)
    for key in f:
        reverse_f[f[key]].add(key)

    return search(-1, program, 0, reverse_f)

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
