import random
import time

def create_grid(rows, cols):
    return [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]

def print_grid(grid):
    for row in grid:
        print(''.join(['*' if cell else ' ' for cell in row]))

def count_neighbors(grid, x, y):
    rows, cols = len(grid), len(grid[0])
    neighbors = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if 0 <= x + i < rows and 0 <= y + j < cols:
                neighbors += grid[x + i][y + j]
    return neighbors

def update_grid(grid):
    new_grid = [row.copy() for row in grid]
    for x in range(len(grid)):
        for y in range(len(grid[0]):
            neighbors = count_neighbors(grid, x, y)
            if grid[x][y] == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[x][y] = 0
            elif grid[x][y] == 0 and neighbors == 3:
                new_grid[x][y] = 1
    return new_grid

def main(rows, cols, generations):
    grid = create_grid(rows, cols)
    for _ in range(generations):
        print_grid(grid)
        grid = update_grid(grid)
        time.sleep(1)
