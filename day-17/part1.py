# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 1
DAY = 17
YEAR = 2024

# The expected result from the test input, if using a test input
TEST_RESULT = "4,6,3,5,6,3,5,2,1,0"

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

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines() if len(line.strip()) > 0]
    
    a = int(lines[0].split(': ')[1])
    b = int(lines[1].split(': ')[1])
    c = int(lines[2].split(': ')[1])
    program = list(map(int, lines[3].split(': ')[1].split(',')))

    vm = VM(a, b, c, program)
    while not vm.execute():
        pass

    return ','.join([str(e) for e in vm.outputs])

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
