import random
import time

def create_grid(rows, cols):
    return [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]

def print_grid(grid):
    for row in grid:
        print(''.join(['*' if cell else ' ' for cell in row]))

