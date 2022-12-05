from pathlib import Path
from typing import Iterator
from utils import get_neighbor_coords, get_neighbors, iter_coords, read_int_rows
from collections import deque
from statistics import median


class Octopus:
    has_glowed = False
    glows = 0

    def __init__(self, x, y, value, grid):
        self.x, self.y = x, y
        self.value = value
        self.grid = grid

    def grow(self):
        self.value += 1
        if self.value > 9 and not self.has_glowed:
            self.glow()

    def glow(self):
        Octopus.glows += 1
        self.has_glowed = True
        for neighbor in get_neighbors(self.x, self.y, self.grid):
            neighbor.grow()

    def reset(self):
        if self.has_glowed:
            self.value = 0
            self.has_glowed = False


def q1(grid):
    for x, y in iter_coords(grid):
        grid[y][x] = Octopus(x, y, grid[y][x], grid)

    for _ in range(100):
        for x, y in iter_coords(grid):
            grid[y][x].grow()
        for x, y in iter_coords(grid):
            grid[y][x].reset()

    return Octopus.glows


def q2(grid):
    for x, y in iter_coords(grid):
        grid[y][x] = Octopus(x, y, grid[y][x], grid)

    size = len(grid) * len(grid[0])
    previous_glows = 0
    step_count = 0
    while Octopus.glows - previous_glows != size:
        previous_glows = Octopus.glows
        for x, y in iter_coords(grid):
            grid[y][x].grow()
        for x, y in iter_coords(grid):
            grid[y][x].reset()
        step_count += 1

    return step_count


def main():
    values = read_int_rows("./11.txt")
    print(q1(values))
    values = read_int_rows("./11.txt")
    print(q2(values))


if __name__ == "__main__":
    main()
